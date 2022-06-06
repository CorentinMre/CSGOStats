
import CSGOStats


player = CSGOStats.CSGOStats("FootSX")
player.refresh_all_informations()

"""TO OPTIMIZE
#If you want to refresh informations

player.refresh_informations_overview()
player.refresh_informations_weapons()
player.refresh_informations_maps()

#Or more simply

player.refresh_all_informations()
"""

##########OVERVIEW##########
print("\n")
print("Kd: "+player.informations_overview["kd"])
print("Headshot: "+player.informations_overview["headshot"])
print("Wins: "+player.informations_overview["win"])
print("MVP: "+player.informations_overview["mvp"])
print("Kill: "+player.informations_overview["kill"])
print("Deaths: "+player.informations_overview["deaths"])
print("Headshot number: "+player.informations_overview["headshot_nb"])
print("Wins number: "+player.informations_overview["win_nb"])
print("Losses number: "+player.informations_overview["losses_nb"])
print("Score: "+player.informations_overview["score"])
print("Damage: "+player.informations_overview["damage"])
print("Shots accuracy: "+player.informations_overview["shotsAccuracy"])
print("Bombs planted: "+player.informations_overview["bombsPlanted"])
print("Bombs defused: "+player.informations_overview["bombsDefused"])
print("Money earned: "+player.informations_overview["moneyEarned"])
print("Hostage rescued: "+player.informations_overview["hostageRescued"])


##########WEAPONS##########
print("\n\n")
print("Url icon weapon: "+player.informations_weapons["AK-47"]["Icons"])
print("Name of weapon: "+player.informations_weapons["AK-47"]["Weapon"])
print("Kills: "+player.informations_weapons["AK-47"]["KillsShots"])
print("Fired shots: "+player.informations_weapons["AK-47"]["FiredShots"])
print("Hit shots: "+player.informations_weapons["AK-47"]["HitShots"])
print("Accuracy: "+player.informations_weapons["AK-47"]["Accuracy"])


##########MAPS##########
print("\n\n")
print("Url icon map: "+player.informations_maps["Lake"]["Icons"])
print("Name of map: "+player.informations_maps["Lake"]["Map"])
print("Wins: "+player.informations_maps["Lake"]["Wins"])
print("Rounds: "+player.informations_maps["Lake"]["Rounds"])