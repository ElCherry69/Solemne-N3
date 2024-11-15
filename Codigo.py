import streamlit as st

st.title("Mi Aplicación")

# Crear un expander para la sección "SOBRE QUÉ"
with st.expander("SOBRE QUÉ", expanded=False):
    st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre el. Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y países que levantaron la copa más preciada del mundo "La Copa del Mundo",'))
    
    st.subheader("Características Principales:")
    st.write("- Interactividad: Los usuarios pueden interactuar con los datos y visualizaciones.")
    st.write("- Visualizaciones: Gráficos y mapas que facilitan la comprensión de la información.")
    st.write("- Accesibilidad: Fácil de usar para usuarios técnicos y no técnicos.")

    st.subheader("Objetivo:")
    st.write("Nuestro objetivo es [explicar el objetivo principal].")
