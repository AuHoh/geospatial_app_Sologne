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
        
        Je suis **Audrey Hohmann**, une consultante indépendante, spécialiste en intelligence et données géospatiales appliquées à des enjeux stratégiques et environnementaux. 
        

        Cette application de démonstration est conçue pour prédire les feux de forêts en Sologne en utilisant des données d'observation de la Terre combinées à des outils d'analyse spatiale pour produire des informations exploitables.

        ### Caractéristiques principales de l'application :
        - Surveillance des feux de forêts
        - Analyse d'images satellites et SIG
        - Solutions de données géospatiales personnalisées

        N'hésitez pas à explorer les différentes fonctionnalités de l'application !

        Visitez mon site web : [Geospatial data scientist](https://www.audreyhohmann.com)
        

        """)
