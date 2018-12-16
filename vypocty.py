import json
from graphic_object import Point, Rectangle

def read_json_file(nazov_suboru): # načítanie vstupného súboru
    with open (nazov_suboru, encoding ="utf-8") as f:
        return json.load(f)

def default_cluster_id(features): # vytvorenie nového stĺpca v dátach
    for bod in features:
        bod["cluster_id"] = "0"
    return features

def calcbox(features):
    body_x = []
    body_y = []
    for x_y in features:
        props = x_y["geometry"]
        poloha = props["coordinates"]
        x = poloha[0] # x-ové súradnice všetkých bodov
        body_x.append(x)
        y = poloha[1] # y-ové súradnice všetkých bodov
        body_y.append(y)

    d = min(body_y) # dolny y bod
    h = max(body_y) # horny y bod
    l = min(body_x) # lavy x bod
    p = max(body_x) # pravy x bod

    ld = Point(l, d) # ľavý dolný bod
    ph = Point(p, h) # pravý horný bod
    return Rectangle(ld, ph)

def najdi_stred(obdlznik):
    ld = obdlznik.pts[0]
    ph = obdlznik.pts[2]
    stred_x = (ld.x + ph.x) / 2 # aritmetický priemer na zistenie stredovej súradnice x
    stred_y = (ld.y + ph.y) / 2 # aritmetický priemer na zistenie stredovej súradnice y
    stred = Point(stred_x, stred_y)
    return stred

def delenie(features, obdlznik):
    if len(features) > 50:
        S = najdi_stred(obdlznik)
        A = obdlznik.pts[0] # ľavý dolný bod základného bboxu
        C = obdlznik.pts[2] # pravý horný bod základného bboxu
        stred_AB = Point(S.x, A.y)
        stred_BC = Point(C.x, S.y) # body na stredoch línií bboxu, slúžiace na vytvorenie deliacich čiar (aby boli presne v strede)
        stred_CD = Point(S.x, C.y)
        stred_DA = Point(A.x, S.y)
        ld_obdlznik = Rectangle(A, S) # ľavý dolný obdĺžnik vzniknutý po delení základného
        pd_obdlznik = Rectangle(stred_AB, stred_BC) # pravý dolný obdĺžnik vzniknutý po delení základného
        ph_obdlznik = Rectangle(S, C) # pravý horný obdĺžnik vzniknutý po delení základného
        lh_obdlznik = Rectangle(stred_DA, stred_CD) # ľavý horný obdĺžnik vzniknutý po delení základného
        ld_body = zhluky(features,ld_obdlznik,"1")
        pd_body = zhluky(features,pd_obdlznik,"2") # priradenie bodov k obdĺžnikom a pridelenie cluster_id
        ph_body = zhluky(features, ph_obdlznik,"3")
        lh_body = zhluky(features, lh_obdlznik,"4")
        nove_ld_body = delenie(ld_body, ld_obdlznik)
        nove_pd_body = delenie(pd_body, pd_obdlznik) # vracia nové body podľa toho do akého obdĺžnika patria
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
        if x > A.x and x < C.x and y > A.y and y < C.y: # zistenie či bod patrí danému obdĺžniku
            bod["cluster_id"] = bod["cluster_id"] + cluster_id # priradenie ďalšej hodnoty cluster_id (ľavý dolný obdĺžnik má cluster_id "1" smerom doľava a nahor pokračuje a končí číslom "4" v ľavom hornom obdĺžniku)
            umiestnenie.append(bod)
    return umiestnenie

def output(features, nazov_suboru):
    with open(nazov_suboru, "w") as outfile:
        json.dump(features, outfile) # výstup programu
