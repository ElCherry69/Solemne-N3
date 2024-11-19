import streamlit as st
import pandas as pd
import os

# Título de la aplicación
st.title("FUSHIBALL")

with st.sidebar:
    with st.expander("SOBRE QUÉ", expanded=False):
        st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre él. '
                   'Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y '
                   'países que levantaron la copa más preciada del mundo "La Copa del Mundo".'))
        
        div = st.slider('Número de bins:', 0, 10, 2)
        st.write('Bins =', div)

    # Sección para cargar y buscar en archivos CSV
    st.subheader("Buscar en archivos CSV")

    # Lista de archivos CSV
    csv_files = [
        'UCL_AllTime_Performance_Table.csv',
        'BallonDor-GoldenBall_Winners_v2.csv',
        'FIFA - World Cup Summary.csv',
        'UCL_Finals_1955-2023.csv'
    ]

    # Cargar todos los archivos CSV en un diccionario
    dataframes = {}
    for file in csv_files:
        if os.path.exists(file):
            dataframes[file] = pd.read_csv(file)
        else:
            st.warning(f"El archivo {file} no se encontró.")

    # Cuadro de texto para buscar
    search_term = st.text_input("Buscar en los archivos:")

    if search_term:
        # Crear un DataFrame vacío para almacenar los resultados
        results = pd.DataFrame()

        # Filtrar los datos de cada DataFrame
        for file, df in dataframes.items():
            filtered_data = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
            filtered_data['Source'] = file  # Añadir una columna para identificar de qué archivo proviene
            results = pd.concat([results, filtered_data], ignore_index=True)

        # Mostrar los resultados filtrados
        if not results.empty:
            st.write('Resultados de la búsqueda:')
            st.dataframe(results)
        else:
            st.write("No se encontraron resultados para el término de búsqueda.")

else:
    st.write("Introduce un término de búsqueda para ver los resultados.")
