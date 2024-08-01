import re
from typing import List, Dict, Any
from src.utils.utils import Utils
from src.exceptions.exceptions import MalformedConfigFileError


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
        """
        Parse the configuration file provided and store its contents in a dictionary, for querying values as needed.
        """
        with open(self.config_path, 'r') as config_file:
            lines = config_file.readlines()

        config_stack: List[Dict[str, Any]] = [self.config]
        current_block = self.config
        open_braces = 0

        for line in lines:
            # normalize lines
            line = Utils.normalize_line(line)
            # skip empty or comment lines
            if not line or re.match(r'^(#|/{2,})+', line):
                continue
            # when we find an opening curly brace, this means a new block of configuration should start
            if line.endswith('{'):
                block_name = Utils.normalize_line(line[:-1])  # we get the block name
                new_config_block = {}
                current_block[block_name] = new_config_block
                config_stack.append(current_block)
                current_block = new_config_block
                open_braces += 1
            # when closing curly brace is found, we should close the configuration
            elif line.endswith('}'):
                current_block = config_stack.pop()
                open_braces -= 1
            else:
                key, *values = re.split(r'\s+', line)
                # - The associated value for the key would be of type:
                #   - None, if the associated string is empty.
                #   - str, if the length of the associated string is 1.
                #   - List[str], if multiple elements were identified.
                value = None if not values else values[0] if len(values) == 1 else values
                current_block[key] = value

        if open_braces != 0:
            raise MalformedConfigFileError()

    @property
    def config(self) -> Dict[str, Any]:
        return self.__config

    @property
    def config_path(self):
        return self.__config_path

    def get_element(self, the_key: str) -> List[Any] | str | bool | None:
        """
        Retrieves the element from the given configuration dictionary with the specified key.

        Args:
            self: The current instance of the class.
            the_key (str): The key to search for in the configuration dictionary.

        Returns:
            List[Any] | str | bool | None: The element associated with the key, if found. Returns None if the key is not present or the element is not found in the nested dictionaries.

        """

        def helper(remaining: Dict[str, Any]) -> List[Any] | str | bool | None:
            if the_key in remaining:
                return remaining[the_key]

            for value in remaining.values():
                if isinstance(value, Dict) and len(value) > 0:
                    return helper(value)

        return helper(self.config)
