import sys
import re
from utils.input_parser import address_parser


def run(input_data):
    address = address_parser(input_data)


if __name__ == '__main__':
    run(sys.argv[1:])
