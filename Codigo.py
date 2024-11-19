import streamlit as st

# Título de la aplicación
st.title("Buscador Simple")

# Descripción de la aplicación
st.write("Introduce un término de búsqueda para encontrar información.")

# Cuadro de texto para buscar
search_term = st.text_input("¿Qué estás buscando?")

# Simulación de datos (puedes reemplazar esto con tus propios datos)
data =[
    'UCL_AllTime_Performance_Table.csv',
    'BallonDor-GoldenBall_Winners_v2.csv',
    'FIFA - World Cup Summary.csv',
    'UCL_Finals_1955-2023.csv'
]

# Función para buscar en los datos
def search_data(term):
    results = {}
    for category, items in data.items():
        filtered_items = [item for item in items if term.lower() in item.lower()]
        if filtered_items:
            results[category] = filtered_items
    return results

# Realizar la búsqueda si hay un término
if search_term:
    results = search_data(search_term)

    # Mostrar los resultados
    if results:
        st.write("Resultados de la búsqueda:")
        for category, items in results.items():
            st.write(f"**{category}:** {', '.join(items)}")
    else:
        st.write("No se encontraron resultados para el término de búsqueda.")
