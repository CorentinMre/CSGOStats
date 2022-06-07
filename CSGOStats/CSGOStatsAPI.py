import requests
import urllib
from bs4 import BeautifulSoup
import re
import json

class CSGOStats:
    def __init__(self,name) -> None:
        self.name = name.replace(" ","+")

        self.headers = {
                'connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        
        ##########GET STEAM ID##########
        steam_url = f"https://steamcommunity.com/search/SearchCommunityAjax?text={self.name}&filter=users&sessionid=csgostats&steamid_user=false"
        site_resp = requests.get(steam_url,headers=self.headers,cookies={"sessionid":"csgostats"})
        soup_object = BeautifulSoup(site_resp.text, "lxml")
        self.steam_id = soup_object.find_all("a")[0].get("href").split("/")[-1][:-2]

        self.link = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/overview"
        self.url_overview = f"https://api.tracker.gg/api/v2/csgo/standard/profile/steam/{self.steam_id}"
        self.url_weapons = f"https://api.tracker.gg/api/v2/csgo/standard/profile/steam/{self.steam_id}/segments/weapon"
        self.url_maps = f"https://api.tracker.gg/api/v2/csgo/standard/profile/steam/{self.steam_id}/segments/map"

    def _get(self, url:str) -> dict:
        req = urllib.request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0')
        response = urllib.request.urlopen(req)
        assert not response.getcode() == 451, "The player either hasn't played CSGO or their profile is private."
        data = response.read()
        html = json.loads(data.decode('utf-8'))
        return html["data"]

    def refresh_informations_platformInfo(self) -> dict:
        """Refresh platform informations"""
        self.platformInfo = self._get(self.url_overview)["platformInfo"]


    def refresh_informations_overview(self) -> dict:
        """Refresh overview informations"""
        self.overview = self._get(self.url_overview)["segments"][0]["stats"]

    
    def refresh_informations_weapons(self) -> dict:
        """Refresh weapons informations"""
        self.weapons = self._get(self.url_weapons)

    def refresh_informations_maps(self) -> dict:
        """Refresh maps informations"""
        self.maps = self._get(self.url_maps)
    
    def refresh_all_informations(self) -> None:
        """Refresh all informations"""
        self.refresh_informations_platformInfo()
        self.refresh_informations_overview()
        self.refresh_informations_weapons()
        self.refresh_informations_maps()
    

"""

->self.platformInfo 
    Return platform informations

    dict with   'platformSlug'
                'platformUserId'
                'platformUserHandle'
                'platformUserIdentifier'
                'avatarUrl'


->self.overview
    Return overview informations

    dict with   'timePlayed'
                'score'
                'kills'
                'deaths'
                'kd'
                'damage'
                'headshots'
                'dominations'
                'shotsFired'
                'shotsHit'
                'shotsAccuracy'
                'snipersKilled'
                'dominationOverkills'
                'dominationRevenges'
                'bombsDefused'
                'moneyEarned'
                'hostagesRescued'
                'mvp'
                'wins'
                'ties'
                'matchesPlayed'
                'losses'
                'roundsPlayed'
                'roundsWon'
                'wlPercentage'
                'headshotPct'


->self.weapons
    Return weapons informations

    list of dict with 0
                      1
                      2
                      3
                      4...


->self.maps
    Return maps informations

    list of dict  0
                  1
                  2
                  3
                  4...
        
"""
if __name__ == "__main__":

    player = CSGOStats("footsx")
    player.refresh_all_informations()

    print(player.platformInfo)
    print(player.overview)
    print(player.weapons)
    print(player.maps)
