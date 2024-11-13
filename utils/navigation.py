import streamlit as st


def create_sidebar():
    with st.sidebar:
        st.page_link("home.py", label="Présentation", icon="🏠")
        st.page_link("pages/1_wildfires_data.py", label="Feux de forêt en Sologne", icon="1️⃣")
        st.page_link("pages/2_hazard_score.py", label="Aléa feux de forêt", icon="2️⃣")
        st.page_link("pages/3_wildfires_prediction.py", label="Modèle de prédiction", icon="3️⃣")

        # Sidebar content
        st.title("About Me")
        st.markdown("""
        **Name**: Audrey Hohmann

        I am a freelance Geospatial Data Scientist specializing in GIS, Remote Sensing, and developing custom geospatial solutions.

        This demo app is designed to monitor Sologne forests in France by using Earth Observation data combined with spatial analysis tools to produce actionable insights.

        ### Key Features of the App:
        - Forest monitoring
        - Satellite and drone imagery analysis
        - Custom geospatial data solutions

        Feel free to explore the various features of the app!

        Visit my website: [Geospatial data scientist](https://www.audreyhohmann.com)

        """)
