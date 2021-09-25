import overpy


def download_city_address(name):
    api = overpy.Overpass()
    query = (
        f'[out:json][timeout:10000];(area[name="{name}"]->.a;node(area.a)["addr:street"];way(area.a)["addr:street"];relation(area.a)["addr:street"];);out body; >; out skel qt;')
    res = api.query(query)
    address = set()
    for i in res.nodes:
        if len(i.tags) != 0:
            address.add(str(i.tags))

    for i in res.ways:
        if len(i.tags) != 0:
            address.add(str(i.tags))

    for i in res.relations:
        if len(i.tags) != 0:
            address.add(str(i.tags))

    for i in res.areas:
        if len(i.tags) != 0:
            address.add(str(i.tags))
