
from CSGOStats import CSGOStats


test = CSGOStats("FootSX")


##########OVERVIEW##########
print("\n")
print("Kd: "+test.informations_overview["kd"])
print("Headshot: "+test.informations_overview["headshot"])
print("Wins: "+test.informations_overview["win"])
print("MVP: "+test.informations_overview["mvp"])
print("Kill: "+test.informations_overview["kill"])
print("Deaths: "+test.informations_overview["deaths"])
print("Headshot number: "+test.informations_overview["headshot_nb"])
print("Wins number: "+test.informations_overview["win_nb"])
print("Losses number: "+test.informations_overview["losses_nb"])
print("Score: "+test.informations_overview["score"])
print("Damage: "+test.informations_overview["damage"])
print("Shots accuracy: "+test.informations_overview["shotsAccuracy"])
print("Bombs planted: "+test.informations_overview["bombsPlanted"])
print("Bombs defused: "+test.informations_overview["bombsDefused"])
print("Money earned: "+test.informations_overview["moneyEarned"])
print("Hostage rescued: "+test.informations_overview["hostageRescued"])


##########WEAPONS##########
print("\n\n")
print("Url icon weapon: "+test.informations_weapons["AK-47"]["Icons"])
print("Name of weapon: "+test.informations_weapons["AK-47"]["Weapon"])
print("Kills: "+test.informations_weapons["AK-47"]["KillsShots"])
print("Fired shots: "+test.informations_weapons["AK-47"]["FiredShots"])
print("Hit shots: "+test.informations_weapons["AK-47"]["HitShots"])
print("Accuracy: "+test.informations_weapons["AK-47"]["Accuracy"])


##########MAPS##########
print("\n\n")
print("Url icon map: "+test.informations_maps["Lake"]["Icons"])
print("Name of map: "+test.informations_maps["Lake"]["Map"])
print("Wins: "+test.informations_maps["Lake"]["Wins"])
print("Rounds: "+test.informations_maps["Lake"]["Rounds"])
