import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles.csv') # lendo os dados

st.header('Visualização interativa de dados sobre veículos')

hist_button = st.button('Criar histograma') # criar um botão
scatter_button = st.button('Criar gráfico de dispersão') # criar um botão

if hist_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Histograma de anúncios de vendas de carros de acordo com a condição do veículo')
    # criar um histograma
    fig_hist = px.histogram(car_data, x="condition")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

if scatter_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Gráfico de dispersão sobre anúncios de vendas de carros: ano de fabricação v preço')
    # criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="model_year", x_label="Ano de fabricação", y="price", y_label="Preço")
    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)

# criar uma caixa de seleção
#build_histogram = st.checkbox('Criar um histograma')

#if build_histogram: # se a caixa de seleção for selecionada
#    st.write('Criando um histograma para a coluna odometer')
