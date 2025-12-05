def add_item(inventory, item_name):
    if item_name not in inventory:
        inventory.append(item_name)
        return True
    return False

def remove_item(inventory, item_name):
    if item_name in inventory:
        inventory.remove(item_name)
        return True
    return False

def has_item(inventory, item_name):
    return item_name in inventory

def show_inventory(inventory):
    if len(inventory) == 0:
        return "Your inventory is empty."
    
    item_names = {
        "map": "🗺️ Ancient Map",
        "sword": "⚔️ Old Sword",
        "golden_key": "🗝️ Golden Key",
        "health_potion": "💊 Health Potion"
    }
    
    items_list = []
    for item in inventory:
        items_list.append(item_names.get(item, item))
    
    return "Your inventory:\n" + "\n".join(items_list)


