# FILE 5: story.py
# ============================================
# Story text and dialogue functions

def get_intro_story(player_name):
    story = f"""⚔️ Welcome, brave {player_name}! ⚔️

Long ago, the legendary King Aurelius hid a magnificent treasure 
somewhere in this kingdom before mysteriously disappearing.

Many have searched for it, but none have succeeded.

Your quest begins in the Enchanted Forest. 
Search carefully, solve ancient riddles, and prove your worth!

The treasure awaits those brave and clever enough to find it...

🗺️ Your adventure begins NOW! 🗺️"""
    return story

def get_victory_message(player_name, coins_collected):
    message = f"""🎉🎉🎉 CONGRATULATIONS {player_name.upper()}! 🎉🎉🎉

You've found the Lost Treasure of King Aurelius!

Your bravery and wisdom have been rewarded!

💰 Total Coins Collected: {coins_collected}
🏆 Status: LEGENDARY TREASURE HUNTER
⭐ Achievement Unlocked: Master Adventurer

The kingdom will remember your name forever!

Thank you for playing Adventure Quest! 🎮✨"""
    return message

def get_defeat_message(player_name):
    message = f"""💔 Oh no, {player_name}! 💔

Your health has dropped to zero...

The treasure remains hidden, waiting for another brave soul.

But don't give up! Every great adventurer faces challenges.

Try again and learn from your mistakes! 💪"""
    return message

def get_elder_dialogue(has_key):
    if has_key:
        return """👴 Elder: "Ah, the golden key! You're truly worthy!

The castle awaits you, brave one. But beware...
The final guardian tests not strength, but wisdom.

Here, take these coins for your journey. 
May fortune smile upon you!" """
    else:
        return """👴 Elder: "Welcome, young traveler!

You seek the Lost Treasure, don't you? 

Legend says it lies within the Ancient Castle,
but the castle doors are sealed by powerful magic.

Only the golden key, hidden deep in the Dark Cave,
can break the spell.

Many have tried... few have succeeded.
Will you be the one?" """