import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

users_params = {
    "token" : "kjiihioopkjoo2",
    "username" : "akstg24",
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

USERNAME = "akstg24"
TOKEN = "kjiihioopkjoo2"

# repsonse = requests.post(url= pixela_endpoint, json = users_params)
# print(repsonse.text)

graph_endpoint = f"https://pixe.la//v1/users/{USERNAME}/graphs"

#create graph
g_config = {
    "id" : "graph1",
    "name" : "course analyser",
    "unit" : "units",
    "type" : "int",
    "color": "sora"
}

headers = {"X-USER-TOKEN" : TOKEN}

# response1 = requests.post(url = graph_endpoint, json = g_config , headers = headers)
# print(response1.text)

pixel_post = f"{graph_endpoint}/graph1"

today = datetime.datetime.now()

#create a pixel
pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity" : str(input("Aaj kitna kie? "))
}

response2 = requests.post(url= pixel_post, json= pixel_config, headers=headers)
print(response2.text)
print(today.strftime("%Y%m%d"))
if response2.status_code==200:
    print("hogya bhai done")

#put request:
put_bruh = f"{pixel_post}/{today.strftime('%Y%m%d')}"
# response_put = requests.put(url=put_bruh,json={"quantity" : "1"}, headers=headers)
# print(response_put.text)

#delete request
delete_bruh = f"{pixel_post}/{today.strftime('%Y%m%d')}"

# response3 = requests.delete(url=delete_bruh, headers=headers)
# print(response3.text)