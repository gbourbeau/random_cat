import requests
import json
import webbrowser

def test_random_cat():
    random_cat_req = requests.get('https://api.thecatapi.com/v1/images/search?api_key=live_BFqd62O18oeYqd4tUx9VsB2UCx9UdBYRI3rzNNMs8OANLZZSmeuTASxsatCGV2hk')
    random_cat_json = random_cat_req.json()
    url = random_cat_json[0]['url']
    test_return = webbrowser.open(url)
    assert test_return == True