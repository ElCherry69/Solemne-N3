import streamlit as st

st.title("Mi Aplicación")

# Crear un expander para la sección "SOBRE QUÉ"
with st.expander("SOBRE QUÉ", expanded=False):
    st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre el. Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y países que levantaron la copa más preciada del mundo "La Copa del Mundo",'))
