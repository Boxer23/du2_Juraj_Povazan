import json

def read_json_file(nazov_suboru):
    with open (nazov_suboru, encoding ="utf-8") as f:
        return json.load(f)

def calcbox(features):

def suradnice(umiestnenie):
    body = []
    for x_y in umiestnenie:
        props = x_y["geometry"]
        poloha = props["coordinates"]
        body.append(poloha)
    return body

def extremy_x(body):
    l = min(body)
    p = max(body)
    print(l, p)
