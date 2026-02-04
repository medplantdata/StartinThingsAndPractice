import streamlit as st
import streamlit.components.v1 as components
from TestFunctions import RequestFromCoconut 
from rdkit import Chem

search_query = st.text_input("Enter your chemical name query:", value = "theobromine")

getMOl = RequestFromCoconut()
if st.button("Search") and search_query:
    raw = getMOl.searchMolecule(search_query)
    st.code(raw[:500])

if st.button("Search"):
    result = getMOl.searchMolecule(search_query)
    st.write(result)