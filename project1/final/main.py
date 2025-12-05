# ============================================
# FILE 1: main.py
# ============================================
# Adventure Quest: The Lost Treasure
# Main game file - Run this file to start the game

from tkinter import *
from locations import get_location_info
from inventory import add_item, has_item, show_inventory
from puzzles import check_puzzle_answer, get_puzzle
from story import get_intro_story, get_victory_message, get_defeat_message, get_elder_dialogue

# Game Variables
player_name = ""
current_location = "forest"
inventory = []
game_progress = {
    "health": 100,
    "coins": 0,
    "puzzles_solved": []
}

# Create main window
window = Tk()
window.title("Adventure Quest: The Lost Treasure")
window.geometry("700x600")
window.config(bg="#2C3E50")

# Title Label
title_label = Label(window, text="🏰 Adventure Quest 🏰", 
                   font=("Arial", 24, "bold"), 
                   fg="#F39C12", bg="#2C3E50")
title_label.pack(pady=10)

# Story Display Area
story_frame = Frame(window, bg="#34495E", width=650, height=200)
story_frame.pack(pady=10)
story_frame.pack_propagate(False)

story_text = Label(story_frame, text="", font=("Arial", 11), 
                  fg="white", bg="#34495E", wraplength=620, justify=LEFT)
story_text.pack(pady=10, padx=10)

# Status Bar
status_frame = Frame(window, bg="#1ABC9C")
status_frame.pack(pady=5, fill=X)

health_label = Label(status_frame, text="❤️ Health: 100", 
                    font=("Arial", 10, "bold"), fg="white", bg="#1ABC9C")
health_label.pack(side=LEFT, padx=20)

coins_label = Label(status_frame, text="💰 Coins: 0", 
                   font=("Arial", 10, "bold"), fg="white", bg="#1ABC9C")
coins_label.pack(side=LEFT, padx=20)

location_label = Label(status_frame, text="📍 Location: Forest", 
                      font=("Arial", 10, "bold"), fg="white", bg="#1ABC9C")
location_label.pack(side=LEFT, padx=20)

# Inventory Display
inventory_label = Label(window, text="🎒 Inventory: Empty", 
                       font=("Arial", 10), fg="#F39C12", bg="#2C3E50")
inventory_label.pack(pady=5)

# Action Buttons Frame
button_frame = Frame(window, bg="#2C3E50")
button_frame.pack(pady=10)

# Functions
def start_game():
    global player_name
    player_name = name_entry.get()
    if player_name.strip() == "":
        player_name = "Adventurer"
    
    intro_story = get_intro_story(player_name)
    story_text.config(text=intro_story)
    
    start_button.pack_forget()
    name_entry.pack_forget()
    name_label.pack_forget()
    
    load_location("forest")
    save_game()

def load_location(location_name):
    global current_location
    current_location = location_name
    
    location_info = get_location_info(location_name)
    story_text.config(text=location_info["description"])
    location_label.config(text=f"📍 Location: {location_info['name']}")
    
    # Change background color based on location
    colors = {
        "forest": "#27AE60",
        "cave": "#34495E",
        "village": "#E67E22",
        "castle": "#8E44AD",
        "treasure_room": "#F39C12"
    }
    window.config(bg=colors.get(location_name, "#2C3E50"))
    story_frame.config(bg=colors.get(location_name, "#34495E"))
    
    # Clear old buttons
    for widget in button_frame.winfo_children():
        widget.destroy()
    
    # Create action buttons based on location
    if location_name == "forest":
        Button(button_frame, text="🔍 Search Area", width=15, 
               command=search_forest).pack(side=LEFT, padx=5)
        Button(button_frame, text="🚶 Go to Cave", width=15, 
               command=lambda: load_location("cave")).pack(side=LEFT, padx=5)
        Button(button_frame, text="🏘️ Go to Village", width=15, 
               command=lambda: load_location("village")).pack(side=LEFT, padx=5)
    
    elif location_name == "cave":
        Button(button_frame, text="🔦 Explore Cave", width=15, 
               command=explore_cave).pack(side=LEFT, padx=5)
        Button(button_frame, text="🔙 Back to Forest", width=15, 
               command=lambda: load_location("forest")).pack(side=LEFT, padx=5)
    
    elif location_name == "village":
        Button(button_frame, text="💬 Talk to Elder", width=15, 
               command=talk_to_elder).pack(side=LEFT, padx=5)
        Button(button_frame, text="🔙 Back to Forest", width=15, 
               command=lambda: load_location("forest")).pack(side=LEFT, padx=5)
        Button(button_frame, text="🏰 Go to Castle", width=15, 
               command=go_to_castle).pack(side=LEFT, padx=5)
    
    elif location_name == "castle":
        Button(button_frame, text="🗝️ Use Key", width=15, 
               command=unlock_castle).pack(side=LEFT, padx=5)
        Button(button_frame, text="🔙 Back to Village", width=15, 
               command=lambda: load_location("village")).pack(side=LEFT, padx=5)
    
    elif location_name == "treasure_room":
        Button(button_frame, text="🎉 Claim Treasure!", width=20, 
               command=win_game).pack(side=LEFT, padx=5)

