import streamlit as st
import pandas as pd

st.title("FUSHIBALL")

competitions_data = pd.read_csv('competitions.csv')

with st.sidebar:
    with st.expander("SOBRE QUÉ", expanded=False):
        st.write(('Esta aplicación se basa en la cultura del fútbol y un poco del conocimiento que se tiene hasta la fecha sobre él. '
                   'Hablándoles un poco sobre estadísticas de grandes equipos, jugadores que han logrado alzar el Balón de Oro y '
                   'países que levantaron la copa más preciada del mundo "La Copa del Mundo".'))
        
        div = st.slider('Número de bins:', 0, 10, 2)
        st.write('Bins =', div)
data = pd.read_csv('BallonDor-GoldenBall_Winners_v2.csv','FIFA - World Cup Summary.csv', 'UCL_AllTime_Performance_Table - UCL_Alltime_Performance_Table.csv', 'UCL_Finals_1955-2023 - UCL_Finals_1955-2023.csv')
