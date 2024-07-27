import pytest
from src.config_parser.config_parser import ConfigParser


class TestConfigParser:
    @pytest.fixture(scope="function")
    def config_parser(self):
        input_config_path: str = "../data/sample_configuration.txt"
        config = ConfigParser(config_path=input_config_path)
        yield config

    def test_config_parser_initialization_path(self, config_parser: ConfigParser):
        assert config_parser.config == {}

    def test_config_parser_load_config_path(self, config_parser: ConfigParser):
        assert config_parser.config_path == "../data/sample_configuration.txt"
