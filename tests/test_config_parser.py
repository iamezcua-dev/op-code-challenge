from typing import Tuple, Dict, Any

import pytest
from src.config_parser.config_parser import ConfigParser


class TestConfigParser:
    sample = "../data/sample_configuration.txt"
    sample2 = "../data/sample_configuration2.txt"
    sample3 = "../data/sample_configuration3.txt"

    well_formed_inputs = [sample, sample2, sample3]

    @pytest.mark.parametrize('input_path, expected_config', zip(well_formed_inputs, [{}, {}, {}]))
    def test_config_parser_config_initialization(self, input_path, expected_config: Dict[str, Any]):
        config_parser: ConfigParser = ConfigParser(config_path=input_path)
        actual_config = config_parser.config
        assert actual_config == expected_config

    @pytest.mark.parametrize('input_path, expected_path', zip(well_formed_inputs, [sample, sample2, sample3]))
    def test_config_parser_load_config_path(self, input_path: str, expected_path: str):
        config_parser: ConfigParser = ConfigParser(config_path=input_path)
        assert config_parser.config_path == input_path

    @pytest.mark.parametrize('input_path, expected', zip(
        well_formed_inputs,
        [True, True, False]
    ))
    def test_config_parser_data_structure_keys(self, input_path: str, expected: bool):
        config_parser: ConfigParser = ConfigParser(config_path=input_path)
        config_parser.parse_configuration()
        config_keyset = list(config_parser.config.keys())
        assert expected == ('runtime' in config_keyset)

    @pytest.mark.parametrize('input_path, expected', zip(
        [sample, sample2],
        [True, False]
    ))
    def test_config_parser_data_structure_keys(self, input_path: str, expected: bool):
        config_parser: ConfigParser = ConfigParser(config_path=input_path)
        config_parser.parse_configuration()
        config_keyset = list(config_parser.config['runtime'].keys())
        assert expected == ('system1' in config_keyset)

    @pytest.mark.parametrize('input_path, expected', zip(
        [sample],
        [True]
    ))
    def test_config_parser_data_structure_keys(self, input_path: str, expected: bool):
        config_parser: ConfigParser = ConfigParser(config_path=input_path)
        config_parser.parse_configuration()
        config_keyset = list(config_parser.config['runtime']['system1'].keys())
        assert expected == ('subsystem1' in config_keyset)
