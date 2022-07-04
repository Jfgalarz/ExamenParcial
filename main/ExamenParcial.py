import streamlit as st
from PIL import Image
icon = Image.open("Engineer_of_petroleum.jpg")
st.set_page_config(page_title="Ingeniería de Producción", page_icon=icon)
<style>
h1 {text-align: center;}
body {background-color: #DCE3D5;
      width: 1400px; margin: 15px auto;}
</style>
unsafe_allow_html=(True,)
st.title("Ingeniería de Producción :link:")
st.markdown("Programa, organiza, dirige, ejecuta y controla las actividades relacionadas "
            "con la producción del petróleo y gas para su almacenamiento, procesamiento, "
            "transporte, distribución y comercialización, aplicando los principios de gestión "
            "de la calidad ambiental hacia la mejora continua.")
expander_bar = st.expander("About")

image = Image.open("p.jpg")
st.image(image, width=100, use_column_width=True)

st.sidebar.title(":arrow_down_small: *Producción*")
uploaded_file = st.sidebar.file_uploader("Upload your csv file here")

st.sidebar.radio("pages", options=["Home", "Data", "Basic Calculations"])