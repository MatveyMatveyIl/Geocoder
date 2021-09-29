import overpy
from utils.handling_addresses import handling_addresses


def download_city_address(name):
    global res
    api = overpy.Overpass()
    query = (
        f'[out:json][timeout:100000];(area[name="{name}"]->.a;node(area.a)["addr:street"];way(area.a)["addr:street"];relation(area.a)["addr:street"];);out body; >; out skel qt;')
    # try:
    res = api.query(query)
    # except Exception:
    #     print('Ошибка сервера OSM. Запустите еще раз.')
    #     sys.exit(0)
    addresses = set()
    coordinates = dict()
    for address in res.nodes:
        if len(address.tags) != 0:
            address.tags['lat'] = address.lat
            address.tags['lon'] = address.lon
            addresses.add(address)
        else:
            coordinates[address.id] = [address.lat, address.lon]

    for cells in [res.ways, res.relations, res.areas]:
        for address in cells:
            if len(address.tags) != 0:
                addresses.add(address)
    print(len(addresses))
    print(len(coordinates))
    handling_addresses(addresses, coordinates)
