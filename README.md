<p align="center"><img width="250" alt="CSGO Statistics" src="img/icon.png"></p>
<p align="center"><strong>CSGO Statistics</strong>
<br/>


<h2 align="center">CSGO Statistics</h2>
<br/>

## Requirements

- Install requirements (`pip install -r requirements.txt`)

## Usage

Here is an example script:

```python
from CSGOStats import CSGOStats


player = CSGOStats("Ritchi92")

if player.no_error:
    print(player.informations)
else:
    print("No information about this person")
```