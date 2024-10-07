import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st


url = 'https://raw.githubusercontent.com/LanceMacNal1/Group3_CSS145_Activity3/refs/heads/main/Electronic_sales_Sep2023-Sep2024.csv'
df = pd.read_csv(url)


st.write(pdf)

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


if st.button('Show Gender Pie Chart'):
    pie_chart_gender()

if st.button('Show Payment Method Bar Plot'):
    bar_plot_payment_method()

daily_sales = pd.DataFrame({
    'Purchase Date': pd.date_range(start='2023-01-01', periods=100),
    'Quantity': np.random.randint(1, 20, size=100)
})


st.write(daily_sales)

def plot_daily_sales():
    plt.figure(figsize=(12, 6))
    plt.scatter(daily_sales['Purchase Date'], daily_sales['Quantity'], color='orange', alpha=0.6)
    plt.title('Daily Sales Quantity Over Time')
    plt.xlabel('Date')
    plt.ylabel('Total Quantity Sold')
    plt.xticks(rotation=45)
    plt.grid(axis='y')

    # Fit line
    z = np.polyfit(daily_sales['Purchase Date'].map(pd.Timestamp.timestamp), daily_sales['Quantity'], 1)
    p = np.poly1d(z)
    plt.plot(daily_sales['Purchase Date'], p(daily_sales['Purchase Date'].map(pd.Timestamp.timestamp)), color='red', linestyle='--')

    plt.tight_layout()
    st.pyplot(plt)


if st.button('Show Daily Sales Quantity Plot'):
    plot_daily_sales()

def plot_members_by_gender():
    membership_counts = df.groupby(['Gender', 'Loyalty Member']).size().unstack()

    plt.figure(figsize=(10, 6))
    membership_counts.plot(kind='bar', ax=plt.gca())
    
    plt.title('Number of Members by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Number of Members')
    plt.xticks(rotation=0)
    plt.legend(title='Member')
    plt.grid(axis='y')

    plt.tight_layout()
    st.pyplot(plt)

if st.button('Show Members per Gender'):
    plot_members_by_gender()
def violin_plot():
    plt.figure(figsize=(12, 6))
    sns.violinplot(x='Product Type', y='Rating', data=df, hue='Product Type', palette="Set3", inner='quartile', legend=False)
    plt.title('Customer Rating Distribution by Product Type')
    plt.xlabel('Product Type')
    plt.ylabel('Rating')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)


if st.button('Show Customer Rating Distribution by Product Type'):
    violin_plot()
def box_plot():
    data_to_plot = [
        df[df['Loyalty Member'] == 'Yes']['Age'],
        df[df['Loyalty Member'] == 'No']['Age']
    ]
    
    plt.figure(figsize=(10, 6))
    plt.boxplot(data_to_plot, patch_artist=True)
    plt.title('Age Distribution of Loyalty Members vs. Non-Loyalty Members')
    plt.ylabel('Age')
    plt.xticks([1, 2], ['Loyalty Members', 'Non-Loyalty Members'])
    plt.grid(True)
    plt.tight_layout()
    st.pyplot(plt)

if st.button('Show Age Distribution Box Plot'):
    box_plot()

def pie_chart_product_type():
    product_counts = df['Product Type'].value_counts()
    colors = ['Blue', 'Orange', 'Green', 'Cyan']
    
    plt.figure(figsize=(8, 6))
    plt.pie(product_counts, labels=product_counts.index, autopct='%1.1f%%', colors=colors)
    plt.title('Product Purchase Ratio')
    plt.tight_layout()
    st.pyplot(plt)

if st.button('Show Product Purchase Ratio Pie Chart'):
    pie_chart_product_type()

def shipping_status_count_plot():
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Shipping Type', hue='Order Status', data=df, palette='viridis')
    plt.title('Shipping Status per Shipping Type')
    plt.xlabel('Shipping Type')
    plt.ylabel('Amount')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(plt)

if st.button('Show Shipping Status Count Plot'):
    shipping_status_count_plot()

def pie_chart_order_status():
    colors = ['#A04747', '#EEDF7A']

    plt.figure(figsize=(8, 6))  # Set the figure size
    plt.title('Order Status Distribution')
    survived = df['Order Status'].value_counts()
    plt.pie(survived, labels=survived.index, autopct='%1.1f%%', colors=colors)

    plt.tight_layout()  # Adjust layout
    st.pyplot(plt)  # Display the plot in Streamlit

if st.button('Show Order Status Distribution Pie Chart'):
    pie_chart_order_status()
OrderStatusPayment = df.groupby(['Payment Method', 'Order Status']).size().unstack()

OrderStatusPayment.plot(kind='bar', figsize=(10, 6))

plt.title('Order Status for each Payment Method')
plt.xlabel('Payment Method')
plt.ylabel('Orders')
plt.xticks(rotation=0)
plt.legend(title='Status')
plt.grid(axis='y')


plt.tight_layout()
plt.show()


---
# Conclusion

---

## Gender Ratio
- The chart shows an almost perfect half distribution for men and women. This indicates that there is no concentrated customer gender demographic.

## Payment Methods
- The chart illustrates the preferred payment methods between males and females. Based on the data, we can conclude that credit card transactions are the most common payment method for both genders.

## Annual Sales
- There is an upward trend in the total quantity of sales as we progress through the year.

## Members per Gender
- We observe that there are more male customers in total. Additionally, the ratio of female customers to male customers who are members is relatively similar.

## Customer Rating Distribution
- The graph displays the distribution of customer ratings across different product types, revealing that smartphones are frequently rated as 2 or 5, while tablets, laptops, and smartwatches are rated as 3. Headphones receive ratings from 1 to 5.

## Customer Age Distribution
- This box plot compares the age distribution of loyalty members and non-loyalty members. While the distributions appear similar, individuals aged 33 and 65 are more likely to be non-loyalty members.

## Product Purchase Ratio
- The ratio of product purchases indicates that smartphones and tablets have equally high purchase rates, while smartwatches and laptops show lower purchase rates.

## Shipping Status
- This graph displays the order statuses for each shipping method, indicating whether they are ready to be shipped to the customer.

## Order Status
- The pie chart shows the percentage of orders that are completed versus cancelled. We can deduce that more than two-thirds of the orders have been completed.

## Order Status for Each Payment Method
- In this bar chart, we compare completed and cancelled orders for each payment method. At a glance, it is evident that credit cards have the highest number of completed orders, while PayPal has the least.
