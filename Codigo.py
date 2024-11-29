import streamlit as st
import pandas as pd
import plotly.express as px  # Importar plotly.express

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

# Botón para mostrar enlace
if st.sidebar.button('El mejor jugador del mundo👑'):
    st.sidebar.markdown('[!!LIONEL ANDRES MESSI HERE¡¡](https://www.afa.com.ar/es/posts/premios-the-best-lionel-messi-el-mejor-jugador-del-mundo)')  # Cambia el enlace aquí

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

                    # Gráfico interactivo con Plotly
                    fig = px.line(Winners_data, x='Year', y='Score', title=f'Rendimiento de {team_name} en UCL Finals',
                                  labels={'Score': 'Goles', 'Year': 'Año'}, markers=True)
                    st.plotly_chart(fig)  # Mostrar el gráfico interactivo

    if st.sidebar.button('Mostrar Palmarés Histórico de la Champions League'):
        if not ucl_finals_data.empty:
            # Agrupar por 'Winners' y contar el número de títulos
            titles_summary = ucl_finals_data['Winners'].value_counts().reset_index()
            titles_summary.columns = ['Equipo', 'Total de Títulos']
            
            # # Mostrar la tabla de resumen
            st.subheader("Palmarés Histórico De La Champions League")
            st.dataframe(titles_summary)

st.subheader("Preguntas y Respuestas")

with st.expander("Haz clic para ver las preguntas", expanded=False):
    pregunta1 = st.radio("¿Cuál es el equipo con más títulos en la Champions League?", 
                          ("AC Milan", "Real Madrid", "Liverpool", "Barcelona"), key="pregunta1")

    if pregunta1:
        if pregunta1 == "Real Madrid":
            st.write("¡Correcto! Real Madrid tiene más títulos en la Champions League.")
        else:
            st.write("Incorrecto. La respuesta correcta es Real Madrid.")

    pregunta2 = st.radio("¿Quién ganó el Balón de Oro en 2021?", 
                          ("Karim Benzema", "Cristiano Ronaldo", "Robert Lewandowski", "Lionel Messi"), key="pregunta2")

    if pregunta2:
        if pregunta2 == "Lionel Messi":
            st.write("¡Correcto! Lionel Messi ganó el Balón de Oro en 2021.")
        else:
            st.write("Incorrecto. La respuesta correcta es Lionel Messi.")

    pregunta3 = st.radio("¿Cuál es la selección con más copas del mundo?", 
                          ("Brasil", "España", "Francia", "Alemania"), key="pregunta3")

    if pregunta3:
        if pregunta3 == "Brasil":
            st.write("¡Correcto! Brasil con un total de cinco Copas del Mundo, es la selección de fútbol con más Mundiales.")
        else:
            st.write("Incorrecto. La respuesta correcta es Brasil.")

    pregunta4 = st.radio("¿Quién es el máximo goleador de la historia del fútbol?", 
                          ("Armando Maradona", "Cristiano Ronaldo", "Eduardo Vargas", "Pelé"), key="pregunta4")

    if pregunta4:
        if pregunta4 == "Pelé":
            st.write("¡Correcto! Pelé es el único jugador con 1200 goles en la historia, convirtiéndolo en el goleador máximo de todos los tiempos.")
        else:
            st.write("Incorrecto. La respuesta correcta es Pelé.")

st.subheader("Galería de Imágenes")

# Definir una lista de imágenes y sus descripciones
imagenes = [
    {
        "url": "https://ovaciones.com/wp-content/uploads/2022/12/pele-campeonn.jpg",  # Reemplaza con la URL de tu imagen
        "descripcion": "Descripción de la imagen 1."
    },
    {
        "url": "https://example.com/image2.jpg",  # Reemplaza con la URL de tu imagen
        "descripcion": "Descripción de la imagen 2."
    },
    {
        "url": "https://example.com/image3.jpg",  # Reemplaza con la URL de tu imagen
        "descripcion": "Descripción de la imagen 3."
    },
    # Agrega más imágenes según sea necesario
]

# Mostrar las imágenes y sus descripciones
for img in imagenes:
    st.image(img["url"], caption=img["descripcion"], use_column_width=True)
    st.write("---")  # Línea divisoria entre imágenes

 
st.subheader("Hablemos de fútbol⚽")
comment = st.text_area("Deja tu comentario o pensamiento aquí:", height=80, key="comment")

if st.button("Enviar Comentario"):
    if comment:
        st.success("Comentario enviado con éxito!")
    else:
        st.warning("Por favor, escribe un comentario antes de enviar.")
