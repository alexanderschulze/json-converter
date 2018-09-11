import sys
import os
import json


def convert(data):
    # That's an example. Replace it with your custom json conversion
    data['score'] = 50
    if data['name'] == 'alex':
        data['score'] = 1000
    return data


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python converter.py <input-folder> <output-folder>")
        exit()

    # Get all input jsons
    input_dir, output_dir = sys.argv[1:]

    # Create output dir if it does not exist
    try:
        os.makedirs(output_dir)
    except OSError as e:
        # If directory cannot be created, and does not exist already
        if e.errno != 17:
            print(
                "Error - Output directory `%s` cannot be created" % output_dir
            )
            exit()

    try:
        json_files = os.listdir(input_dir)
    except OSError:
        print("Error - Input directory `%s` does not exist." % input_dir)
        exit()

    # Convert jsons
    for json_file in json_files:
        json_path = os.path.join(input_dir, json_file)
        data = None
        with open(json_path) as json_data:
            try:
                data = json.load(json_data)
            except ValueError:
                print(
                    "Error - File %s does not contain valid json." % json_path
                )
                exit()
        new_data = convert(data)

        new_json_path = os.path.join(output_dir, json_file)
        with open(new_json_path, "w+") as f:
            f.write(json.dumps(new_data, sort_keys=True, indent=4))
