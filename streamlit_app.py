import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = 'C:/Users\Dell/Desktop/jumia_project/jumia_products_clean.csv'
st.title('Jumia Data UI Page')

# checking if path exists
st.subheader('Loading data')
st.write('The data will loaded was scraped from an e comerce website in kenya called jumia')
st.write(f'link - {file_path}')
if os.path.exists(file_path):
    # load csv file
    df = pd.read_csv(file_path)
    st.success('File loaded successfully')
else:
    st.error(f'File not found in {file_path}')
    df = None
# Check if a file is uploaded
if df is not None:
    try:
         # Display the first few rows of the DataFrame
        st.write("Here are the first few rows of the uploaded data:")
        st.write(df.head())

        # displaying 10 most expensive productsand visualizing them
        st.write('The 10 most expensive products currently are:')
        top_expensive = df.sort_values(by='Current price', ascending=False).head(10)
        st.write(top_expensive)

        # plotting
        st.write('Here is the visualization')

        top_expensive['Shortened Name'] = top_expensive['Item name'].apply(lambda x: x[:25])  # Truncate to 20 characters

        fig1, ax1 = plt.subplots(figsize=(10,6))
        top_expensive.plot(kind='bar',x = 'Shortened Name', y = 'Current price', ax=ax1, color='skyblue')
        ax1.set_title('Top 10 most expensive products')
        ax1.set_xlabel('Item name')
        ax1.set_ylabel('Current price')

        # displaying the plot on streamlit 
        st.pyplot(fig1)

        # top 10 highest discounted products
        st.write('Here are the top 10 highest discointed products')
        top_discounted = df.sort_values(by='Discount', ascending=False).head(10)
        st.write(top_discounted)

        # plotting
        st.write('Here is the visualiation')

        top_discounted['Shortened Name'] = top_discounted['Item name'].apply(lambda x: x[:25])  # Truncate to 20 characters

        fig2, ax2 = plt.subplots(figsize=(10,6))
        top_discounted.plot(kind='bar', x='Shortened Name', y='Discount', ax=ax2, color='skyblue')
        ax2.set_title('Top 10 most discounted products')
        ax2.set_xlabel('Item name')
        ax2.set_ylabel('Discount')
        
        # displaying the plot on streamlit
        st.pyplot(fig2)
        
    except Exception as e:
        st.error(f"Error: {e}")

else:
    st.info("Please upload a CSV file.")
