import streamlit as st

st.title('Currículum Iñigo Heredia Hernandez')

col1, col2 = st.columns(2)

with col1:
    st.header('Experiencia Profesional')
    st.markdown("""
    - Afix Financiera 2021 - 2022
    - Tribu Living 2022 - 2023
    - Cb Espacios 2023 - 2024
    """)

    st.header('Experiencia Profesional')
    st.markdown("""
    - Afix Financiera 2021 - 2022
    - Tribu Living 2022 - 2023
    - Cb Espacios 2023 - 2024
    """)

with col2:
    st.header('Habilidades')
    st.markdown("""
    - **Resolución de problemas:** Habilidad para encontrar soluciones creativas e innovadoras a desafíos.
    - **Aprendizaje rápido:** Capacidad de adquirir nuevos conocimientos y habilidades de manera eficiente.
    - **Adaptabilidad:** Flexibilidad para ajustarte a nuevas situaciones y cambios.
    """)

    st.header('Logros')
    st.markdown("""
    - Miembro de la sociedad de alumnos del liceo del valle
    - Miembro del comite de la generacion 2021
    - Ganador de los up games 2021
    """)

# Línea de separación para la sección de contacto
st.markdown('---')  # Línea horizontal en Markdown

# Sección de contacto
st.header('Contacto')
st.write('Aquí puedes proporcionar información sobre cómo contactarte.')

# Crear una tabla de contacto sin pandas
contact_info = [
    ("Número de Celular", "+1234567890"),
    ("Email", "tuemail@example.com"),
    ("LinkedIn", "[Tu Perfil de LinkedIn](https://linkedin.com/in/tu-perfil)")
]

# Mostrar la tabla en Streamlit
for label, value in contact_info:
    st.write(f"**{label}:** {value}")

