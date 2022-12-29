import pandas_ta as pta
import pandas as pd
import krakenex
import plotly.graph_objects as go
import plotly.express as px
import datetime
import calendar
import time
import streamlit as st
from pykrakenapi import KrakenAPI

"""
# Proyecto Final: Python para análisis de Datos. 
### Máster UNAV en Big Data Science

Diego Arsenio García, Gonzalo Tomás

"""


from proyecto_final import proyecto, transform_data, get_rsi

data, pair = proyecto()

data = transform_data(data)


st.markdown('***')

st.write(f'Trabajamos con el par: {pair}')

"""## Graficar cotizaciones.
- Graficar el par .
- Input de usuario que permita graficar cualquier cotización o una a elegir en el menú.
"""

fig = px.line(data, x='date', y="close", title=pair)
st.plotly_chart(fig)

"""
## Indicadores técnicos: 
- Calcular el Media Móvil y graficarla.
- Calcular el RSI y graficarlo.
- Graficar el Media Móvil junto con la cotización del par calculado.
"""

"""
## Media Móvil

Este gráfico contiene la Media Móvil del par seleccionado anteriormente. 
Se consideran dos tipos de Media Móvil: 
- Standard, usando la función de `rolling`
- Exponential, utilizando la función de `ewm`
"""

data = transform_data(data)

fig = px.line(data, x='date', y=[
              "MA_price", "EMA_price"], title="Moving Average Comparison")
st.plotly_chart(fig)

"""
## RSI

En esta gráfica, vemos el RSI.
"""

data = get_rsi(data)

fig = px.line(data, x='date', y=["rsi"], title="RSI Plot")
st.plotly_chart(fig)

# Graficar el Media Móvil junto con la cotización del par calculado

"""
## Media Móvil vs Cotización. 
En este gráfico encontramos tanto la Media Móvil como el valor de closing. 
"""

fig = px.line(data, x='date', y=["MA_price", "close"],
              title="Moving Average Comparison vs Closing Price")
st.plotly_chart(fig)


"""
## Gráfica Final
En esta última gráfica, vemos todas las métricas que se han creado anteriormente en una gráfica. 
"""

fig = px.line(data, x='date', y=["MA_price", "close", "open", "rsi"],
              title="Moving Average Comparison vs Closing Price vs RSI")
st.plotly_chart(fig)