def search_forest():
    if "map" not in inventory:
        inventory.append("map")
        inventory.append("sword")
        update_inventory_display()
        story_text.config(text="🗺️ You found a mysterious map and an old sword! The map shows a path to a hidden cave.")
        game_progress["coins"] += 10
        update_status()
        save_game()
    else:
        story_text.config(text="You've already searched this area. Nothing new here.")

def explore_cave():
    puzzle = get_puzzle("cave")
    story_text.config(text=puzzle["question"])
    
    # Create answer entry
    answer_entry = Entry(button_frame, font=("Arial", 12), width=20)
    answer_entry.pack(side=LEFT, padx=5)
    
    def check_answer():
        answer = answer_entry.get().lower()
        if check_puzzle_answer("cave", answer):
            inventory.append("golden_key")
            update_inventory_display()
            game_progress["puzzles_solved"].append("cave")
            game_progress["coins"] += 50
            update_status()
            story_text.config(text="✅ Correct! You found a GOLDEN KEY hidden in the cave! This must open something important.")
            save_game()
            answer_entry.destroy()
            check_btn.destroy()
        else:
            game_progress["health"] -= 10
            update_status()
            story_text.config(text="❌ Wrong answer! You triggered a trap and lost 10 health. Try again!")
    
    check_btn = Button(button_frame, text="Submit Answer", command=check_answer)
    check_btn.pack(side=LEFT, padx=5)

def talk_to_elder():
    dialogue = get_elder_dialogue(has_item(inventory, "golden_key"))
    story_text.config(text=dialogue)
    if has_item(inventory, "golden_key"):
        game_progress["coins"] += 100
        update_status()

def go_to_castle():
    if "golden_key" in inventory:
        load_location("castle")
    else:
        story_text.config(text="🚫 The path to the castle is blocked! The elder mentioned you need a golden key first.")

def unlock_castle():
    if "golden_key" in inventory:
        puzzle = get_puzzle("castle")
        story_text.config(text=puzzle["question"])
        
        answer_entry = Entry(button_frame, font=("Arial", 12), width=20)
        answer_entry.pack(side=LEFT, padx=5)
        
        def check_final_answer():
            answer = answer_entry.get().lower()
            if check_puzzle_answer("castle", answer):
                game_progress["puzzles_solved"].append("castle")
                save_game()
                load_location("treasure_room")
                answer_entry.destroy()
                check_btn.destroy()
            else:
                game_progress["health"] -= 20
                update_status()
                if game_progress["health"] <= 0:
                    game_over()
                else:
                    story_text.config(text="❌ Wrong! The guardian attacks! You lost 20 health. Think carefully!")
        
        check_btn = Button(button_frame, text="Submit Answer", command=check_final_answer)
        check_btn.pack(side=LEFT, padx=5)
    else:
        story_text.config(text="🔒 The castle door is locked! You need the golden key.")

def win_game():
    victory_msg = get_victory_message(player_name, game_progress["coins"])
    story_text.config(text=victory_msg)
    
    for widget in button_frame.winfo_children():
        widget.destroy()
    
    Button(button_frame, text="🎮 Play Again", width=15, 
           command=restart_game).pack(side=LEFT, padx=5)
    
    save_game()

def game_over():
    defeat_msg = get_defeat_message(player_name)
    story_text.config(text=defeat_msg)
    
    for widget in button_frame.winfo_children():
        widget.destroy()
    
    Button(button_frame, text="🔄 Try Again", width=15, 
           command=restart_game).pack(side=LEFT, padx=5)

def restart_game():
    global inventory, game_progress, current_location
    inventory = []
    game_progress = {"health": 100, "coins": 0, "puzzles_solved": []}
    current_location = "forest"
    update_status()
    update_inventory_display()
    load_location("forest")

def update_inventory_display():
    if len(inventory) == 0:
        inventory_label.config(text="🎒 Inventory: Empty")
    else:
        items = ", ".join(inventory)
        inventory_label.config(text=f"🎒 Inventory: {items}")

def update_status():
    health_label.config(text=f"❤️ Health: {game_progress['health']}")
    coins_label.config(text=f"💰 Coins: {game_progress['coins']}")

def save_game():
    try:
        with open("savegame.txt", "w") as f:
            f.write(f"Player: {player_name}\n")
            f.write(f"Location: {current_location}\n")
            f.write(f"Health: {game_progress['health']}\n")
            f.write(f"Coins: {game_progress['coins']}\n")
            f.write(f"Inventory: {','.join(inventory)}\n")
            f.write(f"Puzzles Solved: {','.join(game_progress['puzzles_solved'])}\n")
    except:
        pass

# Start Screen
name_label = Label(window, text="Enter Your Name:", font=("Arial", 12), 
                  fg="white", bg="#2C3E50")
name_label.pack(pady=10)

name_entry = Entry(window, font=("Arial", 14), width=25)
name_entry.pack(pady=5)

start_button = Button(window, text="⚔️ Start Adventure", font=("Arial", 12, "bold"), 
                     width=20, command=start_game, bg="#27AE60", fg="white")
start_button.pack(pady=10)

window.mainloop()