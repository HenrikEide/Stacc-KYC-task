import requests

def pep_check(name):
    hit = requests.request("GET", f"https://stacc-code-challenge-2021.azurewebsites.net/api/pep?name={name}").json()
    if hit["numberOfHits"] == 0:
        return "Not a PEP"
    else:
        return "PEP, flag for manual processing"