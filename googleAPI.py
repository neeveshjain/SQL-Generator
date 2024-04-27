import google.generativeai as genai
import streamlit as st

def main():
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel( "gemini-pro")

if __name__ == "__main__":
    main()
