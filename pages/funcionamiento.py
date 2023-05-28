import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Funcionamiento", page_icon="📈")
st.sidebar.header('Barra de navegación')

st.header('Estrategia')
st.markdown('Las mallas atrapaniebla son un sistema de tejido plastificado elaborado a partir de polipropileno principalmente. Esta malla tiene la particular propiedad de retener el agua presente en el ambiente a partir de la humedad, niebla, nubes o fuertes vientos. El agua es retenida en forma de gotas muy diminutas que se irán fusionando entre sí para formar gotas mucho más grandes, que después se juntarán para formar un cúmulo de agua. En base a reportes este tipo de mallas pueden llegar a captar agua desde un 20$%$ de humedad relativa como valor mínimo y producir 24 L por m2 de malla.\n')

st.markdown('El principal objetivo es abastecer de suficiente área de esta malla en la zona montañosa que rodea a la Presa la Boca ubicada en Monterrey Nuevo León.')

col0, col0 = st.columns(2)
with col0:
    st.header('Datos recolectados')
    st.markdown('Las mallas atrapaniebla')
with col0:
    image0 = Image.open('img/recorrido_drone.jpeg')
    st.image(image=image0)



st.header('Funcionamiento')
st.markdown('El agua suspendida en el aire tiene un tamaño de gota extremadamente pequeño (1-40 µm), esto hace que el aire lo levante y quede flotando. Por un fenómeno conocido como condensación la malla atrapaniebla al chocar con un fuerte viento, neblina o nube, retendría las diminutas gotas de agua haciéndolas que se agrupen entre sí para formar una gota más grande. Esta gota grande tendría un peso mayor que por densidad le permitirá fluir a través de la malla y caer sobre un canal colector conectado a la parte baja de la misma para recibir el agua y mandarla a un contenedor.')
image = Image.open('img/Diagrama_malla.jpeg')
st.image(image=image)

st.header('Monitoreo de datos')

st.markdown('Monitoreo de datos de caudal del agua, temperatura, humedad y calidad del aire en el ambiente, ')

col01, col02 = st.columns(2)
with col01:
    st.header('Datos recolectados')
    st.markdown('La malla proove')
with col02:
    images = Image.open('img/malla.jpeg')
    st.image(image=images)

st.header('')
st.markdown('')
image1 = Image.open('img/rocio.jpeg')
st.image(image=image1)
    

st.header('Datos temperatura y humedad detectados por el drone')
st.markdown('Colección y envio de datos (Mostrados en la consola de una computadora)')

col3, col4 = st.columns(2)

with col3:
    image2 = Image.open('img/cumulo.jpeg')
    st.image(image=image2)
with col4:
    image02 = Image.open('img/mallas.jpeg')
    st.image(image=image02)

st.header('Control estadistico')
st.markdown('Grafiación de datos estadisticos detectados por los sensores')

chart_data = pd.DataFrame(
    np.random.randn(20, 2),
    columns=['Temperatura', 'Humedad'])

st.area_chart(chart_data)

st.header('Modelado 3D')
st.markdown('De acuerdo al recorrido del drone y recolección de imagenes, se creara un modelado 3D para la infromación general de la mina y la capacitación de mineros')
age3 = Image.open('img/rocio.jpeg')
st.image(image=age3)

col1, col2 = st.columns(2)

with col1:
    st.header('Nube de puntos')
    st.markdown('Se pleanea hacer un recorrido con una nube de puntos para tener un mejor reconocimiento de gritas y profunidad de la mina')

with col2:
    age4 = Image.open('img/funcion.jpeg')
    st.image(image=age4)