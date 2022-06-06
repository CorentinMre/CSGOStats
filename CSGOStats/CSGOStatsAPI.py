
from unicodedata import category
import requests
from bs4 import BeautifulSoup


class CSGOStats:
    def __init__(self,name) -> None:
        self.name = name.replace(" ","+")
        self.no_error = True

        headers = {
                'connection': 'keep-alive',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0'}
        
        cookies = {
            "steamCountry":"FR|4a6494567bd2f9b6b4d15922b610cc9e",
            "steamMachineAuth76561199100442028":"365DCC0FE322A16D5A10272F5FF638FA8104776B",
            "timezoneOffset":"7200,0",
            "sessionid":"3ca004dbe6b357f4b5cea95e"
        }

        try:

            steam_url = f"https://steamcommunity.com/search/SearchCommunityAjax?text={self.name}&filter=users&sessionid=3ca004dbe6b357f4b5cea95e&steamid_user=false"
            site_resp = requests.get(steam_url,headers=headers,cookies=cookies)
            soup_object = BeautifulSoup(site_resp.text, "lxml")
            self.steam_id = soup_object.find_all("a")[0].get("href").split("/")[-1][:-2]

            #########OVERVIEW#########
            stats_url_overview = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/overview"
            site_resp_overview = requests.get(stats_url_overview, headers=headers)
            soup_object_overview = BeautifulSoup(site_resp_overview.text, "lxml")


            self.informations_overview = {"avatar" : soup_object_overview.find_all("img", {"class":"ph-avatar__image"})[0].get("src"),
                                "kd" : soup_object_overview.find_all("span", {"class":"value"})[0].text,
                                "headshot" : soup_object_overview.find_all("span", {"class":"value"})[1].text,
                                "win" : soup_object_overview.find_all("span", {"class":"value"})[2].text,
                                "mvp" : soup_object_overview.find_all("span", {"class":"value"})[3].text,
                                "kill" : soup_object_overview.find_all("span", {"class":"value"})[4].text,
                                "deaths" : soup_object_overview.find_all("span", {"class":"value"})[5].text,
                                "headshot_nb" : soup_object_overview.find_all("span", {"class":"value"})[6].text,
                                "win_nb" : soup_object_overview.find_all("span", {"class":"value"})[7].text,
                                "losses_nb" : soup_object_overview.find_all("span", {"class":"value"})[8].text,
                                "score" : soup_object_overview.find_all("span", {"class":"value"})[9].text,
                                "damage" : soup_object_overview.find_all("span", {"class":"value"})[10].text,
                                "shotsAccuracy" : soup_object_overview.find_all("span", {"class":"value"})[11].text,
                                "bombsPlanted" : soup_object_overview.find_all("span", {"class":"value"})[12].text,
                                "bombsDefused" : soup_object_overview.find_all("span", {"class":"value"})[13].text,
                                "moneyEarned" : soup_object_overview.find_all("span", {"class":"value"})[14].text,
                                "hostageRescued" : soup_object_overview.find_all("span", {"class":"value"})[15].text}

            #############Weapons#############
            stats_url_weapons = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/weapons"
            site_resp_weapons = requests.get(stats_url_weapons, headers=headers)
            soup_object_weapons = BeautifulSoup(site_resp_weapons.text, "lxml")
            nb_weapons = len(soup_object_weapons.find_all("tr"))
            self.informations_weapons = {}
            for i in range(nb_weapons -1):

                temp_weapons = {}
                temp_weapons["Icons"] = soup_object_weapons.find_all("tr")[i+1].find_all("img")[0].get("src")
                temp_weapons["Weapon"] = soup_object_weapons.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[0].text
                temp_weapons["KillsShots"] = soup_object_weapons.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[1].text
                temp_weapons["FiredShots"] = soup_object_weapons.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[2].text
                temp_weapons["HitShots"] = soup_object_weapons.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[3].text
                temp_weapons["Accuracy"] = soup_object_weapons.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[4].text
                self.informations_weapons[soup_object_weapons.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[0].text] = temp_weapons

            ###############MAPS##############
            stats_url_maps = f"https://tracker.gg/csgo/profile/steam/{self.steam_id}/maps"
            site_resp_maps = requests.get(stats_url_maps, headers=headers)
            soup_object_maps = BeautifulSoup(site_resp_maps.text, "lxml")
            nb_maps = len(soup_object_maps.find_all("tr"))
            self.informations_maps = {}
            for i in range(nb_maps -1):

                temp_maps = {}
                temp_maps["Icons"] = soup_object_maps.find_all("tr")[i+1].find_all("img")[0].get("src")
                temp_maps["Map"] = soup_object_maps.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[0].text
                temp_maps["Wins"] = soup_object_maps.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[1].text
                temp_maps["Rounds"] = soup_object_maps.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[2].text
                self.informations_maps[soup_object_maps.find_all("tr")[i+1].find_all("span", {"class":"segment-used__tp-name"})[0].text] = temp_maps

        
        except:
            self.no_error = False


if __name__ == "__main__":
    test = CSGOStats("footsx")
    if test.no_error:
        print(test.informations_overview)
        print(test.informations_weapons)
        print(test.informations_maps)
    else:
        print("No information about this person")