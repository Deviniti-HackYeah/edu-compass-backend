import requests
import json

# functions to get data from https://radon.nauka.gov.pl/opendata/polon/courses

baza = {}
szkoly = {}

def courses(token):
    url = "https://radon.nauka.gov.pl/opendata/polon/courses?resultNumbers=100"
    if (token != None):
        url = url + "&token=" + str(token)  

    response = requests.get(url)
    data = response.json()
    token = data["pagination"]["token"]
    for x in data["results"]:
        szkola = x["leadingInstitutionName"]
        for courseInstances in x["courseInstances"]:
            kierunek = courseInstances["courseName"]
            kierunki_w_szkole = []
            if (szkola in szkoly.keys()):
                kierunki_w_szkole = szkoly[szkola]
            if (not kierunek in kierunki_w_szkole):
                kierunki_w_szkole.append(kierunek)
            szkoly[szkola] = kierunki_w_szkole

            wydzialy = []
            if kierunek in baza.keys():
                wydzialy = baza[kierunek]

            c=0
            for wydzial in x["organizationalUnits"]:
                if (wydzial["organizationalUnitFullName"] != None):
                    nazwa = wydzial["organizationalUnitFullName"]
                    c =c + 1
                    if (not nazwa in wydzialy):
                        print("\t" + nazwa)
                        wydzialy.append(nazwa)  

            if (c == 0):
                if (not szkola in wydzialy):
                    wydzialy.append(szkola)

            baza[kierunek] = wydzialy
    return token




token  = None
i = 1   
while True:
    token = courses(token)

    with open("tmp/baza"+str(i)+".json", "w") as f:
      f.write(json.dumps(baza ))

    with open("tmp/szkoly"+str(i)+".json", "w") as f:
      f.write(json.dumps(szkoly ))

    i = i + 1