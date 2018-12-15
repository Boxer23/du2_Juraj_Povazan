import json
from graphic_object import Point, Rectangle

def read_json_file(nazov_suboru):
    with open (nazov_suboru, encoding ="utf-8") as f:
        return json.load(f)

def default_cluster_id(features):
    for bod in features:
        bod["cluster_id"] = "0"
    return features

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
        ld_body = zhluky(features,ld_obdlznik,"1")
        pd_body = zhluky(features,pd_obdlznik,"2")
        ph_body = zhluky(features, ph_obdlznik,"3")
        lh_body = zhluky(features, lh_obdlznik,"4")
        nove_ld_body = delenie(ld_body, ld_obdlznik)
        nove_pd_body = delenie(pd_body, pd_obdlznik)
        nove_ph_body = delenie(ph_body, ph_obdlznik)
        nove_lh_body = delenie(lh_body, lh_obdlznik)
        return nove_ld_body + nove_pd_body + nove_ph_body + nove_lh_body
    else:
        return features

def zhluky(features, obdlznik, cluster_id):
    umiestnenie = []
    for bod in features:
        props = bod["geometry"]
        poloha = props["coordinates"]
        x = poloha[0]
        y = poloha[1]
        A = obdlznik.pts[0]
        C = obdlznik.pts[2]
        if x > A.x and x < C.x and y > A.y and y < C.y:
            bod["cluster_id"] = bod["cluster_id"] + cluster_id
            umiestnenie.append(bod)
    return umiestnenie

def output(features, nazov_suboru):
    with open(nazov_suboru, "w") as outfile:
        json.dump(features, outfile)
