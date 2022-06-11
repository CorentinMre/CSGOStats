"""
To use:
        CSGOStats.platformInfo
        CSGOStats.overview
        CSGOStats.weapons
        CSGOStats.maps
"""

import requests
from bs4 import BeautifulSoup
from json import loads

class CSGOStats:
    def __init__(self, name, apiKey = None) -> None:
        self.name = name
        self.nameForSteam = self.name.replace(" ","+")

        self.apiKey = apiKey

        

        ##########GET STEAM ID##########
        steam_url = f"https://steamcommunity.com/search/SearchCommunityAjax?text={self.nameForSteam}&filter=users&sessionid=csgostats&steamid_user=false"
        req = self._get(steam_url, True, {"sessionid": "csgostats"})
        soup_object = BeautifulSoup(req, "lxml")
        self.steam_id = soup_object.find_all("a")[0].get("href").split("/")[-1][:-2]

        if self.apiKey is None: 
            self.urlhost = "api.tracker.gg/api"
            self.trackerParams = "?" + self._get_tracker_params(f"https://{self.urlhost}/v2/csgo/standard/profile/steam/{self.steam_id}")
        else: 
            self.urlhost = "public-api.tracker.gg"
            self.trackerParams = ""

        self.link = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/overview"
        self.url_overview = f"http://{self.urlhost}/v2/csgo/standard/profile/steam/{self.steam_id}{self.trackerParams}"
        self.url_weapons = f"http://{self.urlhost}/v2/csgo/standard/profile/steam/{self.steam_id}/segments/weapon{self.trackerParams}"
        self.url_maps = f"http://{self.urlhost}/v2/csgo/standard/profile/steam/{self.steam_id}/segments/map{self.trackerParams}"

        
    def _get_tracker_params(self, url:str) -> str:
        req = requests.get(url)
        return BeautifulSoup(req.text, "lxml").find("form",{"class":"challenge-form managed-form"}).get("action").split("?")[-1]

    def _get(self, url:str, steam:bool = False, cookies:dict = None) -> None:
        if self.apiKey is None: req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'},cookies=cookies)
        else: req = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0', "TRN-Api-Key":self.apiKey},cookies=cookies)
        assert not req.status_code == 451, "The player either hasn't played CSGO or their profile is private."
        assert not req.status_code == 403, "Access to the api is denied"
        if steam: return req.text
        else:
            if list(loads(req.text).keys())[0] == 'message': raise Exception("API rate limit exceeded")
            else: return loads(req.text)



    def refresh_informations_profil(self) -> None:
        """Refresh overview informations"""
        data = self._get(self.url_overview)
        self.overview = Overview(data["data"]["segments"][0]["stats"])
        self.platformInfo = PlatformInfo(data["data"]["platformInfo"])

    def refresh_informations_weapons(self) -> None:
        """Refresh weapons informations"""
        self.weapons = []
        weapons_temp = self._get(self.url_weapons)["data"]
        for i in range(len(weapons_temp)):
            self.weapons.append(Weapons(weapons_temp[i]))

    def refresh_informations_maps(self) -> None:
        """Refresh maps informations"""
        self.maps = []
        maps_temp = self._get(self.url_maps)["data"]
        for i in range(len(maps_temp)):
            self.maps.append(Maps(maps_temp[i]))
    
    def refresh_all_informations(self) -> None:
        """Refresh all informations"""
        self.refresh_informations_profil()
        self.refresh_informations_weapons()
        self.refresh_informations_maps()
    

class PlatformInfo:
    def __init__(self,data:dict) -> None:
        self.platformSlug = data["platformSlug"]
        self.platformUserId = data["platformUserId"]
        self.platformUserHandle = data["platformUserHandle"]
        self.avatarUrl = data["avatarUrl"]

class Values:
    def __init__(self,data:dict) -> None:
        self.percentile = data["percentile"]
        self.name = data["displayName"]
        self.category = data["displayCategory"]
        self.value = data["displayValue"]

class Overview:
    def __init__(self, data:dict) -> None:
        self.timePlayed = Values(data["timePlayed"])
        self.score = Values(data["score"])
        self.kills = Values(data["kills"])
        self.deaths = Values(data["deaths"])
        self.kd = Values(data["kd"])
        self.damage = Values(data["damage"])
        self.headshots = Values(data["headshots"])
        self.dominations = Values(data["dominations"])
        self.shotsFired = Values(data["shotsFired"])
        self.shotsHit = Values(data["shotsHit"])
        self.shotsAccuracy = Values(data["shotsAccuracy"])
        self.snipersKilled = Values(data["snipersKilled"])
        self.dominationOverkills = Values(data["dominationOverkills"])
        self.dominationRevenges = Values(data["dominationRevenges"])
        self.bombsPlanted = Values(data["bombsPlanted"])
        self.bombsDefused = Values(data["bombsDefused"])
        self.moneyEarned = Values(data["moneyEarned"])
        self.hostagesRescued = Values(data["hostagesRescued"])
        self.mvp = Values(data["mvp"])
        self.wins = Values(data["wins"])
        self.ties = Values(data["ties"])
        self.matchesPlayed = Values(data["matchesPlayed"])
        self.losses = Values(data["losses"])
        self.roundsPlayed = Values(data["roundsPlayed"])
        self.roundsWon = Values(data["roundsWon"])
        self.winsPercentage = Values(data["wlPercentage"])
        self.headshotPercentage = Values(data["headshotPct"])

class Weapons:
    def __init__(self,data:dict) -> None:
        self.type = data["type"]
        self.attributes = data["attributes"]
        self.name = data["metadata"]["name"]
        self.imageUrl = data["metadata"]["imageUrl"]
        self.category = data["metadata"]["category"]
        self.kills = data["stats"]["kills"]["displayValue"]
        self.shotsFired = data["stats"]["shotsFired"]["displayValue"]
        self.shotsHit = data["stats"]["shotsHit"]["displayValue"]
        self.shotsAccuracy = data["stats"]["shotsAccuracy"]["displayValue"]

class Maps:
    def __init__(self, data:dict) -> None:
        self.type = data["type"]
        self.attributes = data["attributes"]
        self.name = data["metadata"]["name"]
        self.imageUrl = data["metadata"]["imageUrl"]
        self.rounds = data["stats"]["rounds"]["displayValue"]
        self.wins = data["stats"]["wins"]["displayValue"]


if __name__ == "__main__":

    player = CSGOStats("Ritchi92")
    player.refresh_all_informations()


    print(player.overview.kd.value)
