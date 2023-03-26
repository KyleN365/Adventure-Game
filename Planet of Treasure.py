#Kyle North
#03/21/2023

import time
import random


# function to wait for user to press Enter
def wait_for_enter():
    input("Press Enter to continue...")
    print("\n")

# function to get player's name
def get_player_name():
    name = input("Enter your name: ")
    return name

# function to print the opening scene
def print_opening_scene():
    print("\nAs you speed through the barren landscape, the wind howls in your ears, whipping your hair back and forth. The sun beats down on your face, making you squint against the glare. In the distance, you hear the faint sound of police sirens growing louder by the second. You check the readouts on your solar board sail, trying to eke out every last bit of speed. The gleaming surface of the sail catches the sunlight and reflects it back at you, almost blinding you.")
    time.sleep(2)
    print("\nAs you push your solar board sail to the limit, you realize with a sinking feeling that the police droids have caught up to you. They surround you on all sides, their red eyes glowing in the darkness. With no other options left, you allow them to apprehend you and bring you back to your mother's inn.")
    time.sleep(2)
    print("\nThe inn is a shadow of its former self, but it still bustles with activity. The sound of clinking dishes and chatter fills the air as you step inside. Your mother Ashley greets you with a mixture of relief and disappointment, but you can tell she's mostly just happy to have you back in one piece.")
    wait_for_enter()
    
# list of choices made by the player
choices_made = []

# function to display the choices
def display_choices():
    # available choices
    choices = {
        "1": "Start talking with customers in the dining area",
        "2": "Help your mum with chores",
        "3": "Go to your room",
        "4": "Sleep off this day"
    }

    # remove choices that have already been made
    for choice in choices_made:
        del choices[choice]

    # display available choices
    print("\nWhat do you want to do?")
    for choice, description in choices.items():
        print(f"{choice}. {description}")
    
    # get player's choice
    while True:
        choice = input("Enter your choice (1-4): ")
        if choice in choices:
            break
        print("Invalid choice. Please enter a valid option.")
    
    # add player's choice to list of choices made
    choices_made.append(choice)

    return choice

player_name = get_player_name()
print_opening_scene()

# function to handle choice 1
def handle_choice_1():
    print("\nYou walk past your mum and say, 'Maybe later,' as you enter the dimly lit dining area where three families and a family friend are eating at individual tables.")
    time.sleep(2)
    print("\nYou speak with each table about their stay and the food, and each replies with praise for the inn's excellent service. Finally, you reach the family friend Gilbert, who speaks of your amazing potential and tells you he would fund your entrance into school or help you make more of your potential.")
    wait_for_enter()
    save = {'choice': 1, 'result': 'Gilbert offers to fund your education or help you make more of your potential'}
    display_choices()
    return save

# function to handle choice 2
def handle_choice_2():
    print("\nYou brush past your mum and say, 'Maybe later. I need to be alone.' As you walk up the stairs, you can see the hurt in her face and ruminate on the grief you've caused her. You enter a small bedroom with only a bed and nightstand. Looking out the window at the night sky, you picture a better, more adventurous future.")
    wait_for_enter()
    display_choices()
    
# function to handle choice 3                   
def handle_choice_3():
    done_chores = []
    print("\nYou tell your mum you'll help with chores.")
    time.sleep(2)
    print("\nShe gives you three options: washing dishes, sweeping, or doing laundry.")
    
    # list of chores
    chores = ["dishes", "sweeping", "laundry"]
    
    for chore in chores:
        print("\nYou start doing {0}...".format(chore))
        time.sleep(2)
        done_chores.append(chore)
    
    print("\nYou've completed all the chores! Your mum looks pleased and says,")
    print("'Thank you so much for your help, {0}. You're such a responsible young adult now.'".format(player_name))
    wait_for_enter()
    display_choices()
    save = {'choice': 3, 'result': 'Completed all chores ({0})'.format(", ".join(done_chores))}
    return save

# function to handle choice 4  
def handle_choice_4():
    print("\nYou decide to sleep off the day and get some rest.")
    time.sleep(2)
    print("\nAs you drift off to sleep, you think about what tomorrow might bring.")
    time.sleep(2)
    print("\nChapter 1 is now complete. Press Enter to continue to Chapter 2.")
    wait_for_enter()

