from src.config_parser.config_parser import ConfigParser
import pprint
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file_path", help="Configuration file to be parsed")
    args = parser.parse_args()
    c = ConfigParser(args.config_file_path)
    c.parse_configuration()
    pp = pprint.PrettyPrinter(depth=10)
    pp.pprint(c.config)
