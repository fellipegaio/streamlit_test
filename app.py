import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles.csv') # reading the data

st.header('Interactive Data Visualization of Vehicle Advertisements') # explanatory jheader
st.write('To view more than one chart simultaneously, use the checkboxes below.')
st.write("To view the histogram of the advertised vehicles' condition, use the button at the bottom.")

# criar caixas de seleção
hist_price = st.checkbox('Price Histogram') # creating a checkbox for the price histogram
hist_year = st.checkbox('Manufacturing Year Histogram') # creating a checkbox for the year histogram
scatter_button = st.checkbox('Scatter Plot between Manufacturing Year and Price') # creating a checkbox for the scatter plot
pie_fuel = st.checkbox('Fuel Type Pie Chart') # creating a checkbox for the pie chart

if hist_price: # if the price histogram is clicked
# write the message
    st.write('Histogram of vehicle prices in the advertisements')
    # plot the histogram
    fig_price = px.histogram(car_data, x="price")
    # showing an interactive Plotly chart
    st.plotly_chart(fig_price, use_container_width=True)

if hist_year: # if the manufacturing year of vehicles histogram is clicked
# write the message
    st.write('Histogram of the manufacturing year of vehicles in the advertisements')
    # plot the histogram
    fig_year = px.histogram(car_data, x="model_year")
    # showing an interactive Plotly chart
    st.plotly_chart(fig_year, use_container_width=True)

if scatter_button: # if the scatter plot button is selected
# write the message
    st.write('Scatter plot on car sales advertisements: Manufacturing Year versus Vehicle Price')
    # plot the scatter plot
    fig_year_price = px.scatter(car_data, x="model_year", y="price")
    # showing an interactive Plotly chart
    st.plotly_chart(fig_year_price, use_container_width=True)

if pie_fuel: # if the pie chart is selected
# write the message
    st.write('Pie chart of fuel types in the advertisements')
    # plot the pie chart
    fig_fuel = px.pie(car_data, names='fuel')
    # showing an interactive Plotly chart
    st.plotly_chart(fig_fuel, use_container_width=True)

# creating the histogram button
build_histogram = st.button('Vehicle Condition Histogram')

if build_histogram: # if he histogram button is clicked
# write the message
    st.write("Histogram of car sales advertisements based on the vehicle's condition")
    # create the histogram
    fig_hist = px.histogram(car_data, x="condition")
    # showing an interactive Plotly chart
    st.plotly_chart(fig_hist, use_container_width=True)
