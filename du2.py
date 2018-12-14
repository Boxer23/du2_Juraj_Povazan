import json
from graphic_object import Point, Rectangle

def read_json_file(nazov_suboru):
    with open (nazov_suboru, encoding ="utf-8") as f:
        return json.load(f)

def calcbox(features):
    body_x = []
    body_y = []
    for x_y in features:
        props = x_y["geometry"]
        poloha = props["coordinates"]
        x = poloha[0]
        body_x.append(x)
        y = poloha[1]
        body_y.append(y)

    d = min(body_y) # dolny y
    h = max(body_y) # horny y
    l = min(body_x) # lavy x
    p = max(body_x) # pravy x

    ld = Point(l, d)
    ph = Point(p, h)
    return Rectangle(ld, ph)

def najdi_stred(obdlznik):
    ld = obdlznik.pts[0]
    ph = obdlznik.pts[2]
    stred_x = (ld.x + ph.x) / 2
    stred_y = (ld.y + ph.y) / 2
    stred = Point(stred_x, stred_y)
    return stred

def delenie(features, obdlznik):
    if len(features) > 50:
        S = najdi_stred(obdlznik)
        A = obdlznik.pts[0]
        C = obdlznik.pts[2]
        stred_AB = Point(S.x, A.y)
        stred_BC = Point(C.x, S.y)
        stred_CD = Point(S.x, C.y)
        stred_DA = Point(A.x, S.y)
        ld_obdlznik = Rectangle(A, S)
        pd_obdlznik = Rectangle(stred_AB, stred_BC)
        ph_obdlznik = Rectangle(S, C)
        lh_obdlznik = Rectangle(stred_DA, stred_CD)
        #obdlznicky = [ld_obdlznik, pd_obdlznik, ph_obdlznik, lh_obdlznik]
        def Cluster_ID(features, ld_obdlznik, pd_obdlznik, ph_obdlznik, lh_obdlznik):
            if features == ld_obdlznik:
                for id in features:
                    id["Cluster_ID"] = "1"
            if features == pd_obdlznik:
                for id in features:
                    id["Cluster_ID"] = "2"
            if features == ph_obdlznik:
                for id in features:
                    id["Cluster_ID"] = "3"
            if features == lh_obdlznik:
                for id in features:
                    id["Cluster_ID"] = "4"
            return id
    else:
        exit()
    return features

output = delenie
