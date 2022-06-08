"""
To use:
        CSGOStatsplatformInfo
        CSGOStats.overview
        CSGOStats.weapons
        CSGOStats.maps

"""

import urllib
from bs4 import BeautifulSoup
import json

class CSGOStats:
    def __init__(self,name) -> None:
        self.name = name.replace(" ","+")

        self.headers = {
                'connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        
        ##########GET STEAM ID##########
        steam_url = f"https://steamcommunity.com/search/SearchCommunityAjax?text={self.name}&filter=users&sessionid=csgostats&steamid_user=false"
        req = self._get(steam_url, True)
        soup_object = BeautifulSoup(req, "lxml")
        self.steam_id = soup_object.find_all("a")[0].get("href").split("/")[-1][:-2]

        self.link = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/overview"
        self.url_overview = f"https://api.tracker.gg/api/v2/csgo/standard/profile/steam/{self.steam_id}"
        self.url_weapons = f"https://api.tracker.gg/api/v2/csgo/standard/profile/steam/{self.steam_id}/segments/weapon"
        self.url_maps = f"https://api.tracker.gg/api/v2/csgo/standard/profile/steam/{self.steam_id}/segments/map"


    def _get(self, url:str, steam:bool = False) -> dict:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0')
        req.add_header("Cookie", "sessionid=csgostats")
        response = urllib.request.urlopen(req)
        assert not response.getcode() == 451, "The player either hasn't played CSGO or their profile is private."
        data = response.read()
        if steam:
            return data.decode("utf-8") 
        else: return  json.loads(data.decode('utf-8'))

    def refresh_informations_platformInfo(self) -> None:
        """Refresh platform informations"""
        self.platformInfo = PlatformInfo(self._get(self.url_overview)["data"]["platformInfo"])


    def refresh_informations_overview(self) -> None:
        """Refresh overview informations"""
        self.overview = Overview(self._get(self.url_overview)["data"]["segments"][0]["stats"])

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
        self.refresh_informations_platformInfo()
        self.refresh_informations_overview()
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
