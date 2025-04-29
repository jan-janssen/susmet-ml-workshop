import json

def strip_values(json_file_path, output_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Function to strip values recursively
    def strip_dict(d):
        if isinstance(d, dict):
            return {k: strip_dict(v) for k, v in d.items()}
        elif isinstance(d, list):
            return [strip_dict(item) for item in d]
        else:
            return None

    schema = strip_dict(data)

    # Write the schema to a new JSON file
    with open(output_file_path, 'w') as file:
        json.dump(schema, file, indent=4)

# Example usage
strip_values('schema_filled.json', 'schema_blank.json')

# import json

# def strip_values(json_file_path, output_file_path):
#     # Read the JSON file
#     with open(json_file_path, 'r') as file:
#         data = json.load(file)

#     # Strip all values
#     def strip_dict(d):
#         return {k: None if isinstance(v, (dict, list)) else type(v).__name__ for k, v in d.items()}

#     schema = strip_dict(data)

#     # Write the schema to a new JSON file
#     with open(output_file_path, 'w') as file:
#         json.dump(schema, file, indent=4)

# # Example usage
# strip_values('schema_filled.json', 'schema_blank.json')
#
