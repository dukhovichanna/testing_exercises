from functions.level_4.five_extra_fields import fetch_app_config_field, fetch_extra_fields_configuration

def test__fetch_extra_fields_configuration__return_dict_with_values_from_extra_fields_section(temp_config):
    result = fetch_extra_fields_configuration(temp_config)
    assert result == {"key1": "value1", "key2": 42}


def test__fetch_extra_fields_configuration__return_empty_dict_when_config_without_extra_fields(temp_config):
    temp_config_content = "[tool:app-config]\n" \
                          "other_field1 = 'value2'\n" \
                          "other_field2 = 3.14"

    with open(temp_config, "w") as f:
        f.write(temp_config_content)

    result = fetch_extra_fields_configuration(temp_config)
    assert result == {}


def test__fetch_extra_fields_configuration__return_empty_dict_when_config_is_empty(temp_config):
    with open(temp_config, "w") as f:
        f.write("[tool:app-config]\n")

    result = fetch_extra_fields_configuration(temp_config)
    assert result == {}


def test__fetch_extra_fields_configuration__return_empty_dict_when_config_is_missing():
    temp_config = "nonexistent_file.py"
    result = fetch_extra_fields_configuration(temp_config)
    assert result == {}


def test__fetch_app_config_field__return_value_when_exists(temp_config):
    result = fetch_app_config_field(temp_config, "other_field1")
    assert result == "'value2'"


def test__fetch_app_config_field__return_none_when_field_does_not_exist(temp_config):
    result = fetch_app_config_field(temp_config, "nonexistent_field")
    assert result is None


