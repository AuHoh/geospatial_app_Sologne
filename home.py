import streamlit as st
import folium
import geopandas as gpd
from streamlit_folium import folium_static

from utils.navigation import create_sidebar

st.set_page_config(
    page_title="Surveillance de la forêt de Sologne",
    page_icon="🌲",
)

create_sidebar()

st.title("Surveillance de la forêt de Sologne")

st.write(
    "La Sologne est une région naturelle française du Centre-Val de Loire qui s'étend sur une partie des départements du Loiret, du Loir-et-Cher et du Cher.")

st.markdown("""
   Sa superficie est d'environ 5 000 kilomètres carrés. Elle est bordée au nord par le fleuve de la Loire, au sud par la rivière du Cher et à l'est par les régions de Sancerre et du Berry.
   Ses habitants sont appelés les Solognots (masculin) et les Solognotes (féminin).

    """
            )

# Lire les données depuis un fichier parquet
dept_sologne = 'data/dept_sologne.parquet'
dept = gpd.read_parquet(dept_sologne)

# Créer une carte centrée sur la zone
m = folium.Map(location=[47.70012, 1.89975], zoom_start=6)

popup = folium.GeoJsonPopup(fields=["NOM"], aliases=["Department name"])

f_dept = folium.GeoJson(
    data=dept,
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "red",
        "weight": 2,
    },
    name='Limites administratives',
    popup=popup, control=True,
    show=True)

f_dept.add_to(m)

# Ajouter un LayerControl pour activer ou désactiver des layers
folium.LayerControl().add_to(m)

folium_static(m, width=900, height=700)
