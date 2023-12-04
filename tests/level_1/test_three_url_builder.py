import pytest
from functions.level_1.three_url_builder import build_url

@pytest.mark.parametrize("host_name, relative_url, get_params, expected", [
    pytest.param("https://example.com", "path/to/resource", {"param1": "value1", "param2": "value2"}, "https://example.com/path/to/resource?param1=value1&param2=value2", id="with_params"),
    pytest.param("https://example.com", "path/to/resource", None, "https://example.com/path/to/resource", id="without_params"),
    pytest.param("https://example.com", "", {"param": "value"}, "https://example.com/?param=value", id="empty_relative_url"),
    pytest.param("https://example.com", "path/to/resource", {"empty_param": ""}, "https://example.com/path/to/resource?empty_param=", id="empty_param_value")
])
def test_build_url(host_name, relative_url, get_params, expected):
    result = build_url(host_name, relative_url, get_params)
    assert result == expected