# loop through the choices until the player chooses to sleep
while True:
    choice = display_choices()
    if choice == "1":
        save = handle_choice_1()
    elif choice == "2":
        handle_choice_2()
    elif choice == "3":
        save = handle_choice_3()
    elif choice == "4":
        handle_choice_4()
    if len(choices_made) == 4:
        print("Congratulations, you have completed Chapter 1!")
        time.sleep(2)
        print("Press Enter to continue to Chapter 2.")
        wait_for_enter()
        break


# Chapter 2: The Escape
def start_chapter_2():
    print("You wake up to a loud noise and see a spacecraft crashing into the dock outside the inn. As you look closer, you see an alien survivor limping away from the crash site towards the inn. At the same time, a group of pirates descend in their ship.")

    choice = input("What do you want to do?\n1. Help the alien survivor escape\n2. Ignore the alien survivor and try to escape the pirates\n3. Wake everyone up and head downstairs\n4. Flee into the nearby town\nEnter your choice (1, 2, 3, or 4): ")


# function to handle choice 1
    if choice == "1":
        print("\nYou run towards the survivor of the crashed spacecraft.")
        time.sleep(2)
        print("\nThe survivor hands you a spherical map and warns you of the dangers of the pirates.")
        time.sleep(2)
        print("\nYou have a 90% chance of escaping the pirates if you listen to the survivor's warning.")
        escape_chance = random.randint(1, 10)
        if escape_chance <= 9:
            print("\nYou take the spherical map from the survivor and quickly follow their instructions.")
            time.sleep(2)
            print("\nAs you're running, you hear the sound of the pirate ship getting closer and closer.")
            time.sleep(2)
            print("\nYour heart races as you see the ship hovering above you, but you manage to escape just in time.")
            time.sleep(2)
            print("\nThe alien survivor thanks you for your help and gives you a reward before disappearing into the night.")
            wait_for_enter()
        else:
            print("\nYou ignore the survivor's warning and continue running in the opposite direction.")
            time.sleep(2)
            print("\nUnfortunately, you don't get far before you hear the sound of the pirate ship getting closer and closer.")
            time.sleep(2)
            print("\nThe pirates catch up to you and you're taken captive.")
            time.sleep(2)
            print("\nThe game ends with the player's capture and a brief description of what might have been.")
            wait_for_enter()

# function to handle choice 2
    if choice == "2":
        print("\nYou jump out of the window and run towards the survivor of the crashed spacecraft.")
        time.sleep(2)
        print("\nThe survivor hands you a spherical map and warns you of the dangers of the pirates.")
        time.sleep(2)
        choice = input("\nDo you listen to the survivor's warning? (Y/N): ")
        if choice == "Y":
            print("\nYou take the spherical map and quickly follow the survivor's instructions.")
            time.sleep(2)
            print("\nAs you're running, you hear the sound of the pirate ship getting closer and closer.")
            time.sleep(2)
            if random.random() < 0.9:
                print("\nYour heart races as you see the ship hovering above you, but you manage to escape just in time.")
                time.sleep(2)
                print("\nThe alien survivor thanks you for your help and gives you a reward before disappearing into the night.")
                wait_for_enter()

# function to handle choice 3
    if choice == "3":
        print("\nYou wake up everyone in the inn and head downstairs.")
        time.sleep(2)
        print("\nThere, you find the pirate who had crawled into the inn for assistance, but had died from his injuries.")
        time.sleep(2)
        print("\nYou see a spherical map in his hand and grab it, just as the pirate ship descends.")
        time.sleep(2)
        if random.random() < 0.5:
            print("\nYou quickly leave the inn and run as fast as you can.")
            time.sleep(2)
            print("\nAs you're running, you hear the sound of the pirate ship getting closer and closer.")
            time.sleep(2)
            if random.random() < 0.5:
                print("\nYour heart races as you see the ship hovering above you, but you manage to escape just in time.")
                time.sleep(2)
            else:
                print("\nUnfortunately, you're not fast enough. The pirates catch up to you and you're taken captive.")
                time.sleep(2)
                print("\nThe game ends with the player's capture and a brief description of what might have been.")
                wait_for_enter()
        else:
            print("\nYou try to run away from the pirate ship, but unfortunately, you're not fast enough.")
            time.sleep(2)
            print("\nThe pirates catch up to you and you're taken captive.")
            time.sleep(2)
            print("\nThe game ends with the player's capture and a brief description of what might have been.")
            wait_for_enter()

    elif choice == "4":
        print("You flee into the nearby town, leaving behind the chaos of the inn and the pirate attack.")
        time.sleep(2)
        print("\nThe game ends with a brief description of how the night lived with you forever, and how you built yourself a humdrum life, always feeling like you were meant for more.")
        wait_for_enter()


