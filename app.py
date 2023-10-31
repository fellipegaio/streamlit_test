import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles.csv') # lendo os dados

st.header('Visualização interativa de dados sobre anúncios de veículos') # cabeçalho explicativo

hist_button = st.button('Ver somente o histograma') # criar um botão para o histograma
scatter_button = st.button('Ver somente o gráfico de dispersão') # criar um botão para o gráfico de dispersão

if hist_button: # se o botão de histograma for clicado
# escrever uma mensagem
    st.write('Histograma de anúncios de vendas de carros de acordo com a condição do veículo')
    # criar um histograma
    fig_hist = px.histogram(car_data, x="condition")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_button: # se o botão de gráfico de dispersão for clicado
# escrever uma mensagem
    st.write('Gráfico de dispersão sobre anúncios de vendas de carros: ano de fabricação v preço')
    # criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="model_year", y="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)

st.write('Para ver mais de um gráfico simultaneamente, use as caixas de seleção abaixo:')
# criar caixas de seleção
build_histogram = st.checkbox('Gerar histograma dos anúncios pela condição dos veículos')
build_scatter = st.checkbox('Gerar gráfico de dispersão sobre anúncios cruzando o ano de fabricação do veículo com o seu preço de venda')

if build_histogram: # se o histograma for selecionado
# escrever a mensagem
    st.write('Histograma de anúncios de vendas de carros de acordo com a condição do veículo')
    # criar um histograma
    fig_hist = px.histogram(car_data, x="condition")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)
if build_scatter: # se o gráfico de dispersão for selecionado
# escrever a mensagem
    st.write('Gráfico de dispersão sobre anúncios de vendas de carros: ano de fabricação v preço')
    # criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="model_year", y="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
