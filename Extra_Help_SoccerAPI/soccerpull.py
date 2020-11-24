import http.client

conn = http.client.HTTPSConnection("football-pro.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "51507cb5fcmsh4a3e9775685c3f9p1e9bb3jsnb9e1628e4ed0",
    'x-rapidapi-host': "football-pro.p.rapidapi.com"
    }

conn.request("GET", "/api/v2.0/fixtures/11867339?include=lineup.player&tz=Europe%2FAmsterdam", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))