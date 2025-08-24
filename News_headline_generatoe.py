# A fun News Headline Generator

# This program generates random and humorous news headlines by combining
import random

# lists of subjects, actions, and places/things.
subject = ["Shah Rukh Khan",
           "Nirmala Sitharaman",
           "Virat Kohli",
           "Narendra Modi",
           "Rohit",
           "Aman",
           "Elon Musk",
           "Jeff Bezos",]

action = ["launches",
"Dances with",
"eats",
"cancels",
"orders",
"clebrates",
"declaer war on",
"buys",]

place_or_things = ["at India gate",
                   "at ganga ghat",
                   "a plate samosha",
                   "in mubai local train",
                   "in red fort",
                   "during IPL match",
                   "inside parliament house",
                   "in space",]

# Start of the program
while True:
    Subject = random.choice(subject)
    Action = random.choice(action)  
    Place_or_things = random.choice(place_or_things)

    headline = f"Breaking News: {Subject} {Action} {Place_or_things}"
    print("\n" + headline)

# Ask if the user wants to generate another headline
    again = input("\nDo you want to generate another headline? (yes/no): ").strip()
    if again.lower() == "no":
        break

print("\nThank you for using the fun News Headline Generator!")
# End of the program
