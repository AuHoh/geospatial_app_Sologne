import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("Sologne forest monitoring")

st.sidebar.success("Select a demo above.")

st.markdown(  """
   Sologne is a natural region in Centre-Val de Loire, France, extending over portions of the departements of Loiret, Loir-et-Cher and Cher.
   Its area is about 5,000 square kilometres (1,900 sq mi). To its north is the river Loire, to its south the river Cher, while the districts of Sancerre and Berry are to its east.
   Its inhabitants are known as the Solognots (masculine) and Solognotes (feminine).

    """
              )

m = leafmap.Map(locate_control=True)
m.add_basemap("ROADMAP")
m.to_streamlit(height=700)