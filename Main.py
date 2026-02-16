#import streamlit as st
#import streamlit.components.v1 as components
#from TestFunctions import RequestFromCoconut 
from TestFunctions import RequestFromChEMBL
#from rdkit import Chem
#from rdkit.Chem import Draw
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Query(BaseModel):
    q: str

@app.post("/api/search-np")
def search_NP(body: Query):
    getMOl = RequestFromChEMBL()
    result = getMOl.nameToSMILES(body.q)
    return result



"""search_query = st.text_input("Enter your chemical name query:", value = "theobromine")

getMOl = RequestFromChEMBL()
 

if st.button("Search"):
    result = getMOl.nameToSMILES(search_query)
    st.write(result)

mol = Chem.MolFromSmiles(result)
if mol:
    st.write("Molecule found!")
    st.image(Chem.Draw.MolToImage(mol))"""