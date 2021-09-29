import overpy


def download_city_address(name):
    api = overpy.Overpass()
    query = (
        f'[out:json][timeout:10000];(area[name="{name}"]->.a;node(area.a)["addr:street"];way(area.a)["addr:street"];relation(area.a)["addr:street"];);out body; >; out skel qt;')
    try:
        res = api.query(query)
    except overpy.exception as e:
        raise e('Ошибка сервера OSM. Запустите еще раз.')
    addresses = set()
    for address in res.nodes:
        if len(address.tags) != 0:
            address.tags['lat'] = address.lat
            address.tags['lon'] = address.lon
            addresses.add(str(address.tags))

    for cells in [res.ways, res.relations, res.areas]:
        for address in cells:
            if len(address.tags) != 0:
                addresses.add(str(address.tags))
