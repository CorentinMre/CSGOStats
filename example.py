
from CSGOStats import CSGOStats


test = CSGOStats("Ritchi92")

if test.no_error:
    print(test.informations)
else:
    print("No information about this person")