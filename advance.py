import streamlit as st
import google.generativeai as genai
import googleAPI

googleAPI.main()

def main():
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
            st.write(data_types)

    #Writing code that will connect to the database and get the data from the database
#------------------------------------------------------------------------------------------------------    

if __name__ == "__main__":
    main()