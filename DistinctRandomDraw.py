import random

rarity_pools = {"UR": [], "SR": [], "R": [], "N": []}

with open("master_duel_cards.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line or line in ["Begin", "END"]:
            continue
        
        name, rarity = line.rsplit("|", 1)
        rarity_pools[rarity.strip()].append(name.strip())

def draw_card():
    roll = random.random()
    
    if roll < 0.025:
        return random.choice(rarity_pools["UR"])
    elif roll < 0.10:
        return random.choice(rarity_pools["SR"])
    elif roll < 0.45:
        return random.choice(rarity_pools["R"])
    else:
        return random.choice(rarity_pools["N"])

drawn_cards = set()

while len(drawn_cards) < 100:
    drawn_cards.add(draw_card())

with open("DrawnCards.txt", "w", encoding="utf-8") as f:
    for card in sorted(drawn_cards):
        f.write(card + "\n")

print("100 DISTINCT cards drawn with rarity odds.")
