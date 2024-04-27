import streamlit as st
import google.generativeai as genai
import googleAPI

googleAPI.main()
model = genai.GenerativeModel("gemini-pro")

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
            st.write(column_names)
            st.write(data_types)

    text_input = st.text_area("Enter your SQL query here, in plain english:")
    submit = st.button("Generate SQL Query")
    if submit:
        with st.spinner("Generation SQL Query..."):
            template = """ Create a SQl query snippet using the below text:
            ```
            {text_input}
            ```
            The database schema includes the following columns and their corresponding data types:
            ```
            {column_names}, {data_types}
            ```

            I just want a SQL query
            """
            formatted_template = template.format(text_input=text_input, column_names=column_names, data_types=data_types)
            response = model.generate_content(formatted_template)
            sql_query = response.text
            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
            st.write(sql_query)   
            conn = st.connection('mysql', type='sql')
            df = conn.query(sql_query, ttl=600)
            st.write(df)
                

if __name__ == "__main__":
    main()