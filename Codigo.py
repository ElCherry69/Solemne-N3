import streamlit as st
import pandas as pd
import os

# Título de la aplicación
st.title("FUSHIBALL")

# Cargar el archivo CSV con los datos de competiciones
file_path = 'competitions.csv'  # Cambia esto a la ruta correcta si es necesario

if os.path.exists(file_path):
    competitions_data = pd.read_csv(file_path)

    # Imprimir las columnas del DataFrame
    st.write("Columnas disponibles en el archivo:", competitions_data.columns.tolist())

    with st.sidebar:
        with st.expander("SOBRE QUÉ", expanded=False):
            st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre él. '
                       'Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y '
                       'países que levantaron la copa más preciada del mundo "La Copa del Mundo".'))
            
            div = st.slider('Número de bins:', 0, 10, 2)
            st.write('Bins =', div)
