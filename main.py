


import requests
from bs4 import BeautifulSoup

class CSGOStats:
    def __init__(self,name) -> None:
        self.name = name
        self.no_error = True

        headers = {
                'connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}

        try:
            url_for_id = f"https://steamid.io/lookup/{self.name}"
            site_resp = requests.get(url_for_id)
            soup_object = BeautifulSoup(site_resp.text, "lxml")
            steam_id_1 = soup_object.find_all("a")[-2].get("href")
                
            site_resp2 = requests.get(steam_id_1)
            soup_object2 = BeautifulSoup(site_resp2.text, "lxml")
            self.steam_id = soup_object2.find_all("img",{"class":"ext"})[0].get("data-clipboard-text")
            
            stats_url = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/overview"
            site_resp3 = requests.get(stats_url, headers=headers)
            soup_object3 = BeautifulSoup(site_resp3.text, "lxml")


            self.informations = {"avatar" : soup_object3.find_all("img", {"class":"ph-avatar__image"})[0].get("src"),
                                "kd" : soup_object3.find_all("span", {"class":"value"})[0].text,
                                "headshot" : soup_object3.find_all("span", {"class":"value"})[1].text,
                                "win" : soup_object3.find_all("span", {"class":"value"})[2].text,
                                "mvp" : soup_object3.find_all("span", {"class":"value"})[3].text,
                                "kill" : soup_object3.find_all("span", {"class":"value"})[4].text,
                                "deaths" : soup_object3.find_all("span", {"class":"value"})[5].text,
                                "headshot_nb" : soup_object3.find_all("span", {"class":"value"})[6].text,
                                "win_nb" : soup_object3.find_all("span", {"class":"value"})[7].text,
                                "losses_nb" : soup_object3.find_all("span", {"class":"value"})[8].text,
                                "score" : soup_object3.find_all("span", {"class":"value"})[9].text,
                                "damage" : soup_object3.find_all("span", {"class":"value"})[10].text,
                                "shotsAccuracy" : soup_object3.find_all("span", {"class":"value"})[11].text,
                                "bombsPlanted" : soup_object3.find_all("span", {"class":"value"})[12].text,
                                "bombsDefused" : soup_object3.find_all("span", {"class":"value"})[13].text,
                                "moneyEarned" : soup_object3.find_all("span", {"class":"value"})[14].text,
                                "hostageRescued" : soup_object3.find_all("span", {"class":"value"})[15].text}
        except:
            self.no_error = False




test = CSGOStats("Ritchi92")

if test.no_error:
    print(test.informations)
else:
    print("No information about this person")
