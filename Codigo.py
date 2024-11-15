import streamlit as st

st.title("FUSHIBOOL")
with st.sidebar:
     st.expander("SOBRE QUÉ")
     st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre el. Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y países que levantaron la copa más preciada del mundo "La Copa del Mundo",'))
     div = st.slider('Numero de bins:', 0, 10, 2)
     st.write('Bins=', div)
