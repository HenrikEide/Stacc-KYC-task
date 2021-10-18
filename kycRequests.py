import requests

def pep_check(name):
    hit = requests.request("GET", f"https://stacc-code-challenge-2021.azurewebsites.net/api/pep?name={name}").json()
    if hit["numberOfHits"] == 0:
        return f"{name} is not a PEP"
    else:
        return f"{name} is a PEP, flag for manual processing"

def pep_check_company(orgNr):
    hit = requests.request("GET", f"https://stacc-code-challenge-2021.azurewebsites.net/api/roller?orgNr={orgNr}").json()
    if type(hit)!=list:
        return "Error: Invalid company or invalid request"
    employees = []
    for section in hit:
        for rolle in section["roller"]:
            employees.append(f'{rolle["person"]["navn"]["fornavn"]} {rolle["person"]["navn"]["etternavn"]}')

    return ", ".join(list(map(pep_check, employees)))



# Testing
if __name__=="__main__":
    # hit = requests.request("GET", "https://stacc-code-challenge-2021.azurewebsites.net/api/roller?orgNr=988971375").json()
    # employees = []
    # for section in hit:
    #     for rolle in section["roller"]:
    #         employees.append(f'{rolle["person"]["navn"]["fornavn"]} {rolle["person"]["navn"]["etternavn"]}')
    # print(list(map(pep_check, employees)))

    # Test, currently on Stacc:
    orgNr = 988971375
    print(pep_check_company(orgNr))