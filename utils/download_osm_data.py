import overpy
import sys
import requests


def download_city_address(name):
    api = overpy.Overpass()
    query = (
        f'[out:json][timeout:10000];(area[name="{name}"]->.a;node(area.a)["addr:street"];way(area.a)["addr:street"];relation(area.a)["addr:street"];);out body; >; out skel qt;')
    try:
        osm_json = api.query(query)
    except overpy.exception.OverpassTooManyRequests:
        print('Ошибка сервера OSM. Запустите еще раз.')
        sys.exit(0)
    except overpy.exception.OverpassGatewayTimeout:
        print('Ошибка сервера OSM. Запустите еще раз.')
        sys.exit(0)
    finally:
        requests.get(r'http://overpass-api.de/api/kill_my_queries')
    addresses = set()
    for address in osm_json.nodes:
        if len(address.tags) != 0:
            address.tags['lat'] = address.lat
            address.tags['lon'] = address.lon
            addresses.add(address)

    for cells in [osm_json.ways, osm_json.relations, osm_json.areas]:
        for address in cells:
            if len(address.tags) != 0:
                addresses.add(address)
    full_city_addresses = handling_addresses(addresses)


def handling_addresses(addresses: set):
    for address in addresses:
        try:
            if address.nodes:
                address.tags['lat'] = address.nodes[0].lat
                address.tags['lon'] = address.nodes[0].lon
        except AttributeError:
            continue
    parsed_city_addresses = set()
    for address in addresses:
        parsed_city_addresses.add(str(address.tags))
    return parsed_city_addresses
