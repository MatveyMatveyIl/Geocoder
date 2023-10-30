import sys

from utils.arg_parser import init_parser
from utils.db_fill import filling_db
from utils.db_model import Address, session
from utils.db_search import searching_db
from utils.download_osm_data import download_city_address
from utils.input_parser import address_parser


def run():
    args = init_parser()
    if args.address:
        address = address_parser(args.address)
        full_address = searching_db(address)
        print(full_address)
    elif args.download:
        city_name = args.download
        if (
            session.query(Address).filter(Address.city == city_name).count()
            != 0
        ):
            print(">>>Город уже скачан")
            sys.exit(0)
        print(">>>Скачивание города")
        full_city_addresses = download_city_address(city_name)
        filling_db(full_city_addresses, city_name)
        print(">>>Город скачан")


if __name__ == "__main__":
    run()
