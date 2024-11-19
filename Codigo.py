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
    
    # Cargar el archivo CSV
    uploaded_file = st.file_uploader("Elige un archivo CSV", type='csv')
    
    if uploaded_file is not None:
        # Leer el archivo CSV
        competitions_data = pd.read_csv(uploaded_file)

        # Mostrar las columnas disponibles
        st.write("Columnas disponibles en el archivo:", competitions_data.columns.tolist())

        # Cuadro de texto para buscar
        search_term = st.text_input("Buscar en el archivo:")

        if search_term:
            # Filtrar los datos según el término de búsqueda
            filtered_data = competitions_data[competitions_data.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]

            # Mostrar los resultados filtrados
            st.write('Resultados de la búsqueda:')
            st.dataframe(filtered_data)
        else:
            st.write("Introduce un término de búsqueda para ver los resultados.")

else:
    st.error("No se ha cargado ningún archivo CSV.")