# call the function to start chapter 2
start_chapter_2()



# Chapter 3: Space Station

# Introduction
print("Chapter 3: Montressanaro Space Station\n")
print("You arrive at the grandiose Montressanaro space station, a bustling hub of activity where locals intermingle with various space crews.")
print("Massive solar sail ships loom in the distance as you disembark from the planetary transit ship.")


print("\nYou look around the station and see two ships available for purchase: a moderate ship, or a mediocre ship.")
ship_choice = input("Which ship do you want to lease? ").lower()
while ship_choice not in ["moderate ship", "mediocre ship"]:
    ship_choice = input("Invalid choice. Which ship do you want to purchase? ").lower()
ship = ship_choice

# Save ship choice to file
with open("ship_choice.txt", "w") as f:
    f.write(ship)

# Talk to merchants to obtain food and extra info about crews and ships
print("\nBefore leaving the station, you decide to talk to some merchants to obtain extra supplies and information about the crew and ship you've chosen.")
print("You learn that the Nirvana crew has a reputation for being reliable and efficient, while the Paramore crew is known for being unpredictable and untrustworthy.")
print(f"\nYou obtain enough food and supplies to last you until your next destination on the {ship}.")

# Meet with crew
print("\nYou walk to the local spaceport bar to meet with the available crews.")
print("Two crews stand out: Nirvana and Paramore.")
crew_choice = input("Which crew do you want to hire? ").lower()
while crew_choice not in ["nirvana", "paramore"]:
  crew_choice = input("Invalid choice. Which crew do you want to hire? ").lower()

# Choosing the cheapest crew results in the captain killing you
if crew_choice == "nirvana":
  crew = "Nirvana crew"
  print("\nThe Nirvana crew accepts your offer and you all board your new ship.")
else:
  print("\nThe Paramore crew agrees to your terms, but as you all prepare to leave the station, you realize too late that you made a grave mistake.")
  print("The captain of the Paramore crew turns out to be a wanted criminal and he kills you before you can leave the spaceport.")
  print("\n\nGame Over!")
  exit()

print("\n\nEnd of Chapter 3!")



# Chapter 4: The Black Hole

# Read ship choice from file
with open("ship_choice.txt", "r") as f:
    ship = f.read().strip()

# Function to save game progress
def save(key, value):
    with open("game_progress.txt", "a") as f:
        f.write(key + ":" + value + "\n")

# Introduction
print("Chapter 4: The Black Hole\n")
print("About a month into your voyage, things have been going smoothly until a catastrophic event occurs.")
if ship == "mediocre ship":
  print("The star Santrepida has collapsed in on itself, creating a black hole. Your ship is sucked in, and you are destroyed in the process.")
  print("\n\nGame Over!")
  exit()
else:
  print("The star Santrepida has collapsed in on itself, creating a black hole. You must act fast to avoid being sucked in.")
  print("\nYou manage to avoid the black hole's gravitational pull, but the ship is caught in a gravitational wave.")
  choice = input("Do you help or hide? ").lower()
  while choice not in ["help", "hide"]:
    choice = input("Invalid choice. Do you help or hide? ").lower()
  if choice == "help":
    print("\nYou quickly realize that the main solar sail has come loose and is flapping uncontrollably.")
    print("You work together with the first mate to untangle the life lines and unfurl the sail, catching the light and the gravitational wave.")
    print("The ship is pushed to safety and you have also saved the first mate's life, who is now indebted to you.")
    save("first mate", "alive")
  else:
    print("\nYou run below deck and cower during the storm.")
    print("Although your ship barely manages to survive, the life of your first mate was lost when his life line came loose.")
    save("first mate", "dead")

print("After surviving the event, some crew members reveal themselves as pirates and demand the map.")

