import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY ="AIzaSyCdGCm8Ge6rEARQ6HnG7qunp1vOJzltlnc"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel( "gemini-pro")

def main():
    st.markdown(
        """
        <div style = "text-align:center;">
        <h1 style="font-size: 30px;">SQL Query Generator bot🤖</h1>
        <h3 style="font-size: 20px;">An A.I tool to generate SQL queries</h3>
        <p style="font-size: 16px;">This tool is designed to help you generate and explain SQL queries for your data.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    text_input = st.text_area("Enter your SQL query here, in plain english:")

    submit = st.button("Generate SQL Query")

    if submit:
        with st.spinner("Generating SQL Query..."):
            template = """Create a SQL query snippet using the below txt:
            ```
            {text_input}
            ```
            I just want a SQL query
            """

            formatted_template = template.format(text_input=text_input)
            response = model.generate_content(formatted_template)
            sql_query = response.text

            sql_query = sql_query.strip().lstrip("```sql").rstrip("```")
            st.write(sql_query)

            expected_output = """
            What would be the expected response of this SQL query snippet:
            ```
            {sql_query}
            ```
            provide sample tabular responses with no explaintation needed
            """
            
            expexted_output_format = expected_output.format (sql_query=sql_query)
            eoutput = model.generate_content(expexted_output_format)
            eoutput = eoutput.text
            st.write(eoutput)

            explanation = """
            What would be the expected response of this SQL query snippet:
            ```
            {sql_query}
            ```
            Please provide with step by step explanation:
            """

            explanation_format = explanation.format(sql_query=sql_query)
            explanation = model.generate_content(explanation_format)
            explanation = explanation.text
            
            with st.container():
                st.write("\n\n")
                st.success("SQL Query Generated Successfully")
                st.code(sql_query,language="sql")
                st.success("Expected Output of this SQL Query:")
                st.markdown(eoutput)
                st.write("\n\n")
                st.success("Explanation:")
                st.markdown(explanation,unsafe_allow_html=True)
                st.write("\n\n")
                st.info("This tool is powered by Google's Generative AI model")
                st.write("\n\n")

if __name__ == "__main__":
    main()
