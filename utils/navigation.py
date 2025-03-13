import streamlit as st


def create_sidebar():
    with st.sidebar:
        st.page_link("home.py", label="Présentation", icon="🏠")
        st.page_link("pages/1_wildfires_data.py", label="Feux de forêt en Sologne", icon="1️⃣")
        st.page_link("pages/2_hazard_score.py", label="Aléa feux de forêt", icon="2️⃣")
        st.page_link("pages/3_wildfires_prediction.py", label="Modèle de prédiction", icon="3️⃣")

        # Sidebar content
        st.title("A propos de moi")
        st.markdown("""
        
        Je suis **Audrey Hohmann**, une consultante indépendante, spécialiste en intelligence artificielle et données géospatiales appliquées à des enjeux stratégiques et environnementaux. 
        

        Cette application de démonstration est conçue pour prédire une classe d'aléa feux de forêts en Sologne en utilisant des données et outils d'analyse spatiale pour produire des informations exploitables pour un modèle de prédiction.

        ### Caractéristiques principales de l'application :
        - Surveillance des feux de forêts
        - Analyse d'images satellites et SIG
        - Solutions de données géospatiales personnalisées

        N'hésitez pas à explorer les différentes fonctionnalités de l'application !
        
        Pour en savoir plus sur le contexte de ce travail et les conditions d'utilisation : \
        
        :octopus: [Repo du projet](https://github.com/AuHoh/geospatial_app_Sologne)

        Pour en savoir plus sur moi, visitez : \
        
        :globe_with_meridians: [mon site web pro](https://www.audreyhohmann.com) 
        
        """)
