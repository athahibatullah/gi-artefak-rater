import json

class Artifact:
    def __init__(self, set, piece, rarity, main_stat, lvl, sub):
        self.set = set
        self.piece = piece
        self.rarity = rarity
        self.main_stat = main_stat
        self.lvl = lvl
        self.sub = sub

substat_json = open("substat_list.json")
artifact_json = open("Artifact_list.json")
data_substat = json.loads(substat_json.read())
data_artifact = json.loads(artifact_json.read())

# Substat = Artifact(0,0,0,0,0,[data['Bloodstained Chivalry']['Flower'],data['Bloodstained Chivalry']['Feather'],data['Bloodstained Chivalry']['Eon'],data['Bloodstained Chivalry']['Goblet'],data['Bloodstained Chivalry']['Circlet']])
# Substat = Artifact(0,0,0,0,0,data_substat['Ampas']['HP'][5])

def Rate(lvl, rarity, main_stat, sub):
    score = 0
    tier = ['Bagus','Copium','Ampas']
    for i in range(4):
        for j in range(3):
            if(sub[i][1] > data_substat[tier[1]][sub[i][0]][int(lvl/4)]['value'] and sub[i][1] <= data_substat[tier[0]][sub[i][0]][int(lvl/4)]['value']):
                score += 3
            elif(sub[i][1] > data_substat[tier[2]][sub[i][0]][int(lvl/4)]['value'] and sub[i][1] <= data_substat[tier[1]][sub[i][0]][int(lvl/4)]['value']):
                score += 2
            elif(sub[i][1] <= data_substat[tier[2]][sub[i][0]][int(lvl/4)]['value']):
                score += 1
            print(sub[i][1], score)
            break
    return score

print("Total skor: " + str(Rate(20, 5, 'HP', [['ATK', 18], ['CR', 0.117], ['CDM', 0.225], ['HP', 0.058]])))
# print(data_substat['Ampas']['HP']['enchant_lvl'])
# print(Rate(20, 5, 'HP', [['ATK', 18], ['CR', 0.117], ['CDM', 0.225], ['HP', 0.058]]))
# print(Substat.sub)