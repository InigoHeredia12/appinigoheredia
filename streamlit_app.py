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
st.write('Resolución de problemas: Habilidad para encontrar soluciones creativas e innovadoras a desafíos.
Ejemplo: Si se presenta un imprevisto durante un evento social, puedes pensar rápidamente en alternativas para mantener a todos contentos.
Aprendizaje rápido: Capacidad de adquirir nuevos conocimientos y habilidades de manera eficiente.
Ejemplo: Puedes aprender a usar un nuevo programa informático en poco tiempo y con facilidad.
Adaptabilidad: Flexibilidad para ajustarte a nuevas situaciones y cambios.
Ejemplo: Puedes cambiar tus planes de manera espontánea si surge una mejor oportunidad.')


# Sección de logros
st.header('Logros')
st.write('Aquí puedes listar tus logros destacados.')

# Sección de contacto
st.header('Contacto')
st.write('Aquí puedes proporcionar información sobre cómo contactarte.')

