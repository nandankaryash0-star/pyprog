def analyse_mood(text):
    print("----------AI FRIEND V-1.0----------")

    if "sad" in text or "tired" in text or "bad" in text:
        return f"I am sorry {user},That you are having an bad day, remember that not every day is same just keep moving"

    elif "good" in text or "great" in text or "amazing" in text:
        return f"It's greate {user}!!, I absolutely love hearing this. Keep that energy flowing!"

    else:
        return "I didn't quite catch that, but I'm listening."

user = input("Hi there ! What is your name ?")
text = input(f"Hello {user}. How are you feeling today ").lower()

bot_respond = analyse_mood(text)

print(bot_respond)