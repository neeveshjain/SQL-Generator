import streamlit as st
import google.generativeai as genai
import simple

GOOGLE_API_KEY ="AIzaSyCdGCm8Ge6rEARQ6HnG7qunp1vOJzltlnc"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel( "gemini-pro")

def main():
    st.sidebar.title("Nav-bar")
    app_mode = st.sidebar.selectbox("Choose a page", ["Home","simple", "advance"])

    if app_mode == "Home":
        st.title("Choose one option")
        st.write("simple: for simple sql generator")
        st.write("advance: for advance sql generator")
        

    elif app_mode == "simple":
        # Add your content for the Home page here
        simple.main()

    elif app_mode == "advance":
        st.title("here I present advance sql genrator")
        # Add your content for the About page here

if __name__ == "__main__":
    main()
