import streamlit as st
import streamlit.components.v1 as components
from TestFunctions import RequestFromCoconut 
from TestFunctions import RequestFromChEMBL
from rdkit import Chem
from rdkit.Chem import Draw

search_query = st.text_input("Enter your chemical name query:", value = "theobromine")

getMOl = RequestFromChEMBL()
 

if st.button("Search"):
    result = getMOl.nameToSMILES(search_query)
    st.write(result)

mol = Chem.MolFromSmiles(result)
if mol:
    st.write("Molecule found!")
    st.image(Chem.Draw.MolToImage(mol))