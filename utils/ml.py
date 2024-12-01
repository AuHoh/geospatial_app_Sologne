import joblib


def get_model(name, path='model'):
    return joblib.load(f'{path}/{name}.joblib')


def mapping_feature_name(feature):
    mapping = {'Class_111': 'Artificial surfaces - Urban fabric - Continuous urban fabric',
               'Class_112': 'Artificial surfaces - Urban fabric - Discontinuous urban fabric',
               'Class_121': 'Artificial surfaces - Industrial, commercial and transport units - Industrial or commercial units',
               'Class_122': 'Artificial surfaces - Industrial, commercial and transport units - Road and rail networks and associated land',
               'Class_123': 'Artificial surfaces - Industrial, commercial and transport units - Port areas',
               'Class_124': 'Artificial surfaces - Industrial, commercial and transport units - Airports',
               'Class_131': 'Artificial surfaces - Mine, dump and construction sites - Mineral extraction sites',
               'Class_132': 'Artificial surfaces - Mine, dump and construction sites - Dump sites',
               'Class_133': 'Artificial surfaces - Mine, dump and construction sites - Construction sites',
               'Class_141': 'Artificial surfaces - Artificial, non-agricultural vegetated areas - Green urban areas',
               'Class_142': 'Artificial surfaces - Artificial, non-agricultural vegetated areas - Sport and leisure facilities',
               'Class_211': 'Agricultural areas - Arable land - Non-irrigated arable land',
               'Class_212': 'Agricultural areas - Arable land - Permanently irrigated land',
               'Class_213': 'Agricultural areas - Arable land - Rice fields',
               'Class_221': 'Agricultural areas - Permanent crops - Vineyards',
               'Class_222': 'Agricultural areas - Permanent crops - Fruit trees and berry plantations',
               'Class_223': 'Agricultural areas - Permanent crops - Olive groves',
               'Class_231': 'Agricultural areas - Pastures - Pastures',
               'Class_241': 'Agricultural areas - Heterogeneous agricultural areas - Annual crops associated with permanent crops',
               'Class_242': 'Agricultural areas - Heterogeneous agricultural areas - Complex cultivation patterns',
               'Class_243': 'Agricultural areas - Heterogeneous agricultural areas - Land principally occupied by agriculture, with significant areas of natural vegetation',
               'Class_244': 'Agricultural areas - Heterogeneous agricultural areas - Agro-forestry areas',
               'Class_311': 'Forest and semi natural areas - Forests - Broad-leaved forest',
               'Class_312': 'Forest and semi natural areas - Forests - Coniferous forest',
               'Class_313': 'Forest and semi natural areas - Forests - Mixed forest',
               'Class_321': 'Forest and semi natural areas - Scrub and/or herbaceous vegetation associations - Natural grasslands',
               'Class_322': 'Forest and semi natural areas - Scrub and/or herbaceous vegetation associations - Moors and heathland',
               'Class_323': 'Forest and semi natural areas - Scrub and/or herbaceous vegetation associations - Sclerophyllous vegetation',
               'Class_324': 'Forest and semi natural areas - Scrub and/or herbaceous vegetation associations - Transitional woodland-shrub',
               'Class_331': 'Forest and semi natural areas - Open spaces with little or no vegetation - Beaches, dunes, sands',
               'Class_332': 'Forest and semi natural areas - Open spaces with little or no vegetation - Bare rocks',
               'Class_333': 'Forest and semi natural areas - Open spaces with little or no vegetation - Sparsely vegetated areas',
               'Class_334': 'Forest and semi natural areas - Open spaces with little or no vegetation - Burnt areas',
               'Class_335': 'Forest and semi natural areas - Open spaces with little or no vegetation - Glaciers and perpetual snow',
               'Class_411': 'Wetlands - Inland wetlands - Inland marshes',
               'Class_412': 'Wetlands - Inland wetlands - Peat bogs',
               'Class_421': 'Wetlands - Maritime wetlands - Salt marshes',
               'Class_422': 'Wetlands - Maritime wetlands - Salines',
               'Class_423': 'Wetlands - Maritime wetlands - Intertidal flats',
               'Class_511': 'Water bodies - Inland waters - Water courses',
               'Class_512': 'Water bodies - Inland waters - Water bodies',
               'Class_521': 'Water bodies - Marine waters - Coastal lagoons',
               'Class_522': 'Water bodies - Marine waters - Estuaries',
               'Class_523': 'Water bodies - Marine waters - Sea and ocean'}

    if feature in mapping:
        return mapping[feature]

    return feature
