import requests

url = "http://127.0.0.1:8000/movie/create/"

payload="{\n    \"Name\" : \"Something\",\n    \"Relaese_date\" : \"17/02/22\"\n}\n"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)