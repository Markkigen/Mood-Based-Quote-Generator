import random

quotes = {
    "happy": [
        "Happiness is a direction, not a place.",
        "Smile, it's a free therapy.",
        "Joy is the simplest form of gratitude."
    ],
    "sad": [
        "Tough times never last, but tough people do.",
        "It's okay to not be okay.",
        "Every storm runs out of rain."
        "Everything will be okay"
        
    ],
    "stressed": [
        "Just breathe. You got this.",
        "Take it one step at a time.",
        "Let go of what you can’t control."
        "It will come to pass, Don't worry bro"
    ],
    "motivated": [
        "Push yourself, no one else will.",
        "You are capable of amazing things.",
        "Dream big. Work hard. Stay focused."
    ],
    "lonely": [
        "You're never as alone as you think.",
        "This moment will pass, and you'll grow stronger.",
        "Even the moon needs darkness to shine."
    ]
    
}

def get_quote(mood):
    mood = mood.lower().strip()
    if mood in quotes:
        return random.choice(quotes[mood])
    else:
        return "Sorry, I don't have quotes for that mood yet."

if __name__ == "__main__":
    user_mood = input("How are you feeling today? ")
    print(get_quote(user_mood))
