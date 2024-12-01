import folium
from folium.plugins import MarkerCluster
import geopandas as gpd
from streamlit_folium import folium_static
import streamlit as st

from utils.navigation import create_sidebar

# Titre de l'application
st.title("Carte d'Aléa des feux de forêt par commune")

create_sidebar()

# Lire les données depuis un fichier parquet
wildfire_sol = 'data/df_feat_target.parquet'
gdf = gpd.read_parquet(wildfire_sol)
com_sologne = 'data/com_sologne.parquet'
df_commune = gpd.read_parquet(com_sologne)

# Obtenir les limites de la distribution
bbox = df_commune.bounds.iloc[0]

# Coordonnées du centre des limites
center_latitude = (bbox['miny'] + bbox['maxy']) / 2
center_longitude = (bbox['minx'] + bbox['maxx']) / 2

# Créer une carte centrée sur les limites
m = folium.Map(location=[center_latitude, center_longitude], tiles="GeoportailFrance.orthos", zoom_start=8)

popup = folium.GeoJsonPopup(fields=["NOM"], aliases=["Commune name"])

f_com = folium.GeoJson(
    data=df_commune,
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "gray",
        "weight": 2,
    },
    name='administrative boundaries',
    popup=popup, control=True,
    show=True)

f_com.add_to(m)

# Ajouter un contrôle de visibilité des couches
folium.LayerControl().add_to(m)

# Afficher la carte avec .streamlit-folium
folium_static(m, width=900, height=700)
