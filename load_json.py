import json

with open ("adresnebody.geojson", encoding ="utf-8") as f:
    budovy = json.load(f)

features = budovy["features"]
suradnice = []
for x_y in features:
    props = x_y["geometry"]
    suradnice.append(props["coordinates"])

print(suradnice)

with open('data.txt', 'w') as outfile:
    json.dump(suradnice, outfile)