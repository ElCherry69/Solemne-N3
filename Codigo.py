import streamlit as st

# Título de la aplicación
st.title("Aplicación de Fútbol")

# Crear un expander en la barra lateral
with st.sidebar:
    with st.expander("SOBRE QUÉ", expanded=False):
        st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre él. '
                   'Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y '
                   'países que levantaron la copa más preciada del mundo "La Copa del Mundo".'))
        
        # Slider para seleccionar el número de bins
        div = st.slider('Número de bins:', 0, 10, 2)
        st.write('Bins =', div)

# Aquí puedes agregar el contenido principal de tu aplicación
st.write("Contenido principal de la aplicación.")
