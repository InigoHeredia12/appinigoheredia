import streamlit as st

col1, col2 = st.columns(2)


with col1:

    # URL de la imagen (enlace directo desde Google Drive)
    image_url = 'https://drive.google.com/file/d/FILE_ID'
    st.image(image_url, width=150)  # Ajusta el ancho según sea necesario
    
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

    st.title('Currículum Iñigo Heredia Hernandez')
    
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

st.markdown('---')  # Línea horizontal en Markdown

st.header('Contacto')

contact_info = [
    ("Número de Celular", "+52 3322567569"),
    ("Email", "inigoh@hotmail.com"),
    ("LinkedIn", "https://linkedin.com/in/tu-perfil")
]

# Mostrar la tabla en Streamlit
for label, value in contact_info:
    st.write(f"**{label}:** {value}")

