import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Funcionamiento", page_icon="📈")
st.sidebar.header('Barra de navegación')




st.header('Funcionamiento')
st.markdown('El agua suspendida en el aire tiene un tamaño de gota extremadamente pequeño (1-40 µm), esto hace que el aire lo levante y quede flotando. Por un fenómeno conocido como condensación la malla atrapaniebla al chocar con un fuerte viento, neblina o nube, retendría las diminutas gotas de agua haciéndolas que se agrupen entre sí para formar una gota más grande. Esta gota grande tendría un peso mayor que por densidad le permitirá fluir a través de la malla y caer sobre un canal colector conectado a la parte baja de la misma para recibir el agua y mandarla a un contenedor.')
image = Image.open('img/Diagrama_malla.jpeg')
st.image(image=image)

st.header('Estrategia')
st.markdown('Las mallas atrapaniebla son un sistema de tejido plastificado elaborado a partir de polipropileno principalmente. Esta malla tiene la particular propiedad de retener el agua presente en el ambiente a partir de la humedad, niebla, nubes o fuertes vientos. El agua es retenida en forma de gotas muy diminutas que se irán fusionando entre sí para formar gotas mucho más grandes, que después se juntarán para formar un cúmulo de agua. En base a reportes este tipo de mallas pueden llegar a captar agua desde un 20$%$ de humedad relativa como valor mínimo y producir 24 L por m2 de malla.\n')

st.markdown('El principal objetivo es abastecer de suficiente área de esta malla en la zona montañosa que rodea a la Presa la Boca ubicada en Monterrey Nuevo León.')


st.header('Datos recolectados')
st.markdown('Las mallas atrapaniebla, considerrando la basta humedad ocn la que cuenta la zona de monterrey podemos hacer enfasis en la utilización de nuestro monitoreo siendo factible para la población')

image0 = Image.open('img/funcion.jpeg')
st.image(image=image0)


st.header('Monitoreo de datos')

st.markdown('Monitoreo de datos de caudal del agua, temperatura, humedad y calidad del aire en el ambiente, ')
image01 = Image.open('img/grafica1.jpeg')
st.image(image=image01)

image02= Image.open('img/grafica2.jpeg')
st.image(image=image02)

image03 = Image.open('img/grafica3.jpeg')
st.image(image=image03)



st.header('Normatividad')

st.markdown('El control de calidad será evaluada conforme a lo establecido en las siguientes normas:')
st.markdown('NOM-127-SSA1-2021. Agua para uso y consumo humano. Límites permisibles de la calidad del agua')
st.markdown('NOM-02-SSA1-1993. Requisitos sanitarios que deben cumplir los sistemas de abastecimiento de agua para uso y consumo humano públicos y privados.')
st.markdown('NOM-013-SSA1-1993, Requisitos sanitarios que debe cumplir la cisterna de un vehículo para el transporte y distribución de agua para uso y consumo humano.')
st.markdown('NOM-014-SSA1-1993, Procedimientos sanitarios para el muestreo de agua para uso y consumo humano en sistemas de abastecimiento de agua públicos y privados.')
st.markdown('NOM-179-SSA1-1998, Vigilancia y evaluación del control de calidad del agua para uso y consumo humano, distribuida por sistemas de abastecimiento público.')
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
