import streamlit as st

st.title('Currículum Iñigo Heredia Hernandez')

st.header('Introducción')
st.write('Soy una persona trabajadora, apasionada por el deporte y muy sociable. Disfruto de los desafíos y me encanta rodearme de gente positiva.')

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
    st.write(- 'Resolución de problemas: Habilidad para encontrar soluciones creativas e innovadoras a desafíos.')
    st.write('Aprendizaje rápido: Capacidad de adquirir nuevos conocimientos y habilidades de manera eficiente.')
    st.write('Adaptabilidad: Flexibilidad para ajustarte a nuevas situaciones y cambios.')

    st.header('Logros')
    st.write('Miembro de la sociedad de alumnos del liceo del valle')
    st.write('Miembro del comite de la generacion 2021')
    st.write('Ganador de los up games 2021')

# Sección de contacto
st.header('Contacto')
st.write('Aquí puedes proporcionar información sobre cómo contactarte.')

