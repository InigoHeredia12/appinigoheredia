import streamlit as st

st.markdown("<h1 style='text-align: center;'>Currículum Iñigo Heredia Hernandez</h1>", unsafe_allow_html=True)

st.markdown('---') 

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
st.write('Mi meta es convertirme en un líder visionario y emprendedor, capaz de inspirar a equipos y construir organizaciones de alto rendimiento. Quiero crear un negocio que no solo sea rentable, sino que también sea un lugar donde las personas puedan crecer y desarrollarse. Paralelamente, deseo construir una familia unida y compasiva, basada en valores sólidos como el respeto, la honestidad y la integridad. Mi objetivo es ser un ejemplo para mis hijos y demostrarles que con trabajo duro y dedicación se pueden alcanzar grandes metas.')

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

