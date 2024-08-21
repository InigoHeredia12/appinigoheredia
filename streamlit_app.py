import streamlit as st

st.title('Currículum Iñigo Heredia Hernandez')

col1, col2 = st.columns(2)

with col1:
    
    st.header('Hobbies')
    st.markdown("""
    - Pasar tiempo con amigos
    - Hacer Ejercicio
    - Relacionarme con gente
    """)

    st.header('Experiencia Profesional')
    st.markdown("""
    - Yeti.com 2017 - 2018
    - Afix Financiera 2019 - 2019
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


st.header('Mi Meta')
st.write('Mi objetivo es convertirme en un líder empresarial influyente, inspirando a otros a alcanzar sus sueños. Paralelamente, deseo formar una familia unida y estable, donde el amor y el apoyo mutuo sean pilares fundamentales.')

st.markdown('---') 

st.header('Contacto')

contact_info = [
    ("Número de Celular", "+52 3322567569"),
    ("Email", "inigoh@hotmail.com"),
    ("LinkedIn", "https://linkedin.com/in/tu-perfil")
]

# Mostrar la tabla en Streamlit
for label, value in contact_info:
    st.write(f"**{label}:** {value}")

