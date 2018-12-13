import vypocty

data = vypocty.read_json_file("adresnebody.geojson")
features = data["features"]

obdlznik = vypocty.calcbox(features)

new_features = vypocty.delenie(features, obdlznik)

vypocty.output(new_features, nazov_suboru)