import re
import sys

import overpy
import requests


def download_city_address(name):
    api = overpy.Overpass()
    query = f'[out:json][timeout:10000];(area[name="{name}"]->.a;node(area.a)["addr:street"];way(area.a)["addr:street"];relation(area.a)["addr:street"];);out body; >; out skel qt;'
    try:
        osm_json = api.query(query)
    except overpy.exception.OverpassTooManyRequests:
        print("Ошибка сервера OSM. Запустите еще раз.")
        sys.exit(0)
    except overpy.exception.OverpassGatewayTimeout:
        print("Ошибка сервера OSM. Запустите еще раз.")
        sys.exit(0)
    finally:
        requests.get(r"http://overpass-api.de/api/kill_my_queries")
    addresses = set()
    for address in osm_json.nodes:
        if len(address.tags) != 0:
            address.tags["lat"] = str(address.lat)
            address.tags["lon"] = str(address.lon)
            addresses.add(address)

    for cells in [osm_json.ways, osm_json.relations]:
        for address in cells:
            if len(address.tags) != 0:
                addresses.add(address)
    region = find_region_of_city(name)
    full_city_addresses = handling_addresses(addresses, region)
    return full_city_addresses


def handling_addresses(addresses: set, region):
    for address in addresses:
        try:
            address.tags["region"] = region
            if address.nodes:
                address.tags["lat"] = address.nodes[0].lat
                address.tags["lon"] = address.nodes[0].lon
        except AttributeError:
            continue
    parsed_city_addresses = set()
    for address in addresses:
        if check_to_add(address):
            address = dict(
                region=address.tags["region"],
                street=address.tags["addr:street"]
                .replace("улица", "")
                .strip(),
                house_number=address.tags["addr:housenumber"],
                lat=address.tags["lat"],
                lon=address.tags["lon"],
            )
            full_address = (
                str(address)
                .replace("Decimal(", "")
                .replace(")", "")
                .replace('"', "")
                .replace("'", '"')
            )
            parsed_city_addresses.add(full_address)
    if len(parsed_city_addresses) == 0:
        print("Неверный город. Проверьте название")
        sys.exit(0)
    return parsed_city_addresses


def find_region_of_city(name):
    req = requests.get(
        "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%80%D0%BE%D0%B4%D0%BE%D0%B2_%D0%A0%D0%BE%D1%81%D1%81%D0%B8%D0%B8"
    )
    first_search = re.search(
        r'<table class="standard sortable"><tbody><tr>(.+?)</td></tr></tbody></table>',
        req.text,
        re.DOTALL,
    )
    try:
        second_search = re.search(
            rf'title="{name}(.+?)data-sort-value', first_search.group(1)
        )
        region = re.search(
            r'</td><td align="left">(.+?)</td><td align="left">',
            second_search.group(1),
        )
    except AttributeError:
        raise ValueError("Неверный город. Проверьте название")
    if "title" in region.group(1):
        return re.search(r'title="(.+?)"', region.group(1)).group(1).strip()
    else:
        return region.group(1).strip()


def check_to_add(address):
    keys = address.tags.keys()
    return (
        "addr:housenumber" in keys
        and "addr:street" in keys
        and "lat" in keys
        and "lon" in keys
    )
