from neo4j import GraphDatabase
from TestFunctions import RequestFromChEMBLPYTHON

uri = "bolt://localhost:7687"
user = "neo4j"
password = "123456789"

driver = GraphDatabase.driver(uri, auth=(user, password))

tg = RequestFromChEMBLPYTHON()
ligands = tg.targetIDtoCompoundList("CHEMBL220", limit=20)
print(ligands)


query = """
UNWIND $rows AS row
MERGE (m:Molecule {chembl_id: row.chembl_id})
  ON CREATE SET
    m.name   = row.name,
    m.smiles = row.smiles

MERGE (t:Target {chembl_id: $target_id})
  ON CREATE SET
    t.name = $target_name

MERGE (m)-[r:BINDS_TO]->(t)
  ON CREATE SET
    r.interaction_type = "BINDING"
"""

with driver.session() as session:
    result = session.run(query,rows=ligands, target_id="CHEMBL220", target_name="Acetylcholine receptor")
    for record in result:
        print(record)