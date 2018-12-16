import vypocty

vstup = input("Zadajte nazov suboru + príponu geojson: ")
data = vypocty.read_json_file(vstup)
features = data["features"]

cluster_features = vypocty.default_cluster_id(features) #zavola funkciu default_cluster_id(features)

obdlznik = vypocty.calcbox(features)

new_features = vypocty.delenie(features, obdlznik)

nazov_suboru = "output.geojson"
vypocty.output(new_features, nazov_suboru)

