import requests

# Master Duel specific API endpoint - need misc=yes to get md_rarity
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php?format=master%20duel&misc=yes"
response = requests.get(url)
data = response.json()

cards = []

for card in data["data"]:
    name = card["name"]
    
    # Master Duel rarity is in misc_info under "md_rarity"
    rarity = "N"
    if "misc_info" in card and card["misc_info"]:
        rarity = card["misc_info"][0].get("md_rarity", "N")
    
    # Normalize rarity codes (API returns full names like "Ultra Rare")
    if rarity == "Ultra Rare":
        rarity_code = "UR"
    elif rarity == "Super Rare":
        rarity_code = "SR"
    elif rarity == "Rare":
        rarity_code = "R"
    else:
        rarity_code = "N"
    
    cards.append((name, rarity_code))

# Sort alphabetically
cards.sort(key=lambda x: x[0])

with open("master_duel_cards.txt", "w", encoding="utf-8") as f:
    f.write("Begin\n\n")
    
    for name, rarity in cards:
        f.write(f"{name} | {rarity}\n")
    
    f.write("\nEND")

print("master_duel_cards.txt created with TRUE Master Duel rarities.")
