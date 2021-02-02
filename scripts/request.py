import requests

def Run(Input):
    while (1):
        Input = input("root@Request: ")
        Response = requests.get(Input)
        print(Response.status_code)