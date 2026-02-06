import requests

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
