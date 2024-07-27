from typing import List, Dict, Any


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

    @property
    def config(self) -> Dict[str, Any]:
        return self.__config

    @property
    def config_path(self):
        return self.__config_path
