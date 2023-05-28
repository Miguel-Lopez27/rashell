import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Acerca de nostros", page_icon="📈")
st.sidebar.header('Barra de navegación')
st.title('Acerca de nosOtros')

image0 = Image.open('img/logo.jpeg')
st.image(image=image0)

st.header('¿Quienes somos?')
st.markdown('Somos jovenes zacatecanos que al ver en apuros a la poblacion regia, tomamos la iniciativa al buscar alternativas que solventen una solucion hacia su falta de agua, por que asi es el corazon zacatecano, cara de cantera y corazon de plata')

image1 = Image.open('img/nosotros.jpeg')
st.image(image=image1)


st.header('Objetivos')
st.markdown('Atraves de un sistema de recoleccion presentar una alternativa para el sustento de la presa, "La Boca ", empleando alternativas de materiales accesibles')

st.header('Contactos')
st.markdown('')


st.header('Ver más...')