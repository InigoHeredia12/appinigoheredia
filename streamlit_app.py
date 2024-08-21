import streamlit as st

st.title('Currículum Iñigo Heredia Hernandez')

st.header('Introducción')
st.write('Soy una persona trabajadora, apasionada por el deporte y muy sociable. Disfruto de los desafíos y me encanta rodearme de gente positiva.')

col1, col2 = st.columns(2)

with col1:
    st.header('Experiencia Profesional')
    st.write('Afix Financiera 2021 - 2022')
    st.write('Tribu Living 2022 - 2023')
    st.write('Cb Espacios 2023 - 2024')

    st.header('Experiencia Profesional')
    st.write('Afix Financiera 2021 - 2022')
    st.write('Tribu Living 2022 - 2023')
    st.write('Cb Espacios 2023 - 2024')

with col2:
    st.header('Habilidades')
    st.write('Resolución de problemas: Habilidad para encontrar soluciones creativas e innovadoras a desafíos.')
    st.write('Aprendizaje rápido: Capacidad de adquirir nuevos conocimientos y habilidades de manera eficiente.')
    st.write('Adaptabilidad: Flexibilidad para ajustarte a nuevas situaciones y cambios.')

# Sección de logros
st.header('Logros')
st.write('Aquí puedes listar tus logros destacados.')

# Sección de contacto
st.header('Contacto')
st.write('Aquí puedes proporcionar información sobre cómo contactarte.')

