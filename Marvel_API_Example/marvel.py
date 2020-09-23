#https://developer.marvel.com
#Author: Lynda Yearwood
#Modified By: Paul Miskew


import requests
import hashlib
import json

def getKeys():
	keys = open("../../API_Keys//marvelkey.txt", "r")
	publicKey = keys.readline().strip()
	privateKey = keys.readline().strip()
	keys.close()
	key = [privateKey, publicKey]
	return key

def getHash(publicKey, privateKey):
	key = "1" + privateKey + publicKey
	result = hashlib.md5(key.encode()) #Don't expose private key
	return result.hexdigest()

key = getKeys()
publicKey = key[1]
result = getHash(key[1], key[0])

url = "https://gateway.marvel.com:443/v1/public/characters?name=hulk&ts=1&apikey="+publicKey+"&hash="+result
response = requests.get(url)
#print (response.text)

data = json.loads(response.text)
print (data['data']['results'][0]['name'])
print (data['data']['results'][0]['description'])

url = "https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=T&orderBy=name&ts=1&apikey="+publicKey+"&hash="+result
response = requests.get(url)
data = json.loads(response.text)

for character in data['data']['results']:
	print (character['name'])
	print (character['description'])
