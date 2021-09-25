from utils.input_parser import address_parser
from utils.arg_parser import init_parser


def run():
    args = init_parser()
    if args.address:
        address = address_parser(args.address)
    elif args.download:
        city_name = args.download


if __name__ == '__main__':
    run()
