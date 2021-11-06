import json

class Artifact:
    def __init__(self, set, piece, rarity, main_stat, lvl, sub):
        self.set = set
        self.piece = piece
        self.rarity = rarity
        self.main_stat = main_stat
        self.lvl = lvl
        self.sub = sub

# file_json = open("Artifact_list.json")
substat_json = open("substat_list.json")
artifact_json = open("Artifact_list.json")
data_substat = json.loads(substat_json.read())
data_artifact = json.loads(artifact_json.read())

# Substat = Artifact(0,0,0,0,0,[data['Bloodstained Chivalry']['Flower'],data['Bloodstained Chivalry']['Feather'],data['Bloodstained Chivalry']['Eon'],data['Bloodstained Chivalry']['Goblet'],data['Bloodstained Chivalry']['Circlet']])
# Substat = Artifact(0,0,0,0,0,data_substat['Ampas']['HP'][5])

print(Substat.sub)