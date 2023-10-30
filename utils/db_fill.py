import json

from utils.db_model import Address, session


def filling_db(full_city_addresses, city_name):
    for address in full_city_addresses:
        dict_address = json.loads(address)
        new_address = Address(
            region=dict_address["region"],
            city=city_name,
            street=dict_address["street"],
            house_number=dict_address["house_number"],
            latitude=dict_address["lat"],
            longitude=dict_address["lon"],
        )
        session.add(new_address)
    session.commit()
