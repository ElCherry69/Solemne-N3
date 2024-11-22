import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
                
                
                Winners_data = result[result['Winners'].str.contains(team_name, case=False)]
                
                if not Winners_data.empty:
                  
                    Winners_data['Year'] = Winners_data['Season'].str.split('/').str[0].str.replace('–', '-').str.strip()
                    
                  
                    Winners_data['Year'] = pd.to_numeric(Winners_data['Year'], errors='coerce')
                    
                
                    Winners_data = Winners_data.dropna(subset=['Year'])
                    
                    plt.figure(figsize=(10, 5))
                    plt.plot(Winners_data['Year'], Winners_data['Score'], marker='o')
                    plt.title(f'Rendimiento de {team_name} en UCL Finals')
                    plt.xlabel('Año')
                    plt.ylabel('Goles')
                    plt.xticks(rotation=45)
                    plt.grid()
                    div = st.slider('Número de bins:', 0, 10, 2)
                    st.write('Bins =', div)
                
                    st.pyplot(plt)
                    plt.clf()
