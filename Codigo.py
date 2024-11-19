import streamlit as st

st.title("FUSHIBALL")

with st.sidebar:
    with st.expander("SOBRE QUÉ", expanded=False):
        st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre él. '
                   'Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y '
                   'países que levantaron la copa más preciada del mundo "La Copa del Mundo".'))
        
        
        div = st.slider('Número de bins:', 0, 10, 2)
        st.write('Bins =', div)
 if 'Tipo de Competición' in competitions_data.columns:
        competition_types = competitions_data['Tipo de Competición'].unique()  # Obtener tipos únicos de competición
        selected_competition = st.selectbox('Selecciona el tipo de competición:', competition_types)

        # Filtrar los datos según la competición seleccionada
        filtered_data = competitions_data[competitions_data['Tipo de Competición'] == selected_competition]

        # Mostrar los resultados filtrados
        st.write('Resultados para la competición seleccionada:')
        st.dataframe(filtered_data)
    else:
        st.error("La columna 'Tipo de Competición' no se encuentra en el archivo CSV.")
