# Análisis de Anuncios de Venta de Coches

Este proyecto utiliza Streamlit para crear una aplicación web interactiva que analiza anuncios de venta de coches. Los datos se cargan desde un archivo CSV y se limpian antes de visualizarlos mediante gráficos interactivos.

## Requisitos

- Python 3.x
- Streamlit
- Pandas
- Plotly

## Instalación

1. Clona este repositorio.
2. Instala las dependencias necesarias utilizando pip:

    ```bash
    pip install streamlit pandas plotly
    ```

3. Ejecuta la aplicación:

    ```bash
    streamlit run app.py
    ```

## Uso

### Cargar los Datos

Los datos se cargan desde el archivo `vehicles_us.csv` y se limpian para asegurar que no haya valores nulos y que los tipos de datos sean correctos.

### Limpieza de Datos

- Rellenar valores nulos en `model_year`, `odometer` y `cylinders` con la media.
- Convertir `model_year` y `odometer` a enteros.
- Convertir `date_posted` a formato datetime.
- Eliminar duplicados.
- Rellenar valores nulos en `paint_color` con "No Specified".
- Rellenar valores nulos en `is_4wd` con 0.

### Visualizaciones

#### Histograma del Odómetro

Haz clic en el botón "Construir histograma" para generar un histograma del odómetro de los coches.

#### Scatterplot: Odómetro vs Precio

Haz clic en el botón "Construir Scatterplot" para generar un scatterplot que muestra la relación entre el odómetro y el precio de los coches.

### Repositorio
[Repo Sprint 7](https://github.com/artemisaix/sprint7)