import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Análisis de anuncios de venta de coches')

# Leer datos
df = pd.read_csv('vehicles_us.csv')

# Checkbox para histograma
build_hist = st.checkbox('Mostrar histograma de kilometraje')

if build_hist:
    st.write('Distribución del kilometraje de los vehículos')
    fig = px.histogram(df, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Checkbox para scatter
build_scatter = st.checkbox('Mostrar gráfico Precio vs Kilometraje')

if build_scatter:
    st.write('Relación entre precio y kilometraje')
    fig = px.scatter(df, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)