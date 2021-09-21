import re


def address_parser(input_data):
    input_data = ' '.join(input_data)
    pattern = ';|,|/'
    address = re.split(pattern, input_data)
    parsed_address = dict(
        region='',
        city='',
        areas='',
        street='',
        house='',
    )
    for el in address:
        if 'область' in el or 'обл.' in el:
            parsed_address['region'] = re.split('область|обл.', el)[1].strip()
        if 'город' in el or 'гор.' in el or 'г.' in el:
            parsed_address['city'] = re.split('город|гор.|г.', el)[1].strip()
        if 'район' in el:
            parsed_address['areas'] = re.split('район|р.', el)[1].strip()
        if 'улица' in el or 'ул.' in el:
            parsed_address['street'] = re.split('улица|ул.', el)[1].strip()
        if 'дом' in el or 'д.' in el:
            parsed_address['house'] = re.split('дом|д.', el)[1].strip()

    return parsed_address
