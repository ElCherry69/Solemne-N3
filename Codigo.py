import streamlit as st
import pandas as pd

st.title("FUSHIBALL")

competitions_data = pd.read_csv('competitions.csv')
ballon_dor_data = pd.read_csv('BallonDor-GoldenBall_Winners_v2.csv')
world_cup_data = pd.read_csv('FIFA - World Cup Summary.csv')
ucl_data = pd.read_csv('UCL_AllTime_Performance_Table - UCL_Alltime_Performance_Table.csv')
ucl_finals_data = pd.read_csv('UCL_Finals_1955-2023 - UCL_Finals_1955-2023.csv')

with st.sidebar:
    with st.expander("SOBRE QUÉ", expanded=False):
        st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre él. '
                   'Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y '
                   'países que levantaron la copa más preciada del mundo "La Copa del Mundo".'))
        
        div = st.slider('Número de bins:', 0, 10, 2)
        st.write('Bins =', div)

    st.sidebar.header("Opciones de Filtro")
    search_title = st.sidebar.text_input("Jugador, País o Competición")

if search_title:
    filtered_competitions = competitions_data[competitions_data['column_name'].str.contains(search_title, case=False)]
    st.write(filtered_competitions)
