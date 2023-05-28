import streamlit as st
import pandas as pd
import numpy as np
import firestoreCrud as fsCRUD
import pip

pip.main(["install","openpyxl"])
# LLamado de datos para firebase

#docs = fsCRUD.getDocument()
docs = pd.read_excel('Hack.xlsx')

st.sidebar.header('Barra de navegación')

st.title('Estrategia para el monitoreo del reabastecimiento de agua en presa "La Boca" Monterrey')

st.header('Rehidratando Monterrey')
st.markdown('El escases y falta de la calidad del agua para consumo humano, agrícola, indutrial, etc, ha llegado a ser una de las problemáticas más grandes a nivel mundial, y con muy pocas estrategias costeables para resolverlo agrava su problemática. La humedad relativa que se define como la cantidad de agua contenida en el aire, se ha estado considerando como una muy prometedora y costeable fuente de obtención de agua, y con el respaldo de varios estudios se ha demostrado que puede ser costeable para resolver esta problemática en zonas afectadas.\n')

st.markdown('Monterrey ocupa el segundo lugar de la ciudad más grande de México y demuestra ser además una de las más industrializadas. Sin embargo en el año 2022 enfrentó un problema extremo debido a una falta de abastecimiento de agua por la sequía de una de las principales presas, “La Boca” que da sustento no solo a una ciudad grande como Monterrey sino también a Santiago. Una de las causas fue una demanda excesiva del servicio hídrico, llevando a la suspensión total del mismo.')


#st.header('Rehidratando Monterrey')
#st.markdown('La cantidad de agua dispersa o contenida en el aire, lo que se expresa como humedad relativa, ha sido considerada y estudiada como una fuente prometedora para la obtención de agua, con el objetivo de reabastecer o hacer llegar agua a zonas que no tienen acceso a ella. Siendo así una estrategia para resolver dicho problema.')

st.write(docs)
#Seleccionar una linea de tuberia

col1, col2 = st.columns(2)

with col1:
   st.header("Historial y sensores")
   #option = st.selectbox('Selecciona un sector: ', [e.to_dict()["nom_mina"] for e in docs])
   #st.dataframe([e.to_dict() for e in docs], use_container_width=True)

with col2:
   st.header("Historial de temperatura y humedad")
   #chart_data = pd.DataFrame(np.random.randn(20, 2),columns=['Temperatura', 'humedad',])
   #st.line_chart(chart_data)

st.header('')

