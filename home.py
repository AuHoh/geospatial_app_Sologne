import streamlit as st
import folium
import geopandas as gpd
from streamlit_folium import folium_static


st.set_page_config(
    page_title="Sologne forest monitoring",
    page_icon="🌲",
)



st.title("Sologne forest monitoring")

st.write("Sologne is a natural region in Centre-Val de Loire, France, extending over portions of the departements of Loiret, Loir-et-Cher and Cher.")

st.markdown("""
   Sologne is a natural region in Centre-Val de Loire, France, extending over portions of the departements of Loiret, Loir-et-Cher and Cher.
   Its area is about 5,000 square kilometres (1,900 sq mi). To its north is the river Loire, to its south the river Cher, while the districts of Sancerre and Berry are to its east.
   Its inhabitants are known as the Solognots (masculine) and Solognotes (feminine).

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
    name= 'administrative boundaries',
    popup = popup, control=True,
    show=True)

f_dept.add_to(m)


# Ajouter un LayerControl pour activer ou désactiver des layers
folium.LayerControl().add_to(m)


folium_static(m, width=900, height=700)

# Sidebar content
st.sidebar.title("About Me")
st.sidebar.markdown("""
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