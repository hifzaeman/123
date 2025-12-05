locations = [
    ["forest", "Enchanted Forest", "🌲 You stand in a mysterious forest. Ancient trees tower above you. You hear strange sounds in the distance. There might be something useful hidden here..."],
    ["cave", "Dark Cave", "🕳️ A dark, damp cave stretches before you. Water drips from the ceiling. You see strange markings on the walls. This place guards secrets..."],
    ["village", "Peaceful Village", "🏘️ A small, friendly village welcomes you. The villagers seem to know about the legendary treasure. An old elder sits near the fountain, waiting to speak with travelers."],
    ["castle", "Ancient Castle", "🏰 A magnificent but abandoned castle looms before you. Its gates are locked with ancient magic. Only the pure of heart and sharp of mind can enter the treasure room."],
    ["treasure_room", "Treasure Room", "✨ The legendary treasure room! Golden light fills the chamber. Jewels, coins, and ancient artifacts are scattered everywhere. You've found the Lost Treasure!"]
]

def get_location_info(location_name):
    for location in locations:
        if location[0] == location_name:
            return {
                "id": location[0],
                "name": location[1],
                "description": location[2]
            }
    return {"id": "unknown", "name": "Unknown", "description": "You are lost..."}

def get_all_locations():
    return locations