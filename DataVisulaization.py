import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
from mpl_toolkits.mplot3d import Axes3D

url = 'https://raw.githubusercontent.com/LanceMacNal1/Group3_CSS145_Activity3/refs/heads/main/Electronic_sales_Sep2023-Sep2024.csv'

df = pd.read_csv(url)

df

def pie_chart_Gender():

  gender = df['Gender'].value_counts()
  colors = ['Blue', 'Pink']
  plt.pie(gender, labels = ['Male', 'Female'], autopct='%1.1f%%', colors=colors)
  plt.title('Customer Gender Ratio')
  plt.show()

pie_chart_Gender()

def bar_plot_PayMethod():
  sns.countplot(x='Payment Method', hue='Gender', data=df)
  plt.title('Preferred Payment Method')
  plt.xlabel('Payment Method')
  plt.ylabel('Count')
  plt.xticks(rotation=30)
  plt.show()

bar_plot_PayMethod()


