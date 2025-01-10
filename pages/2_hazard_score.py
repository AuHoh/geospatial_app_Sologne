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
com_score = 'data/com_score.parquet'
df_score = gpd.read_parquet(com_score)

# Get the bounds of your GeoDataFrame
bounds = df_score.total_bounds
# bounds returns [minx, miny, maxx, maxy]

# Convert to the format Folium expects: [[southWest], [northEast]]
folium_bounds = [[bounds[1], bounds[0]], [bounds[3], bounds[2]]]

def style_function(feature):
    hazard_score = feature['properties']['hazard_class']
    color_dict = {
        'Low': '#f1c40f',
        'Medium': '#f39c12',
        'High': 'red'
    }
    return {
        'fillColor': color_dict.get(hazard_score, 'gray'),  # 'gray' comme couleur par défaut
        'color': 'black',  # Couleur des bordures
        'weight': 1,       # Épaisseur des bordures
        'fillOpacity': 0.7 # Opacité du remplissage
    }

# Créer une carte centrée sur les limites
m = folium.Map(tiles="GeoportailFrance.orthos", zoom_start=8)

m.fit_bounds(folium_bounds)

# create popup
popup = folium.GeoJsonPopup(
    fields=["NOM", "hazard_class"],
    aliases=["Nom commune", "Classe d'aléa"],
    localize=True
)

f_com = folium.GeoJson(
    data=df_score,
    style_function=style_function,
    name="classe d'aléa",
    popup=popup,
    show=True,
    tooltip=folium.GeoJsonTooltip(
        fields=["NOM"],
        aliases=["Commune"],
        sticky=True
    )
)
f_com.add_to(m)
folium.LayerControl().add_to(m)

# Afficher la carte
folium_static(m, width=900, height=700)

# Créer une légende positionnée à droite de la carte
st.markdown("""
    <style>
    /* Créer un conteneur flex pour aligner la légende */
    .stMarkdown {
        display: inline-block;
        position: relative;
        top: -650px;  /* Remonter la légende */
        left: 920px;  /* Positionner à droite de la carte (900px + 20px de marge) */
    }
    </style>

    <div style='background-color: white; 
                padding: 10px; 
                border: 2px solid grey; 
                width: fit-content;'>
        <b>Classe d'aléa</b>
        <div style='display: flex; align-items: center; margin-top: 5px;'>
            <div style='background-color: red; width: 18px; height: 18px; margin-right: 8px;'></div>
            <span>Fort</span>
        </div>
        <div style='display: flex; align-items: center; margin-top: 5px;'>
            <div style='background-color: #f39c12; width: 18px; height: 18px; margin-right: 8px;'></div>
            <span>Moyen</span>
        </div>
        <div style='display: flex; align-items: center; margin-top: 5px;'>
            <div style='background-color: #f1c40f; width: 18px; height: 18px; margin-right: 8px;'></div>
            <span>Faible</span>
        </div>
    </div>
""", unsafe_allow_html=True)