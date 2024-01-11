import json

"""Save transformed data to a JSON file."""
def transform(data, output):
    with open(output, 'w') as file:
        json.dump(data, file, indent=2)
