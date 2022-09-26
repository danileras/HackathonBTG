import json
import requests
import urllib3


def buscadados(url):
    requests.packages.urllib3.disable_warnings()
    requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    try:
        requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'
    except AttributeError:
        # no pyopenssl support used / needed / available
        pass

    response = requests.get(url, verify=False)
    j = json.loads(response.content)
    print("Tipos de contas disponiveis nesse banco")
    for i in j['data']['brand']['companies']:
        for k in i['personalAccounts']:
            type = k['type']
            type = type.replace("_", " ")
            print(type.title())
