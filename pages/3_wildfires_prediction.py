import streamlit as st
import pandas as pd
import numpy as np

from utils.ml import get_model, mapping_feature_name
from utils.navigation import create_sidebar


# Function to create a row with a label and numeric input
def display_label_and_input(label_text, key, value):
    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control label and input width
    with col1:
        st.write(label_text)
    with col2:
        return st.number_input("feature input", key=key, value=value, label_visibility="collapsed")


single_sample = {'Class_111': 0.0,
                 'Class_112': 0.0253287349719777,
                 'Class_121': 0.0,
                 'Class_122': 0.0,
                 'Class_124': 0.0,
                 'Class_131': 0.0,
                 'Class_132': 0.0,
                 'Class_141': 0.0,
                 'Class_142': 0.0,
                 'Class_211': 0.7479523653718727,
                 'Class_221': 0.0,
                 'Class_222': 0.0,
                 'Class_231': 0.0,
                 'Class_242': 0.0,
                 'Class_243': 0.032441790665534,
                 'Class_311': 0.1942771089906156,
                 'Class_312': 0.0,
                 'Class_313': 0.0,
                 'Class_322': 0.0,
                 'Class_324': 0.0,
                 'Class_331': 0.0,
                 'Class_411': 0.0,
                 'Class_511': 0.0,
                 'Class_512': 0.0,
                 'Altitude moyenne': 122.42744782297176,
                 'Pente moyenne': 0.5536060846991653,
                 'Angle moyen des pentes': 158.6160259787535,
                 "Population": 272,
                 'Nombre de logements occupés': 120.9113486857153,
                 'Densité population au km2': 13.2708175992398,
                 'Chemin': 15633.76402002429,
                 'Route empierrée': 1912.0777193954077,
                 'Route à 1 chaussée': 20792.086892970492,
                 'Route à 2 chaussées': 0.0,
                 'Sentier': 0.0,
                 'Autoroute': 4153.977807001664}

model = get_model('rf_clf')

st.title("Modèle de prédiction de la classe d'aléa feu de forêt d'une commune en fonction des valeurs fournies pour les facteurs de prédisposition")

create_sidebar()

st.markdown(
    """
    **Cette classe d'aléa feu de forêt** est conçu pour prendre en compte à la fois la fréquence et l'intensité des feux de forêt dans une commune, en les comparant à la moyenne régionale.

    ### Informations sur les facteurs de prédisposition pris en compte par commune
    - Les classes d'occupation sont données en pourcentage de recouvrement de la surface de la commune.
    - Les informations sur les tronçons de route sont en mètres. 
    
""")

# Display three rows with labels and numeric inputs
features = {}
for feature, default_value in single_sample.items():
    features[feature] = display_label_and_input(mapping_feature_name(feature), feature, default_value)

predict_button = st.button("Prédiction")

if predict_button:
    df_to_predict = pd.DataFrame([features])
    prediction = np.round(model.predict(df_to_predict)[0], 2)

    st.write("Score d'aléa prédit : " + str(prediction))
