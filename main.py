from quotes import get_quote

print("Mood-Based Quote Generator ")
mood = input("How are you feeling? (happy, sad, stressed, motivated): ")

quote = get_quote(mood)
print("\n Here's a quote for you:")
print(quote)
