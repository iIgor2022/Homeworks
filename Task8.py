import requests
from pprint import pprint

heroes = ["Hulk", "Captain America", "Thanos"]

def SmartestHero(heroes_list):
    hero_dict = {}
    for hero in heroes_list:
        url = f"https://superheroapi.com/api/2619421814940190/search/{hero}"
        response = requests.get(url)
        hero_dict[response.json()["results"][0]["name"]] = response.json()["results"][0]["powerstats"]["intelligence"]
    hero_dict = dict(sorted(hero_dict.items()))
    return hero_dict


if __name__ == "__main__":
     pprint(SmartestHero(heroes))