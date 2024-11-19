import streamlit as st

# Título de la aplicación
st.title("Buscador Simple")

# Descripción de la aplicación
st.write("Introduce un término de búsqueda para encontrar información.")

# Cuadro de texto para buscar
search_term = st.text_input("¿Qué estás buscando?")

# Simulación de datos (puedes reemplazar esto con tus propios datos)
data = {
    "Fútbol": ["Lionel Messi", "Cristiano Ronaldo", "Neymar Jr", "Kylian Mbappé"],
    "Balón de Oro": ["Lionel Messi", "Cristiano Ronaldo", "Johan Cruyff"],
    "Copa del Mundo": ["Brasil", "Alemania", "Italia", "Argentina"],
}

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
