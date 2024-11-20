import streamlit as st
import pandas as pd
import matplotlib as plt

st.title("FUSHIBALL")

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

def search_data(query):
    results = {
        "Balón de Oro": ballon_dor_data[ballon_dor_data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)],
        "Copa del Mundo": world_cup_data[world_cup_data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)],
        "UCL All-Time": ucl_data[ucl_data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)],
        "UCL Finals": ucl_finals_data[ucl_finals_data.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)],
    }
    return results

if search_title:
    results = search_data(search_title)
    for title, result in results.items():
        if not result.empty:
            st.subheader(title)
            st.dataframe(result)


            if title == "UCL Finals":
                team_name = search_title
            
                team_data = result[result['Team'].str.contains(team_name, case=False)]
                
                if not team_data.empty:
                  
                    team_data['Season'] = pd.to_datetime(team_data['Season'], format='%Y').dt.Season
                    plt.figure(figsize=(10, 5))
                    plt.plot(team_data['Season'], team_data['Score'], marker='o')
                    plt.title(f'Rendimiento de {team_name} en UCL Finals')
                    plt.xlabel('Año')
                    plt.ylabel('Goles')
                    plt.xticks(rotation=45)
                    plt.grid()
                    st.pyplot(plt)
