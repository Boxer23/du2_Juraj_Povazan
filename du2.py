import json

def read_json_file(nazov_suboru):
    with open (nazov_suboru, encoding ="utf-8") as f:
        return json.load(f)

subor = input("Skopiruj nazov suboru: ")
budovy = read_json_file(subor)

features = budovy["features"]

def suradnice(features):
    for x_y in features:
        props = x_y["geometry"]
        suradnice = props["coordinates"]
        x = suradnice[0]
        y = suradnice[1]
        print(x, y)

poloha = suradnice(features)

