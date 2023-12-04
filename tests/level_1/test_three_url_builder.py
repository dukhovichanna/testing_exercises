import pytest
from functions.level_1.three_url_builder import build_url

@pytest.mark.parametrize("host_name, relative_url, get_params, expected", [
    ("https://example.com", "path/to/resource", {"param1": "value1", "param2": "value2"}, "https://example.com/path/to/resource?param1=value1&param2=value2"),
    ("https://example.com", "path/to/resource", None, "https://example.com/path/to/resource"),
])
def test_build_url(host_name, relative_url, get_params, expected):
    result = build_url(host_name, relative_url, get_params)
    assert result == expected
