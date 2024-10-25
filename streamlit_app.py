import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar la página de Streamlit
st.set_page_config(page_title="Simulador de ETFs Allianz", layout="wide")

# Título de la aplicación
st.title("Simulador Financiero de ETFs - Allianz Patrimonial")

# Función para descargar datos de ETFs
def descargar_datos(etf, periodo):
    data = yf.download(etf, period=periodo)
    return data

# Función para calcular rendimiento y riesgo
def calcular_rendimiento_riesgo(data):
    data['Rendimiento Diario'] = data['Adj Close'].pct_change()
    rendimiento = data['Rendimiento Diario'].mean() * 252  # Rendimiento anualizado
    riesgo = data['Rendimiento Diario'].std() * np.sqrt(252)  # Volatilidad anualizada
    return rendimiento, riesgo

# Función para mostrar gráficos
def mostrar_graficos(data, etf):
    st.subheader(f"Gráfico del ETF: {etf}")
    plt.figure(figsize=(10, 6))
    plt.plot(data.index, data['Adj Close'], label=etf)
    plt.title(f"Precio Ajustado de {etf}")
    plt.xlabel("Fecha")
    plt.ylabel("Precio")
    plt.grid(True)
    st.pyplot(plt)

# Sidebar: Selección de ETF y Periodo
etfs = ['SPY', 'IVV', 'VOO', 'QQQ', 'EFA']  # Lista de ETFs (puedes agregar más)
etf_seleccionado = st.sidebar.selectbox("Selecciona el ETF", etfs)
periodos = ['1mo', '3mo', '6mo', '1y', 'ytd', '3y', '5y', '10y']
periodo_seleccionado = st.sidebar.selectbox("Selecciona el Periodo", periodos)

# Descargar y mostrar datos
st.subheader(f"Datos del ETF: {etf_seleccionado}")
data = descargar_datos(etf_seleccionado, periodo_seleccionado)
st.dataframe(data.tail(10))  # Mostrar las últimas 10 filas de datos

# Calcular rendimiento y riesgo
rendimiento, riesgo = calcular_rendimiento_riesgo(data)
st.write(f"**Rendimiento Anualizado**: {rendimiento:.2%}")
st.write(f"**Volatilidad Anualizada (Riesgo)**: {riesgo:.2%}")

# Mostrar gráficos
mostrar_graficos(data, etf_seleccionado)

# Posibles mejoras: ratios financieros adicionales o cálculos personalizados

# Footer
st.sidebar.markdown("**Desarrollado por el equipo de Allianz Patrimonial**")


