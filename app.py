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

    # elif app_mode == "advance":
    #     st.title("Advance SQL generator")
    #     st.write("In this type of SQL generator you can add the column name and the data type of the column as an input, and connect you database to it so to get live data from the database")
    #     column_names = []
    #     data_types = []

    #     column_counter = 1
    #     while True:
    #         column_name = st.text_input(f"Enter column name {column_counter}:", key=f"column_name_input_{column_counter}")
    #         data_type = st.text_input(f"Enter data type {column_counter}:", key=f"data_type_input_{column_counter}")
            
    #         column_names.append(column_name)
    #         data_types.append(data_type)
            
    #         add_more = st.button("Add more columns", key=f"add_more_button_{column_counter}")
    #         done = st.button("Done", key=f"done_button_{column_counter}")
            
    #         if done:
    #             break
    #         if add_more:
    #             column_counter += 1
    elif app_mode == "advance":
        st.title("Advance SQL generator")
        st.write("In this type of SQL generator you can add the column name and the data type of the column as an input, and connect you database to it so to get live data from the database")
        
        column_counter = st.number_input('Number of columns', min_value=1, value=1, step=1)

        column_names = []
        data_types = []

        with st.form(key='columns_form'):
            for i in range(column_counter):
                column_name = st.text_input(f"Enter column name {i+1}:", key=f"column_name_input_{i+1}")
                data_type = st.text_input(f"Enter data type {i+1}:", key=f"data_type_input_{i+1}")
                
                column_names.append(column_name)
                data_types.append(data_type)

            if st.form_submit_button("Done"):
                # process the column_names and data_types here
                st.write(column_names)


if __name__ == "__main__":
    main()
