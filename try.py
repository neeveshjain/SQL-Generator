import streamlit as st

with st.form("Number of Products"):
  numProducts = st.number_input('Insert a number', key='numProducts')
  submitForm = st.form_submit_button("Set Product Number")

  if submitForm:
    st.success("Please assign product codes below")

if 'numProducts' in st.session_state.keys():
  with st.form("Product Codes"):
    for i in range(st.session_state['numProducts']):
      # insert text inputs with keys here