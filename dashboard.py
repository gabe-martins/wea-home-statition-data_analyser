import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from plotly.offline import plot

from get_data import get_data

def main():
  df = get_data()
  # Título do Dashboard
  st.title("Temperature and Humidity Dashboard")

  # Mostrando o DataFrame na interface do Streamlit
  st.subheader("Data Table")
  st.dataframe(df[['date', 'time', 'temperature', 'humidity']])
  
  st.subheader("Estatísticas")
  st.write(df.describe())


  # Criando o gráfico de linha com Plotly
  fig = go.Figure()

  # Linha de temperatura
  fig.add_trace(go.Scatter(
      x=df['date_time'], 
      y=df['temperature'],
      mode='lines+markers',
      name='Temperature',
      line=dict(color='firebrick', width=2),
      marker=dict(size=6)
  ))

  # Linha de umidade
  fig.add_trace(go.Scatter(
      x=df['date_time'], 
      y=df['humidity'],
      mode='lines+markers',
      name='Humidity',
      line=dict(color='royalblue', width=2),
      marker=dict(size=6)
  ))

  # Ajustando o layout
  fig.update_layout(
      title='Temperature and Humidity Over Time',
      xaxis_title='Date/Time',
      yaxis_title='Value',
      legend_title='Metrics',
      hovermode='x',
      template='plotly_white'
  )

  # Exibindo o gráfico no Streamlit
  st.subheader("Temperature and Humidity Over Time")
  st.plotly_chart(fig)

  # Adicionando interatividade (filtrando por data)
  st.subheader("Filter by Date")
  selected_date = st.selectbox("Select Date", df['date'].unique())

  # Filtrando os dados pelo valor da data selecionada
  filtered_df = df[df['date'] == selected_date]

  st.write(f"Data for {selected_date}")
  st.dataframe(filtered_df[['time', 'temperature', 'humidity']])

  
main()