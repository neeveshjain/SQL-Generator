import google.generativeai as genai

def main():
    GOOGLE_API_KEY ="AIzaSyCdGCm8Ge6rEARQ6HnG7qunp1vOJzltlnc"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel( "gemini-pro")

if __name__ == "__main__":
    main()