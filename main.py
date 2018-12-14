import vypocty
import json

data = vypocty.read_json_file("adresnebody.geojson")
features = data["features"]

obdlznik = vypocty.calcbox(features)
print(obdlznik)

new_features = vypocty.delenie(features, obdlznik)
print(new_features)

vypocet = vypocty.output(new_features, obdlznik)

with open('data.txt', 'w') as outfile:
    json.dump(vypocet, outfile)
