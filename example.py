import CSGOStats


player = CSGOStats.CSGOStats("FootSX")
player.refresh_all_informations()

"""TO OPTIMIZE
#If you want to refresh informations

player.refresh_informations_platformInfo()
player.refresh_informations_overview()
player.refresh_informations_weapons()
player.refresh_informations_maps()

#Or more simply

player.refresh_all_informations()
"""

##########PlatformInfo##########
print("\n")
print("platformSlug: "+ player.platformInfo.platformSlug)
print("platformUserId: "+ player.platformInfo.platformUserId)
print("platformUserHandle: "+ player.platformInfo.platformUserHandle)
print("avatarUrl: "+ player.platformInfo.avatarUrl)


##########OVERVIEW##########
#value:str / category:str / name:str

print("\n")
print("Kd: " + player.overview.kd.value) # (value/category/name)
print("Play time: " + player.overview.timePlayed.value) # (value/category/name)
print("Matches number: " + player.overview.matchesPlayed.value) # (value/category/name)
print("Headshot %: " + player.overview.headshotPercentage.value) # (value/category/name)
print("Wins %: " + player.overview.winsPercentage.value) # (value/category/name)
print("MVP: " + player.overview.mvp.value) # (value/category/name)
print("Kills: " + player.overview.kills.value) # (value/category/name)
print("Deaths: " + player.overview.deaths.value) # (value/category/name)
print("Headshot number: " + player.overview.headshots.value) # (value/category/name)
print("Wins number: " + player.overview.wins.value) # (value/category/name)
print("Losses number: " + player.overview.losses.value) # (value/category/name)
print("Score: " + player.overview.score.value) # (value/category/name)
print("Damage: " + player.overview.damage.value) # (value/category/name)
print("Shots accuracy: " + player.overview.shotsAccuracy.value) # (value/category/name)
print("Bombs planted: " + player.overview.bombsPlanted.value) # (value/category/name)
print("Bombs defused: " + player.overview.bombsDefused.value) # (value/category/name)
print("Money earned: " + player.overview.moneyEarned.value) # (value/category/name)
print("Hostage rescued: "+ player.overview.hostagesRescued.value) # (value/category/name)

##########WEAPONS##########
print("\n\n")
print("Type: " + player.weapons[0].type)
print("Category: " + player.weapons[0].category)
print("Weapon url: " + player.weapons[0].imageUrl)
print("Weapon name: " + player.weapons[0].name)
print("Kills: " + player.weapons[0].kills)
print("Shots fired: " + player.weapons[0].shotsFired)
print("Shots hit: " + player.weapons[0].shotsHit)
print("Shots accuracy: " + player.weapons[0].shotsAccuracy)


##########MAPS##########
print("\n\n")
print("Type: " + player.maps[0].type)
print("Map url: " + player.maps[0].imageUrl)
print("Map name: " + player.maps[0].name)
print("Wins: " + player.maps[0].wins)
print("Rounds: " + player.maps[0].rounds)


##########OTHER##########
print("\n\n")
print("Link for more informations: " + player.link)