# Check if first mate is saved
if "saved first mate" in choice:
  print("You and your first mate quickly jump into action, fighting off the pirates and securing the map.")
  roll = random.randint(1, 6)
  if roll <= 4:
    print("\nYou emerge victorious in the fight and the pirates are subdued.")
    choice = input("\nDo you want to give up and head back to Chapter 3 spaceport, or proceed to Chapter 5? ").lower()
    while choice not in ["give up", "head back", "proceed", "chapter 5"]:
      choice = input("Invalid choice. Do you want to give up and head back to Chapter 3 spaceport, or proceed to Chapter 5? ").lower()
    if choice in ["give up", "head back"]:
      print("\nYou decide to head back to Chapter 3 spaceport and rethink your plans.")
      save("chapter", 3)
      exit()
    else:
      print("\nYou continue on your journey to find the planet of treasure.")
      save("chapter", 5)
  else:
    print("\nDespite your best efforts, the pirates overpower you and take the map.")
    print("The ship is taken over and you are left stranded in the middle of space.")
    print("\n\nGame Over!")
    exit()
else:
  print("You try to fend off the pirates, but their numbers are too great and they overpower you.")
  print("Your ship is taken over, and you are left stranded in the middle of space.")
  print("\n\nGame Over!")
  exit()

print("\n\nEnd of Chapter 4!")

# Save ship choice to file
with open("ship_choice.txt", "w") as f:
    f.write(ship)



import random

print("After weeks of travel, you finally arrive at the fabled planet of treasure. You descend in a landing vessel to the planet's surface and begin exploring.")
chapter = choose_direction()

def choose_direction():
    directions = ['N', 'S', 'E', 'W']
    direction = input("Choose a direction to explore (N, S, E, W): ")
    
    while direction not in directions:
        direction = input("Invalid choice. Choose a direction to explore (N, S, E, W): ")
    
    if direction == 'W':
        print("As you travel west, you come across a large rusted robot. The robot appears to have been here for a long time. While you observe the large machine, you notice gears start turning and the lights behind the eyes illuminate.")
        print("The robot slowly turns to look at you.")
        choice = input("What do you want to do? Fight, flee, or bargain? ")
        while choice not in ['fight', 'flee', 'bargain']:
            choice = input("Invalid choice. What do you want to do? Fight, flee, or bargain? ")
        if choice == 'fight':
            roll = random.randint(1, 6)
            if roll in [2, 4]:
                print("You realize you're not going to win the fight and try to bargain with the robot.")
                return "bargain"
            elif roll in [1, 5]:
                print("You realize you're not winning the fight and try to flee.")
                return "flee"
            elif roll in [3]:
                print("After an intense battle you rip the bionic red eye from the robots head and see a code on his internal panel. As the machine collapses you see a valut behind the droid covered in moss with a small keypad.")
                print("Upon entering the code the door opens revealing the a massive treasure so you grab as much as the ship can hold.")
            else:
                print("You fight valiantly but are ultimately defeated by the robot. Game over.")
                return "game over"
        elif choice == 'flee':
            roll = random.randint(1, 6)
            if roll % 2 == 1:
                print("You manage to get away from the robot and return to Montressanaro to regroup.")
                return "chapter 3"
            else:
                print("The robot chases after you and catches up, forcing you to fight or bargain.")
                return "fight/bargain"
        else:
            print("You attempt to bargain with the robot.")
            return "bargain"
    else:
        print("You travel in the direction of {} and find yourself in a plain, boring landscape.".format(direction))
        print("There doesn't seem to be much of interest here.")
        choice = input("Choose another direction to explore or regroup in Montressanaro (type 'regroup'): ")
        while choice not in directions and choice != 'regroup':
            choice = input("Invalid choice. Choose another direction to explore or regroup in Montressanaro (type 'regroup'): ")
        if choice == 'regroup':
            print("You decide to regroup in Montressanaro and return to the previous chapter.")
            return "chapter 3"
        else:
            print("You travel in the direction of {} and find yourself in another plain, boring landscape.".format(choice))
            print("There doesn't seem to be much of interest here.")
            choice = input("Choose another direction to explore or regroup in Montressanaro (type 'regroup'): ")
            while choice not in directions and choice != 'regroup':
                choice = input("Invalid choice. Choose another direction to explore or regroup in Montressanaro (type 'regroup'): ")
            if choice == 'regroup':
                print("You decide to regroup in Montressanaro and return to the previous chapter.")
                return "chapter 3"
            else:
                print("You travel in the direction of {} and find yourself in another plain, boring landscape.".format(choice))
                print("There doesn't seem to be much of interest here.")
                choice = input("Choose another direction to explore or regroup in Montressanaro (type 'regroup'): ")

choose_direction()
