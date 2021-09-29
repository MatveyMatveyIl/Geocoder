

def handling_addresses(addresses: set, coordinates: dict):
    for address in addresses:
        if address.nodes:
            for node in address.nodes:
                if node in coordinates.keys():
                    address.tags['lat'] = coordinates[node][0]
                    address.tags['lon'] = coordinates[node][1]
    parsed_city_addresses = set()
    for address in addresses:
        parsed_city_addresses.add(str(address.tags))

    print(parsed_city_addresses)