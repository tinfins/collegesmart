import json


def json_list(json_file):
    """ Reads json file, returns list for Flask pages """
    json_open = []
    with open(json_file, 'r') as json_f:
        json_open = json.load(json_f)
        json_f.close()
    return json_open
