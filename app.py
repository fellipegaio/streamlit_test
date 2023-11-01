import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles.csv', 'rb') # lendo os dados

st.header('Visualização interativa de dados sobre anúncios de veículos') # cabeçalho explicativo
st.write('Para ver mais de um gráfico simultaneamente, use as caixas de seleção abaixo:')

# criar caixas de seleção
hist_price = st.checkbox('Ver somente o histograma de preço') # criar uma caixa de seleção para o histograma de preço
hist_year = st.checkbox('Ver somente o histograma de ano de fabricação') # criar uma caixa de seleção para o histograma de ano
scatter_button = st.checkbox('Ver somente o gráfico de dispersão') # criar uma caixa de seleção para o gráfico de dispersão
pie_fuel = st.checkbox('Ver somente o gráfico de pizza de tipo de combustível') # criar uma caixa de seleção para o gráfico de pizza

if hist_price: # se o histograma de preço for clicado
# escrever uma mensagem
    st.write('Histograma dos preços dos veículos nos anúncios')
    # criar um histograma
    fig_price = px.histogram(car_data, x="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_price, use_container_width=True)

if hist_year: # se o histograma por ano for clicado
# escrever uma mensagem
    st.write('Histograma do ano de fabricação dos veículos nos anúncios')
    # criar um histograma
    fig_year = px.histogram(car_data, x="model_year")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_year, use_container_width=True)

if scatter_button: # se o gráfico de dispersão for clicado
# escrever uma mensagem
    st.write('Gráfico de dispersão sobre anúncios de vendas de carros: Ano de Fabricação versus Preço do Veículo')
    # criar um gráfico de dispersão
    fig_year_price = px.scatter(car_data, x="model_year", y="price")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_year_price, use_container_width=True)

if pie_fuel: # se o gráfico de pizza for clicado
# escrever uma mensagem
    st.write('Gráfico de pizza dos tipos de combustível nos anúncios')
    # criar um gráfico de pizza
    fig_fuel = px.pie(df, names='fuel')
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_fuel, use_container_width=True)

# Criar botão de histograma
build_histogram = st.button('Gerando histograma dos anúncios pela condição dos veículos')

if build_histogram: # se o histograma for selecionado
# escrever a mensagem
    st.write('Histograma de anúncios de vendas de carros de acordo com a condição do veículo')
    # criar um histograma
    fig_hist = px.histogram(car_data, x="condition")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)
