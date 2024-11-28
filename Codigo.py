import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

st.title("FUSHIBALL")

def set_background_image(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url({image_url});
            background-size: cover;  /* Ajusta la imagen para cubrir todo el fondo */
            background-position: center;  /* Centra la imagen */
            background-repeat: no-repeat;  /* Evita que la imagen se repita */
            height: 100vh;  /* Altura del contenedor */
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background_image('https://wallpapers.com/images/hd/uefa-champions-league-intergalactic-stadium-2mxl696eobodolq3.jpg')

# Carga de datos
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
    search_title = st.sidebar.text_input("JUGADOR, EQUIPO o PAIS")

    # Selección de competiciones
    competition = st.sidebar.selectbox("Selecciona una competición:", ["Balón de Oro", "Copa del Mundo", "UCL All-Time", "UCL Finals"])

# Botón para mostrar enlace
if st.sidebar.button('Lionel Andres Messi HERE'):
    st.sidebar.markdown('[!!El mejor jugador de todos los tiempos¡¡](https://www.elcomercio.com/deportes/futbol/fifa-the-best-messi-mbappe.html)')

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
                    
                    st.pyplot(plt)
                    plt.clf()

# Caja de comentarios
st.subheader("Comentarios y Análisis")
comment = st.text_area("Deja tu comentario o análisis aquí:", height=150)

if st.button("Enviar Comentario"):
