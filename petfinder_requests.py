from secrets import PETFINDER_API_TOKEN
import requests
from random import randrange

random_num = randrange(500)


def get_random_pet():
    resp = requests.get(
        "https://api.petfinder.com/v2/animals/",
        headers={'Authorization': f"Bearer {PETFINDER_API_TOKEN}"},
        params={"id": random_num}
    )
    name = resp.json()["animals"][0]["name"]
    age = resp.json()["animals"][0]["age"]
    if resp.json()["animals"][0]["photos"]:
        url = resp.json()["animals"][0]["photos"][0]["medium"]
    else:
        url = 'https://thecontemporarypet.com/wp-content/themes/contemporarypet/images/default.png'

    return [name, age, url]
