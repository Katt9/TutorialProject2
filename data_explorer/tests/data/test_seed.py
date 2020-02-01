from data_explorer.data.seed import load_schema, InvalidJSONError
import pytest


def test_load_schema():
    filename = './seed/schemas/test_schema.json'
    schema = load_schema(filename)

    assert schema.num_of_columns == 3
    assert len(schema.rules) == 3
    assert schema.rules[2]["name"] == "payr"


def test_load_schema_exception():
    filename = './seed/schemas/test_schema_bad.json'

    with pytest.raises(InvalidJSONError) as ex:
        schema = load_schema(filename)

    assert "Invalid JSON type in meta. Expected 'schema', got 'bad'" == str(ex.value)