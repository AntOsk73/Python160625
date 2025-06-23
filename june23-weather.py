# Weather check app

# Ask the user about the weather
weather = input("How's the weather today? (hot/cold/rainy): ").lower()

# Respond based on the input
if weather == "hot":
    print("Don't forget to drink some water, and hydrate yourself.")
elif weather == "cold":
    print("Stay warm and cozy and drink some soup!")
elif weather == "rainy":
    print("Take an umbrella with you to stay dry, althoug I hae umbrellas!")
else:
    print("Sorry, didn’t get your answer, please try again.")
