import tkinter as tk
import requests
import json
from pprint import pprint

resp = requests.get("https://api.nasa.gov/planetary/apod?date=2020-09-09&api_key=DEMO_KEY")

data = resp.json()
pprint(data)
