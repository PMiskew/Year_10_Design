import requests

url = "https://rapidapi.p.rapidapi.com/api/v2.0/fixtures/11867339"

querystring = {"include":"lineup.player","tz":"Europe/Amsterdam"}

headers = {
    'x-rapidapi-host': "football-pro.p.rapidapi.com",
    'x-rapidapi-key': "51507cb5fcmsh4a3e9775685c3f9p1e9bb3jsnb9e1628e4ed0"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)