import requests
from chembl_webresource_client.new_client import new_client

class RequestFromChEMBLPYTHON:
    def __init__(self):
        self.molecule = new_client.molecule
        self.target = new_client.target
        self.activity = new_client.activity

    def targetIDtoCompoundList(self, target_id: str, limit: int = 20):
        activities = self.activity.filter(target_chembl_id=target_id,assay_type = "B").only('molecule_chembl_id')
        print('Number of activities:', len(activities))


        ligands = {}
        Ids = []
        seen = set()

        for a in activities:
            if a['molecule_chembl_id'] not in seen:
                seen.add(a['molecule_chembl_id'])
                Ids.append(a['molecule_chembl_id'])
            if len(Ids) >= limit:
                break
        
        for chembl_id in Ids:
            mols = self.molecule.filter(molecule_chembl_id=chembl_id).only(["molecule_chembl_id", "molecule_name", "molecule_structures"])
            for mol in mols:
                structures = mol.get("molecule_structures") or {}
                smiles = structures.get("canonical_smiles")
                if not smiles:
                    continue
                name = mol.get("molecule_name") or "Unknown"
                print(f"Processing {chembl_id}: {name}")
                ligands[chembl_id] = {
                    "name": name,
                    "smiles": smiles,
                }

        return [
            {"chembl_id": chembl_id, "name": data["name"], "smiles": data["smiles"]}
            for chembl_id, data in ligands.items()
        ]  


class RequestFromChEMBL:
    def __init__(self):
        self.baseURL = "https://www.ebi.ac.uk/chembl/api/data/molecule/search.json?q="

    def nameToSMILES(self, name: str):
        r = requests.get(self.baseURL + name)
        r.raise_for_status()
        data = r.json()
        return data["molecules"][0]["molecule_structures"]["canonical_smiles"]

class RequestFromCoconut:
    def __init__(self):
        self.baseURL = "https://coconut.naturalproducts.net/api/molecules/search"

    def searchMolecule(self, query: str):
        payload = {
            "search": {
                "scopes": [],
                "filters": [
                    {
                        "field": "name",
                        "operator": "=",
                        "value": query,
                    }
                ],
                "sorts": [{"field": "name", "direction": "asc"}],
                "selects": [
                    {"field": "standard_inchi"},
                    {"field": "standard_inchi_key"},
                    {"field": "canonical_smiles"},
                    {"field": "identifier"},
                    {"field": "name"},
                ],
                "includes": [{"relation": "properties"}],
                "aggregates": [],
                "instructions": [],
                "gates": ["create", "update", "delete"],
                "page": 1,
                "limit": 10,
            }
        }

        r = requests.post(self.baseURL, json=payload)

        # Do NOT parse JSON yet
        print("Status:", r.status_code)
        print("Content-Type:", r.headers.get("Content-Type"))
        print("Body snippet:", r.text[:500])

        return r.text  # just raw text for now

"""import requests

class RequestFromCoconut:
    def __init__(self):
       self.baseURL = 'https://coconut.naturalproducts.net/api/molecules/search'
       

    def searchMolecule(self, query: str):
        payload = {
            "search": {
                "scopes": [],
                "filters": [
                    # only filter on name; you can add others later
                    {
                        "field": "name",
                        "operator": "=",
                        "value": query,  # <— use the function argument
                    }
                ],
                "sorts": [
                    {"field": "name", "direction": "asc"}
                ],
                "selects": [
                    {"field": "standard_inchi"},
                    {"field": "standard_inchi_key"},
                    {"field": "canonical_smiles"},
                    {"field": "identifier"},
                    {"field": "name"},
                ],
                "includes": [{"relation": "properties"}],
                "aggregates": [],
                "instructions": [],
                "gates": ["create", "update", "delete"],
                "page": 1,
                "limit": 10,
            }
        }
        r = requests.post(self.baseURL, json = payload)
        r.raise_for_status()
        return r.json()"""
