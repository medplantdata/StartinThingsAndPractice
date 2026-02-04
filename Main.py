import streamlit as st
import TestFunctions as tf

search_query = st.text_input("Enter your chemical name query:", value="theobromine")

getMOl = tf.RequestFromCoconut()

if st.button("Search") and search_query:
    resp = getMOl.searchMolecule(search_query)

    st.write("Status:", resp.status_code)
    st.write("Content-Type:", resp.headers.get("Content-Type"))
    st.code(resp.text[:500])