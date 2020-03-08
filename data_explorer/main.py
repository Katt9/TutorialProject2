from data_explorer.db.io import validate_data, read_file

def main():
    filename = './seed/db/us_state_6digitnaics_2016.txt'
    schema = './seed/schemas/susb_2016_schema.json'
    census_data = read_file(filename)
    result = validate_data(census_data, schema)
    fakeline = 'blah'

if __name__ == "__main__":
    main()

