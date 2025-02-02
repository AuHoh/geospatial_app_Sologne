import folium
from folium.plugins import MarkerCluster
import geopandas as gpd
from streamlit_folium import folium_static
import streamlit as st

from utils.navigation import create_sidebar

# Titre de l'application
st.title("Carte d'aléa des feux de forêt par commune")

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
    aliases=["Nom commune", "Classes d'aléa"],
    localize=True
)

f_com = folium.GeoJson(
    data=df_score,
    style_function=style_function,
    name="classes d'aléa",
    popup=popup,
    show=True,
    tooltip=folium.GeoJsonTooltip(
        fields=["NOM"],
        aliases=["Nom de la commune :"],
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
    .legend-container {
        position: fixed;  
        top: 400px;      
        right: 20px;     
        z-index: 1000;   
    }

    .legend-box {
        background-color: white;
        padding: 12px;
        border: 2px solid grey;
        border-radius: 4px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        color: black; 
    }

    /* S'assurer que tous les textes dans la légende restent noirs */
    .legend-box b,
    .legend-box span,
    .legend-item span {
        color: black !important;  /* Use !important to override any theme settings */
    }

    .legend-item {
        display: flex;
        align-items: center;
        margin-top: 8px;
    }

    .color-box {
        width: 18px;
        height: 18px;
        margin-right: 8px;
        border: 1px solid rgba(0,0,0,0.1);
    }

    /* Style spécifique pour le mode sombre */
    @media (prefers-color-scheme: dark) {
        .legend-box {
            border-color: rgba(255,255,255,0.2);
        }
    }
    </style>

    <div class="legend-container">
        <div class="legend-box">
            <b>Classe d'aléa</b>
            <div class="legend-item">
                <div class="color-box" style="background-color: red;"></div>
                <span>Fort</span>
            </div>
            <div class="legend-item">
                <div class="color-box" style="background-color: #f39c12;"></div>
                <span>Moyen</span>
            </div>
            <div class="legend-item">
                <div class="color-box" style="background-color: #f1c40f;"></div>
                <span>Faible</span>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown(''':gray[Cette carte d'aléa présente les communes utilisées dans le jeu de données en entrée du modèle.\
        Certaines communes apparaissent en gris sur la carte, ce sont les communes exclues du jeu de données\
       lors du processus de nettoyage des données]''')