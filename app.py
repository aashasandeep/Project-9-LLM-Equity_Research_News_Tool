import streamlit as st
from langchain_config1 import get_summary

# Streamlit UI
st.title("Equity Research News Tool")
st.write("Enter your query to get the latest news articles summarized.")

query = st.text_input("Enter Query")

if st.button("Get News Summary"):
    if query:
        st.write("Fetching news and generating summary...")
        try:
            summary = get_summary(query)
            st.write("### Summary:")
            st.write(summary)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("⚠️ Please enter a query.")
        st.sidebar.title('📂 Historical Data Analysis')
        st.sidebar.write('### 📌 Past Queries:') 
    if st.sidebar.button('Analyze'):
        with open('queries.txt', 'r') as file:
            queries = file.readlines()
            st.write('### Historical Queries:')
            st.write(queries)
            