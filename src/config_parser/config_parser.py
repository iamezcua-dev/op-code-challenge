import re
from typing import List, Dict, Any
from src.utils.utils import Utils


class ConfigParser:
    """
    A class for parsing configuration files.
    """

    def __init__(self, config_path: str):
        """
        Initializes the ConfigParser.

        :param config_path: The path to the configuration file.
        :type config_path: str
        """
        self.__config_path = config_path
        self.__config = {}

    def parse_configuration(self):
        with open(self.config_path, 'r') as config_file:
            lines = config_file.readlines()

        config_stack = [self.config]
        current_block = self.config

        for line in lines:
            # normalize lines
            line = Utils.normalize_line(line)
            # skip empty or comment lines
            if not line or re.match(r'^(#|/{2,})+', line):
                continue
            if line.endswith('{'):
                block_name = Utils.normalize_line(line[:-1])  # we get the block name
                new_config_block = {}
                current_block[block_name] = new_config_block
                config_stack.insert(0, current_block)
                current_block = new_config_block
            elif line.endswith('}'):
                current_block = config_stack.pop()

    @property
    def config(self) -> Dict[str, Any]:
        return self.__config

    @property
    def config_path(self):
        return self.__config_path
