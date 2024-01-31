import requests

response = requests.get("https://search.namu.wiki/api/ranking")

print(response.content.decode("utf-8"))