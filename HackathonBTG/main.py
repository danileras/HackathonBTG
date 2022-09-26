import requests
import json
import buscaAPI

print("-- ENCONTRANDO TIPOS DE CONTAS DE CADA BANCO -- ")


def buscaconta():
    url = "https://data.directory.openbankingbrasil.org.br/participants"
    rsp = requests.request("GET", url)
    final = 0
    response = rsp.content
    banco = str(input("Digite o nome do Banco :\n"))
    cont = 0
    links = []
    j = json.loads(response)

    for i in j:
        for k in i['AuthorisationServers']:
            for l in k['ApiResources']:
                if l['ApiFamilyType'] == 'products-services':
                    for m in l['ApiDiscoveryEndpoints']:
                        if 'personal-accounts' in m['ApiEndpoint']:
                            if banco.lower() in i['OrganisationName'].lower():
                                print(str(cont) + " - " + i['OrganisationName'] + " - " + k['CustomerFriendlyName'])
                                links.append(m['ApiEndpoint'])
                                costumerfriendlyname = k['CustomerFriendlyName']
                                cont += 1
    if cont < 1:
        print("Banco nao encontrado")
        buscaconta()
        final = 1
    if final != 1:
        num = int(input("Escolha o numero do banco: "))
        print("Indo para a api do " + costumerfriendlyname + ":\n" + links[num])
        print("\n\n\n\n\n\n")
        buscaAPI.buscadados(links[num])


buscaconta()
