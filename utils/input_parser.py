import re


def address_parser(input_data):
    #input_data = ' '.join(input_data)
    #print(input_data)
    pattern = ';|,|/'
    address = re.split(pattern, input_data)
    parsed_address = dict(
        region='',
        city='',
        street='',
        house='',
    )
    for address_element in address:
        if 'область' in address_element or 'обл.' in address_element and not parsed_address['region']:
            parsed_address['region'] = define_address_arg('область|обл.', address_element)
        elif 'город' in address_element or 'гор.' in address_element or 'г.' in address_element \
                and not parsed_address['city']:
            parsed_address['city'] = define_address_arg('город|гор.|г.', address_element)
        elif 'улица' in address_element or 'ул.' in address_element and not parsed_address['street']:
            parsed_address['street'] = define_address_arg('улица|ул.', address_element)
        elif 'дом' in address_element or 'д.' in address_element and not parsed_address['house']:
            parsed_address['house'] = define_address_arg('дом|д.', address_element)
    return parsed_address


def define_address_arg(pattern, address_element):
    parsed_el = re.split(pattern, address_element)
    for el in parsed_el:
        if len(el.strip()):
            return el.strip()


def check_input_data(input_data):
    pass