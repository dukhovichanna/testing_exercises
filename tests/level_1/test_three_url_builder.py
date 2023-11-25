from functions.level_1.three_url_builder import build_url


def test_build_url():
    host_name = "https://example.com"
    relative_url = "path/to/resource"
    get_params = {"param1": "value1", "param2": "value2"}
    assert build_url(host_name, relative_url, get_params) == "https://example.com/path/to/resource?param1=value1&param2=value2"

    host_name = "https://example.com"
    relative_url = "path/to/resource"
    assert build_url(host_name, relative_url) == "https://example.com/path/to/resource"
