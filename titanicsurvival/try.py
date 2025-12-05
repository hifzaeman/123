import tkinter as tk
from tkinter import messagebox
import random

# Game state variables
game_state = {
    'rows': 4,
    'cols': 4,
    'card_values': ['🍎', '🍌', '🍇', '🍊', '🍓', '🍒', '🍉', '🍑'],
    'cards': [],
    'buttons': [],
    'revealed': [],
    'matched_pairs': [],
    'moves': 0,
    'pairs_found': 0,
    'first_card': None,
    'second_card': None,
    'can_click': True,
    'moves_label': None,
    'pairs_label': None,
    'root': None
}

def initialize_game(root):
    """Initialize the game with a shuffled deck"""
    game_state['root'] = root
    game_state['cards'] = game_state['card_values'] * 2
    random.shuffle(game_state['cards'])

def card_clicked(index):
    """Handle card click event"""
    # Prevent clicking if processing or card already revealed
    if not game_state['can_click'] or index in game_state['revealed'] or index in game_state['matched_pairs']:
        return
    
    # Reveal the card
    game_state['buttons'][index].config(
        text=game_state['cards'][index],
        bg="#3498db",
        fg="white"
    )
    game_state['revealed'].append(index)
    
    # First card clicked
    if game_state['first_card'] is None:
        game_state['first_card'] = index
    
    # Second card clicked
    elif game_state['second_card'] is None:
        game_state['second_card'] = index
        game_state['moves'] += 1
        game_state['moves_label'].config(text=f"Moves: {game_state['moves']}")
        game_state['can_click'] = False
        
        # Check for match after a short delay
        game_state['root'].after(1000, check_match)

def check_match():
    """Check if the two revealed cards match"""
    # Get the values of both cards
    first_value = game_state['cards'][game_state['first_card']]
    second_value = game_state['cards'][game_state['second_card']]
    
    if first_value == second_value:
        # Match found!
        game_state['buttons'][game_state['first_card']].config(bg="#2ecc71", state=tk.DISABLED)
        game_state['buttons'][game_state['second_card']].config(bg="#2ecc71", state=tk.DISABLED)
        game_state['matched_pairs'].extend([game_state['first_card'], game_state['second_card']])
        game_state['pairs_found'] += 1
        game_state['pairs_label'].config(text=f"Pairs: {game_state['pairs_found']}/8")
        
        # Check if game is won
        if game_state['pairs_found'] == 8:
            game_won()
    else:
        # No match - flip cards back
        game_state['buttons'][game_state['first_card']].config(text="?", bg="#95a5a6", fg="#2c3e50")
        game_state['buttons'][game_state['second_card']].config(text="?", bg="#95a5a6", fg="#2c3e50")
        game_state['revealed'].remove(game_state['first_card'])
        game_state['revealed'].remove(game_state['second_card'])
    
    # Reset for next turn
    game_state['first_card'] = None
    game_state['second_card'] = None
    game_state['can_click'] = True

def game_won():
    """Display win message"""
    messagebox.showinfo(
        "Congratulations! 🎉",
        f"You won!\n\nTotal Moves: {game_state['moves']}\n\nGreat job! 🌟"
    )

def restart_game():
    """Reset the game to initial state"""
    # Reset game state
    game_state['cards'] = game_state['card_values'] * 2
    random.shuffle(game_state['cards'])
    game_state['revealed'] = []
    game_state['matched_pairs'] = []
    game_state['moves'] = 0
    game_state['pairs_found'] = 0
    game_state['first_card'] = None
    game_state['second_card'] = None
    game_state['can_click'] = True
    
    # Reset UI
    game_state['moves_label'].config(text="Moves: 0")
    game_state['pairs_label'].config(text="Pairs: 0/8")
    
    # Reset all buttons
    for btn in game_state['buttons']:
        btn.config(
            text="?",
            bg="#95a5a6",
            fg="#2c3e50",
            state=tk.NORMAL
        )

def show_instructions():
    """Display game instructions"""
    instructions = """
🎯 HOW TO PLAY:

1. Click on any card to reveal it
2. Click on a second card to find its match
3. If the cards match, they stay revealed
4. If they don't match, they flip back
5. Find all 8 pairs to win!

💡 TIP: Try to remember where each 
symbol is located to make fewer moves!

Good luck! 🍀
    """
    messagebox.showinfo("How to Play", instructions)

def create_widgets(root):
    """Create all game widgets"""
    # Title
    title_frame = tk.Frame(root, bg="#34495e", pady=15)
    title_frame.pack(fill=tk.X)
    
    title_label = tk.Label(
        title_frame,
        text="🎮 Memory Card Game 🎮",
        font=("Arial", 18, "bold"),
        bg="#34495e",
        fg="#ecf0f1"
    )
    title_label.pack()
    
    # Info panel
    info_frame = tk.Frame(root, bg="#2c3e50", pady=10)
    info_frame.pack()
    
    game_state['moves_label'] = tk.Label(
        info_frame,
        text="Moves: 0",
        font=("Arial", 13, "bold"),
        bg="#2c3e50",
        fg="#3498db"
    )
    game_state['moves_label'].pack(side=tk.LEFT, padx=20)
    
    game_state['pairs_label'] = tk.Label(
        info_frame,
        text="Pairs: 0/8",
        font=("Arial", 13, "bold"),
        bg="#2c3e50",
        fg="#2ecc71"
    )
    game_state['pairs_label'].pack(side=tk.LEFT, padx=20)
    
    # Game board frame
    board_frame = tk.Frame(root, bg="#2c3e50")
    board_frame.pack(pady=20, expand=True)
    
    # Create card buttons
    button_index = 0
    for row in range(game_state['rows']):
        for col in range(game_state['cols']):
            btn = tk.Button(
                board_frame,
                text="?",
                font=("Arial", 28, "bold"),
                width=3,
                height=1,
                bg="#95a5a6",
                fg="#2c3e50",
                activebackground="#7f8c8d",
                cursor="hand2",
                relief=tk.RAISED,
                bd=3,
                command=lambda idx=button_index: card_clicked(idx)
            )
            btn.grid(row=row, column=col, padx=4, pady=4)
            game_state['buttons'].append(btn)
            button_index += 1
    
    # Control buttons frame
    control_frame = tk.Frame(root, bg="#2c3e50", pady=20)
    control_frame.pack()
    
    restart_btn = tk.Button(
        control_frame,
        text="🔄 New Game",
        font=("Arial", 14, "bold"),
        bg="#e74c3c",
        fg="white",
        activebackground="#c0392b",
        cursor="hand2",
        padx=20,
        pady=10,
        command=restart_game
    )
    restart_btn.pack(side=tk.LEFT, padx=10)
    
    instructions_btn = tk.Button(
        control_frame,
        text="❓ How to Play",
        font=("Arial", 14, "bold"),
        bg="#9b59b6",
        fg="white",
        activebackground="#8e44ad",
        cursor="hand2",
        padx=20,
        pady=10,
        command=show_instructions
    )
    instructions_btn.pack(side=tk.LEFT, padx=10)

def main():
    """Main function to run the game"""
    root = tk.Tk()
    root.title("Memory Card Game")
    root.geometry("600x600")
    root.configure(bg="#2c3e50")
    
    initialize_game(root)
    create_widgets(root)
    
    root.mainloop()

# Run the game
if __name__ == "__main__":
    main()
