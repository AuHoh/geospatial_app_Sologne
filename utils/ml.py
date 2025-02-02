import joblib


def get_model(name, path='model'):
    return joblib.load(f'{path}/{name}.joblib')


def mapping_feature_name(feature):
    mapping = {'Class_111': 'Territoires artificialisés - Tissu urbain continu',
               'Class_112': 'Territoires artificialisés - Tissu urbain discontinu',
               'Class_121': 'Territoires artificialisés - Zones industrielles ou commerciales',
               'Class_122': 'Territoires artificialisés - Réseaux routiers et ferroviaires et espaces associés',
               'Class_123': 'Territoires artificialisés - Zones portuaires',
               'Class_124': 'Territoires artificialisés - Aéroports',
               'Class_131': "Territoires artificialisés - Extraction de matériaux",
               'Class_132': 'Territoires artificialisés - Décharges',
               'Class_133': 'Territoires artificialisés - Chantiers',
               'Class_141': 'Territoires artificialisés - Espaces verts urbains',
               'Class_142': 'Territoires artificialisés - Équipements sportifs et de loisirs',
               'Class_211': 'Territoires agricoles - Terres arables hors périmètres d’irrigation',
               'Class_212': 'Territoires agricoles - Périmètres irrigués en permanence',
               'Class_213': 'Territoires agricoles - Rizières',
               'Class_221': 'Territoires agricoles - Vignobles',
               'Class_222': 'Territoires agricoles - Vergers et petits fruits',
               'Class_223': 'Territoires agricoles - Oliveraies',
               'Class_231': 'Territoires agricoles - Prairies',
               'Class_241': 'Territoires agricoles - Cultures annuelles associées aux cultures permanentes',
               'Class_242': 'Territoires agricoles - Systèmes culturaux et parcellaires complexes',
               'Class_243': 'Territoires agricoles - Surfaces essentiellement agricoles, interrompues par des espaces naturels importants',
               'Class_244': 'Territoires agricoles - Territoires agro-forestiers',
               'Class_311': 'Forêts et milieux semi-naturels - Forêts de feuillus',
               'Class_312': 'Forêts et milieux semi-naturels - Forêts de conifères',
               'Class_313': 'Forêts et milieux semi-naturels - Forêts mélangées',
               'Class_321': 'Forêts et milieux semi-naturels - Pelouses et pâturages naturels',
               'Class_322': 'Forêts et milieux semi-naturels - Landes et broussailles',
               'Class_323': 'Forêts et milieux semi-naturels - Végétation sclérophylle',
               'Class_324': 'Forêts et milieux semi-naturels - Forêt et végétation arbustive en mutation',
               'Class_331': 'Forêts et milieux semi-naturels - Plages, dunes et sable',
               'Class_332': 'Forêts et milieux semi-naturels - Roches nues',
               'Class_333': 'Forêts et milieux semi-naturels - Végétation clairsemée',
               'Class_334': 'Forêts et milieux semi-naturels - Zones incendiées',
               'Class_335': 'Forêts et milieux semi-naturels - Glaciers et neiges éternelles',
               'Class_411': 'Zones humides - Marais intérieurs',
               'Class_412': 'Zones humides - Tourbières',
               'Class_421': 'Zones humides - Marais maritimes',
               'Class_422': 'Zones humides - Marais salants',
               'Class_423': 'Zones humides - Zones intertidales',
               'Class_511': 'Surfaces en eau - Cours et voies d’eau',
               'Class_512': 'Surfaces en eau - Plans d’eau',
               'Class_521': 'Surfaces en eau - Lagunes littorales',
               'Class_522': 'Surfaces en eau - Estuaires',
               'Class_523': 'Surfaces en eau - Mers et océans',
               'MNT': 'Altitude moyenne',
               'slope': 'Pente moyenne (°)',
               'aspect': 'Angle moyen des pentes (°)',
               'P21_POP': 'Population',
               'P21_OCCLOG': 'Nombre de logements occupés',
               'P21_density': 'Densité population au km2',
               'Type autoroutier': 'Autoroute'}

    if feature in mapping:
        return mapping[feature]

    return feature


def validate_class_percentages(features):
    class_sum = sum(value for key, value in features.items() if key.startswith('Class_'))
    return class_sum <= 1, class_sum


low_threshold = 2.5
medium_threshold = 5


def get_hazard_color(prediction):
    if prediction <= low_threshold:
        return "#f1c40f"  # Jaune (Faible)
    elif prediction <= medium_threshold:
        return "#f39c12"  # Orange (Moyen)
    else:
        return "red"  # Rouge (Fort)


# Fonction pour déterminer la couleur du texte en fonction du fond
def get_text_color(background_color):
    if background_color == "#f1c40f":
        return "black"
    return "white"
