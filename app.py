import streamlit as st
import pandas as pd
import plotly.express as px  # Asegúrate de que la importación sea correcta

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Limpieza de datos
# Fill NA values
car_data['model_year'] = car_data['model_year'].fillna(
    car_data['model_year'].mean())
car_data['odometer'] = car_data['odometer'].fillna(car_data['odometer'].mean())
car_data['cylinders'] = car_data['cylinders'].fillna(
    round(car_data['cylinders'].mean()))

# Convertir a enteros
car_data['model_year'] = car_data['model_year'].astype(int)
car_data['odometer'] = car_data['odometer'].astype(int)

# Convertir date_posted a formato datetime
car_data['date_posted'] = pd.to_datetime(car_data['date_posted'])

# Eliminar duplicados
car_data.drop_duplicates(inplace=True)

# Rellenar NA en paint_color con "No Specified"
car_data['paint_color'] = car_data['paint_color'].fillna('No Specified')

# Rellenar NA en is_4wd con 0
car_data['is_4wd'] = car_data['is_4wd'].fillna(0)

# Título de la aplicación
st.title("Análisis de anuncios de venta de coches")


st.header("Histograma del odómetro")
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:

    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)


st.header("Scatterplot: Odómetro vs Precio")
disp_button = st.button('Construir Scatterplot')

if disp_button:
    st.write(
        'Creación de un scatterplot para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)


st.header("Casillas de Verificación")
build_histogram = st.checkbox('Mostrar Autos mas vendidos')
if build_histogram:
    st.write(
        'Lista de los tipos de Autos mas vendidos')
    top_10_types = car_data['type'].value_counts().nlargest(
        10).reset_index()
    top_10_types.columns = ['type', 'count']
    fig = px.bar(top_10_types, x='type', y='count',
                 title="Top 10 Años de Modelo Más Vendidos")
    fig.update_layout(xaxis_title="Año de Modelo",
                      yaxis_title="Cantidad de Coches")
    st.plotly_chart(fig, use_container_width=True)
