import streamlit as st

from utils.navigation import create_sidebar


# Function to create a row with a label and numeric input
def display_label_and_input(label_text, key, value):
    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control label and input width
    with col1:
        st.write(label_text)
    with col2:
        return st.number_input("feature input", key=key, value=value, label_visibility="collapsed")


st.title("ML model for wildfire hazard index prediction")

create_sidebar()

st.markdown(
    """
    **This wildfire hazard index**  is designed to take into account both the frequency and intensity of wildfires in a commune, by comparing them with the regional average.

    ### features par commune
    informations sur les types de feature : 
    - Les classes d'occupation sont données en pourcentage de recouvrement de la surface de la commune.
    - Les informations sur les tronçons de route sont en mètres. 
    
""")

# Display three rows with labels and numeric inputs
value1 = display_label_and_input("Forêts de conifères :", "a", 0)
value2 = display_label_and_input("Route empiérrée :", "b", 0)
value3 = display_label_and_input("Forêt mixtes : ", "c", 0)

predict_button = st.button("Prédiction")
