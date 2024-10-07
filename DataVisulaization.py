import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st

# Load the dataset
url = 'https://raw.githubusercontent.com/LanceMacNal1/Group3_CSS145_Activity3/refs/heads/main/Electronic_sales_Sep2023-Sep2024.csv'
df = pd.read_csv(url)

# Display the DataFrame
st.write(df)

def pie_chart_gender():
    gender_counts = df['Gender'].value_counts()
    colors = ['Blue', 'Pink']
    plt.figure(figsize=(8, 6))
    plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', colors=colors)
    plt.title('Customer Gender Ratio')
    st.pyplot(plt)

def bar_plot_payment_method():
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Payment Method', hue='Gender', data=df)
    plt.title('Preferred Payment Method')
    plt.xlabel('Payment Method')
    plt.ylabel('Count')
    plt.xticks(rotation=30)
    st.pyplot(plt)

# Create buttons to display charts
if st.button('Show Gender Pie Chart'):
    pie_chart_gender()

if st.button('Show Payment Method Bar Plot'):
    bar_plot_payment_method()
