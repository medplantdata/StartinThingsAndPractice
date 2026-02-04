import requests


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

        # ABSOLUTELY NO r.json() HERE
        return r  # return the Response object itself