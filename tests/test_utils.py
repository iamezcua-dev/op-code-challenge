import pytest

from utils.utils import Utils


class TestUtils:
    @pytest.mark.parametrize("input, expected", [
        ['RunTime              ', 'runtime'],
        ['       RUNTIME     ', 'runtime'],
        ['RuntimE', 'runtime'],
    ])
    def test_normalize_line(self, input, expected):
        actual = Utils.normalize_line(input)
        assert actual == expected
