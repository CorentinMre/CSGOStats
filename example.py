
from CSGOStats import CSGOStats


test = CSGOStats("footsx")

if test.no_error:
        print(test.informations_overview)
        print(test.informations_weapons)
        print(test.informations_maps)
else:
    print("No information about this person")