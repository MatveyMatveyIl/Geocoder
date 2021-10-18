from utils.input_parser import address_parser
from utils.arg_parser import init_parser
from utils.download_osm_data import download_city_address


def run():
    args = init_parser()
    if args.address:
        address = address_parser(args.address)
    elif args.download:
        city_name = args.download
        full_city_addresses = download_city_address(city_name)


if __name__ == '__main__':
    run()
