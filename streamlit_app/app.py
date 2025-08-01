import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set wide layout
st.set_page_config(page_title="📚 Book Store Scraper Dashboard", layout="wide")

# Load CSV
df = pd.read_csv("scraped_books.csv")

# Convert price column if not already numeric
if df['Price'].dtype == object:
    df['Price'] = df['Price'].str.replace('£', '').astype(float)

# Title
st.title("📚 Book Store Scraper Dashboard")

# Dropdown to select a book title
book_titles = df['Title'].sort_values().unique()
selected_title = st.selectbox("📖 Select a Book Title", book_titles)

# Filter the DataFrame for the selected book
selected_book = df[df['Title'] == selected_title].iloc[0]

# 3-column layout for details
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Price (£)", f"{selected_book['Price']:.2f}")

with col2:
    st.metric("⭐ Rating", selected_book['Rating'])

with col3:
    st.metric("📦 Availability", selected_book['Availability'])

# Optional: Show all data
st.subheader("📄 All Book Data")
st.dataframe(df)

# Optional Visualizations
st.subheader("📊 Rating Distribution")
fig1 = sns.countplot(x='Rating', data=df, order=['One', 'Two', 'Three', 'Four', 'Five'])
st.pyplot(fig1.figure)

st.subheader("💸 Price Distribution")
fig2 = sns.histplot(df['Price'], bins=10, kde=True)
st.pyplot(fig2.figure)
