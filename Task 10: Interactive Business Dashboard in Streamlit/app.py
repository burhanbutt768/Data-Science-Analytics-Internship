#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df = pd.read_csv("D:\Data Science & Analytics Internship\Phase 2\Task 10 Interactive Business Dashboard in Streamlit\superstore.csv", encoding='latin1')
df.head()


# In[3]:


df.info()


# In[4]:


df.isnull().sum()


# In[5]:


# Page configuration
st.set_page_config(page_title="Business Dashboard", layout="wide")

# Title
st.title("📊 Global Superstore Business Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("D:\Data Science & Analytics Internship\Phase 2\Task 10 Interactive Business Dashboard in Streamlit\superstore.csv", encoding='latin1')
    df['Order.Date'] = pd.to_datetime(df['Order.Date'])
    return df

df = load_data()


# Sidebar Filters

st.sidebar.header("🔍 Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df['Category'].unique(),
    default=df['Category'].unique()
)

sub_category = st.sidebar.multiselect(
    "Select Sub.Category",
    options=df['Sub.Category'].unique(),
    default=df['Sub.Category'].unique()
)

# Apply filters

filtered_df = df[
    (df['Region'].isin(region)) &
    (df['Category'].isin(category)) &
    (df['Sub.Category'].isin(sub_category))
]


# KPI Metrics

total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()

col1, col2 = st.columns(2)

col1.metric("💰 Total Sales", f"${total_sales:,.2f}")
col2.metric("📈 Total Profit", f"${total_profit:,.2f}")


#Top 5 Customers

st.subheader("🏆 Top 5 Customers by Sales")

top_customers = (
    filtered_df.groupby("Customer.Name")['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

fig, ax = plt.subplots()
top_customers.plot(kind='bar', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)


#Sales by Category

st.subheader("📦 Sales by Category")
sales_category = filtered_df.groupby("Category")['Sales'].sum()
fig2, ax2 = plt.subplots()
sales_category.plot(kind='bar', ax=ax2)
st.pyplot(fig2)

