import requests
import json
import webbrowser

def random_cat():
    """
    Have you had a long day of programming? Generate photos of random cats for morale.

    Parameters
    ----------
    None

    Returns
    -------
    Opens new web browser page with a photo of a random cat.

    Examples
    --------
    >>> from random_cat import random_cat
    >>> random_cat()
    ### opens url below, which is a random cat photo
    https://cdn2.thecatapi.com/images/PG-4j7axo.jpg
    """
    random_cat_req = requests.get('https://api.thecatapi.com/v1/images/search?api_key=live_BFqd62O18oeYqd4tUx9VsB2UCx9UdBYRI3rzNNMs8OANLZZSmeuTASxsatCGV2hk')
    random_cat_json = random_cat_req.json()
    url = random_cat_json[0]['url']
    return webbrowser.open(url)
