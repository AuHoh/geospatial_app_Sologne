import folium
from folium.plugins import MarkerCluster
import geopandas as gpd
from streamlit_folium import folium_static
import streamlit as st

from utils.navigation import create_sidebar

# Titre de l'application
st.title("Sologne wildfires map since 2006")

create_sidebar()

# Lire les données depuis un fichier parquet
wildfire_sol = 'data/wildfire_sol.parquet'
gdf = gpd.read_parquet(wildfire_sol)
com_sologne = 'data/com_sologne.parquet'
commune = gpd.read_parquet(com_sologne)


# Obtenir les limites de la distribution
bbox = gdf.bounds.iloc[0]

# Coordonnées du centre des limites
center_latitude = (bbox['miny'] + bbox['maxy']) / 2
center_longitude = (bbox['minx'] + bbox['maxx']) / 2

# Créer une carte centrée sur les limites
m = folium.Map(location=[center_latitude, center_longitude], zoom_start=8)

popup = folium.GeoJsonPopup(fields=["NOM"], aliases=["Commune name"])


f_com = folium.GeoJson(
    data=commune,
    style_function=lambda feature: {
        "fillColor": "#ffff00",
        "color": "black",
        "weight": 2,
            },
    name= 'administrative boundaries',
    popup = popup, control=True,
    show=False)

f_com.add_to(m)

# Créer un cluster de marqueurs
marker_cluster = MarkerCluster(
    name="Incendies Sologne",
    spiderfyOnMaxZoom=True,
    showCoverageOnHover=False,
    zoomToBoundsOnClick=True,
).add_to(m)


# Ajout des marqueurs dans le cluster avec des popups uniques
def create_custom_marker(row):
    icon = folium.Icon(
        icon='fire',  # Utilisation de FontAwesome pour l'icône "fire"
        prefix='fa',  # FontAwesome prefix
        icon_color='orange',
        color='lightgray'
    )

    folium.Marker(
        location=[row.geometry.y, row.geometry.x],
        popup=f"Année: {row['Année']}<br>Date de première alerte: {row['Date de première alerte']}",
        icon=icon
    ).add_to(marker_cluster)


# Appliquer la fonction à chaque ligne du GeoDataFrame pour ajouter un marqueur avec icône personnalisée
gdf = gdf.apply(create_custom_marker, axis=1)

# Ajouter un LayerControl pour activer ou désactiver des groupes de marqueurs
folium.LayerControl().add_to(m)

# Afficher la carte avec .streamlit-folium
folium_static(m, width=900, height=700)

