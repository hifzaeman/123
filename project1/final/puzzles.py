# ============================================
# FILE 4: puzzles.py
# ============================================
# Puzzle and riddle functions

puzzles = {
    "cave": {
        "question": "🧩 RIDDLE: I speak without a mouth and hear without ears. I have no body, but come alive with wind. What am I?",
        "answer": "echo",
        "hint": "Think about sounds in a cave..."
    },
    "castle": {
        "question": "🧩 FINAL CHALLENGE: The more you take, the more you leave behind. What am I?",
        "answer": "footsteps",
        "hint": "Think about what you create when you walk..."
    }
}

def get_puzzle(location):
    return puzzles.get(location, {
        "question": "No puzzle here!",
        "answer": "",
        "hint": "Nothing to solve."
    })

def check_puzzle_answer(location, user_answer):
    puzzle = puzzles.get(location)
    if puzzle:
        correct_answer = puzzle["answer"].lower()
        user_answer = user_answer.lower().strip()
        return user_answer == correct_answer
    return False