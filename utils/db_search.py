import json

from utils.db_model import Address, session


def searching_db(input_address: dict):
    query = (
        session.query(
            Address.country,
            Address.region,
            Address.city,
            Address.street,
            Address.house_number,
            Address.latitude,
            Address.longitude,
        )
        .filter(
            Address.city == input_address["city"],
            Address.street == input_address["street"],
            Address.house_number == input_address["house"],
        )
        .first()
    )
    if query is None:
        print("такого адреса не существует")
    else:
        return convert_to_json(query)


def convert_to_json(query):
    full_address = {
        "Страна": query[0],
        "Область": query[1],
        "Город": query[2],
        "Улица": query[3],
        "Дом": query[4],
        "Широта": query[5],
        "Долгота": query[6],
    }
    return json.dumps(full_address, ensure_ascii=False)
