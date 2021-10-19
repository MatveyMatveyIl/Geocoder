from utils.db_model import session, Address


def searching_db(input_address: dict):
    query = (session.query(Address.country, Address.region, Address.city, Address.street, Address.house_number,
                       Address.latitude, Address.longitude).
         filter(Address.city == input_address['city'],
                Address.street == input_address['street'],
                Address.house_number == input_address['house']).first())
    if query is None:
        print("такого аддреса не существует")
    
