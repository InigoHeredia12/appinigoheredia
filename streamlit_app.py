import streamlit as st

# Título de la aplicación
st.title('Currículum Iñigo Heredia Hernandez')

# Sección de introducción
st.header('Introducción')
st.write('Soy una persona trabajadora, apasionada por el deporte y muy sociable. Disfruto de los desafíos y me encanta rodearme de gente positiva.')

# Crear dos columnas para dividir el contenido
col1, col2 = st.columns(2)

with col1:
    st.header('Experiencia Profesional')
    st.write('Afix Financiera 2021 - 2022')
    st.write('Tribu Living 2022 - 2023')
    st.write('Cb Espacios 2023 - 2024')

    st.header('Educación')
    st.write('Liceo del Valle 2009 - 2021')
    st.write('Universidad Panamericana 2021 - Ahora')

with col2:
    st.header('Educación')
    st.write('Liceo del Valle 2009 - 2021')
    st.write('Universidad Panamericana 2021 - Ahora')

# Sección de habilidades
st.header('Habilidades')
st.write('Aquí puedes listar tus habilidades técnicas y blandas.')

# Sección de logros
st.header('Logros')
st.write('Aquí puedes listar tus logros destacados.')

# Sección de contacto
st.header('Contacto')
st.write('Aquí puedes proporcionar información sobre cómo contactarte.')

