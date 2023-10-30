import argparse


def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-address",
        "-a",
        dest="address",
        type=str,
        nargs="?",
        action="store",
        required=False,
        help="Адрес в формате: ."
        '"область=обл."_'
        '"город=гор.=г."_'
        '"улица=ул."_'
        '"дом=д."_'
        '"разделители: ; , /"',
    )
    parser.add_argument(
        "-d",
        "-download",
        dest="download",
        type=str,
        action="store",
        required=False,
        help="",
    )
    args = parser.parse_args()
    return args
