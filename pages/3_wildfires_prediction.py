import streamlit as st
import pandas as pd
import numpy as np

from utils.ml import get_model, mapping_feature_name, get_hazard_color, get_text_color, validate_class_percentages
from utils.navigation import create_sidebar


# Function to create a row with a label and numeric input
def display_label_and_input(label_text, key, value):
    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control label and input width
    with col1:
        st.write(label_text)
    with col2:
        return st.number_input("feature input", key=key, value=float(value), label_visibility="collapsed",
                               min_value=0.0)


single_sample = {'Class_111': 0.0,
                 'Class_331': 0.0,
                 'Class_112': 0.0253287349719777,
                 'Class_211': 0.7479523653718727,
                 'Class_131': 0.0,
                 'Class_132': 0.0,
                 'Class_231': 0.0,
                 'Class_313': 0.0,
                 'Class_511': 0.0,
                 'Class_512': 0.0,
                 'Class_311': 0.1942771089906156,
                 'Class_312': 0.0,
                 'Class_411': 0.0,
                 'Class_141': 0.0,
                 'Class_122': 0.0,
                 'Class_221': 0.0,
                 'Class_243': 0.032441790665534,
                 'Class_222': 0.0,
                 'Class_142': 0.0,
                 'Class_121': 0.0,
                 'Class_242': 0.0,
                 'Class_324': 0.0,
                 'Class_124': 0.0,
                 'Class_322': 0.0,
                 'MNT': 122.42744782297176,
                 'slope': 0.5536060846991653,
                 'aspect': 158.6160259787535,
                 'P21_POP': 272,
                 'P21_OCCLOG': 120.9113486857153,
                 'P21_density': 13.2708175992398,
                 'Chemin': 15633.76402002429,
                 'Route empierrée': 1912.0777193954077,
                 'Route à 1 chaussée': 20792.086892970492,
                 'Route à 2 chaussées': 0.0,
                 'Sentier': 0.0,
                 'Type autoroutier': 4153.977807001664}

model = get_model('rf_clf')

st.title("Modèle de prédiction de la classe d'aléa feu de forêt d'une commune")

create_sidebar()

st.markdown(
    """
    **Cette classe d'aléa feu de forêt** est basée à la fois sur la fréquence et l'intensité des feux de forêt dans une commune, en les comparant à la moyenne régionale.

    ### Informations sur les facteurs de prédisposition pris en compte dans le modèle :
    - Les classes d'occupation du sol sont données en pourcentage de recouvrement de la surface de la commune (valeurs entre 0 et 1).
    - Les informations sur les tronçons de route sont fournies en mètres. 
    
""")

# Display three rows with labels and numeric inputs
features = {}
features_ordered = ['Class_111', 'Class_112', 'Class_121', 'Class_122', 'Class_124', 'Class_131', 'Class_132',
                    'Class_141', 'Class_142',
                    'Class_211', 'Class_221', 'Class_222', 'Class_231', 'Class_242', 'Class_243',
                    'Class_311', 'Class_312', 'Class_313', 'Class_322', 'Class_324', 'Class_331', 'Class_411',
                    'Class_511', 'Class_512',
                    'MNT', 'slope', 'aspect', 'P21_POP', 'P21_OCCLOG', 'P21_density', 'Chemin', 'Route empierrée',
                    'Route à 1 chaussée', 'Route à 2 chaussées', 'Sentier', 'Type autoroutier'
                    ]
for feature in features_ordered:
    features[feature] = display_label_and_input(mapping_feature_name(feature), feature, single_sample[feature])

st.markdown("""
    <style>
    .stButton {
        text-align: center;  
        margin-top: 20px;    
    }
    .stButton > button {
        font-size: 24px;
        font-weight: bold;
        padding: 15px 30px;
        border-radius: 5px;
        height: auto;
        width: 50%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.2s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

predict_button = st.button("Prédiction")

if predict_button:
    # Validation des pourcentages
    is_valid, total_percentage = validate_class_percentages(features)

    if not is_valid:
        st.error(
            f"La somme des pourcentages des classes d'occupation du sol dépasse 100% ({total_percentage:.4f}). Veuillez ajuster les valeurs svp.")
    else:
        df_to_predict = pd.DataFrame([features])
        prediction = np.round(model.predict(df_to_predict[list(single_sample.keys())])[0], 2)

        # Création du HTML
        score_html = f"""
            <div style='
                width: 100%;          
                text-align: center;  
                margin-top: 20px;
                margin-bottom: 20px;  
                font-size: 20px;
            '>
                <b>Score d'aléa prédit : </b>
                <span style='
                    background-color: {get_hazard_color(prediction)};
                    padding: 2px 6px;
                    border-radius: 3px;
                    color: {get_text_color(get_hazard_color(prediction))};
                    font-weight: bold;
                    display: inline-block;  /* Permet de mieux gérer le padding */
                    margin-top: 5px;        /* Petit espace entre le texte et le score */
                '>{prediction:.2f}</span>
            </div>
        """

        # Affichage dans Streamlit
        st.markdown(score_html, unsafe_allow_html=True)

st.markdown("""
    <style>
    .alert-box {
        font-size: 16px;
        margin: 20px 0;
        padding: 20px;
        border-radius: 8px;
        border: 2px solid #4a4a4a;  /* Bordure plus épaisse et plus visible */
    }

    /* Style pour mode clair */
    [data-theme="light"] .alert-box {
        background-color: #f8f9fa;
        color: black;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);  /* Ajout d'une ombre légère */
    }

    /* Style pour mode sombre */
    [data-theme="dark"] .alert-box {
        background-color: #262730;
        color: white;
        box-shadow: 0 2px 4px rgba(255,255,255,0.1);  /* Ombre adaptée au mode sombre */
    }

    /* Style pour le titre */
    .title-text {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 15px;
        border-bottom: 2px solid #4a4a4a;  /* Ligne de séparation sous le titre */
        padding-bottom: 8px;
        display: block;
    }

    /* Style pour les badges de niveau */
    .hazard-badge {
        padding: 2px 6px;
        border-radius: 3px;
        font-weight: bold;
        color: black !important;
    }
    </style>

    <div class='alert-box'>
        <span class='title-text'>Classification des niveaux d'aléa</span>
        Le score de prédiction est classé en trois niveaux d'aléa selon les seuils suivants :
        <ul style='list-style-type: none; padding-left: 20px; margin-top: 10px;'>
            <li style='margin-bottom: 8px;'>
                • Score ≤ 2.5 : Niveau d'aléa 
                <span class='hazard-badge' style='background-color: #f1c40f;'>
                    Faible
                </span>
            </li>
            <li style='margin-bottom: 8px;'>
                • Score entre 2.5 et 5 : Niveau d'aléa 
                <span class='hazard-badge' style='background-color: #f39c12;'>
                    Moyen
                </span>
            </li>
            <li style='margin-bottom: 8px;'>
                • Score > 5 : Niveau d'aléa 
                <span class='hazard-badge' style='background-color: red;'>
                    Fort
                </span>
            </li>
        </ul>
        <p style='margin-top: 15px;'>Ces seuils ont été définis pour caractériser l'intensité potentielle du phénomène.</p>
    </div>
""", unsafe_allow_html=True)
