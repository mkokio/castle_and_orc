from os import system
from random import randint

gametitle = "Castle Dungeons - A Game"
system("mode 110, 30")
system("title "+ gametitle)

def cls():
    """Clears the screen"""
    system('cls')

character_name = None #these are global variables, note the usage in create_characters()
character_race = None
character_class = None
character_strength = None
character_magic = None
character_dexterity = None
character_life = None

cls()
print("Welcome to this game")

def Intro():
    print("\nIn this adventure, you are the hero.")
    print("Your choices, skills and luck all matter.")
    print("\nAn evil something-er-other is holding your fellow adventurers prisoners.")
    print("Will you succeed to free your friends from the castle dungeons, or die trying?\n")
    input("Press Enter to start...")

Intro()

def create_character():
    cls()
    global character_name
    character_name = input("""
        Let's begin by creating your character.
        What's your name?

        > """)
    print(f"\n\tWelcome, '{character_name.title()}'! The world is currently your oyster.")
    global character_race
    while character_race is None:
        race_choice = input("""
        Choose a character:
        1 - Elf
        2 - Dwarf

        > """)
        if race_choice == "1":
            character_race = "Elf"
        elif race_choice == "2":
            character_race = "Dwarf"
        else:
            print("Invalid choice; type 1 or 2")
    global character_class
    while character_class is None:
        class_choice = input("""
        Choose your class
        1 - Warrior
        2 - Wizard

        > """)
        if class_choice == "1":
            character_class = "Warrior"
        elif class_choice == "2":
            character_class = "Wizard"
        else:
            print("Invalid choice, type 1 or 2")

create_character()

def create_character_skill_sheet():
    cls()
    global character_name, character_class, character_race, character_strength, character_magic, character_dexterity, character_life
    print("""
    It's time to determine your 4 skills.
    -Strength, for combat and strength tests
    -Dexterity, for ability tests
    -Magic, for spells and such
    -Life, which you need more than zero of. Otherwise dead.

    Your class and class already pre-determined a certain base-level; how convenient.
    Let's roll a 6-sided die to increase your skills.

    Here is your base Character SKills Sheet:
    """)
    character_strength = 5
    character_magic = 0
    character_dexterity = 3
    character_life = 10
    if character_race == "Elf":
        character_strength += 3
        character_magic += 6
        character_dexterity +=4
        character_life += 2
    elif character_race == "Dwarf":
        character_strength += 5
        character_life += 4
    if character_class == "Warrior":
        character_strength += 3
        character_life += 3
    elif character_race == "Wizard":
        character_magic += 4
    print(f"""
    Name: {character_name.title()}
    Class: {character_class}
    Strength: {character_strength}
    Magic: {character_magic}
    Dexterity: {character_dexterity}
    Life: {character_life}
    """)
    input("\nPress Enter when you're ready to roll (for your skills and such)")

create_character_skill_sheet()

def modify_skills():
    cls()
    global character_strength, character_dexterity, character_life
    outcome = "You rolled a "
    print("Here's our trusty handheld cube, each side numbered 1 through 6")
    input("\nPress Enter to roll for Strength")
    strength_roll = randint(1,6)
    print(outcome + str(strength_roll))
    print(f"{str(character_strength)} + {str(strength_roll)} = ")
    character_strength += strength_roll
    print(f"Your new Strength: {character_strength}")

    input("\nPress Enter to roll for Dexterity")
    dexterity_roll = randint(1,6)
    print(outcome + str(dexterity_roll))
    print(f"{str(character_dexterity)} + {str(dexterity_roll)} = ")
    character_dexterity += dexterity_roll
    print(f"Your new Dexterity: {character_dexterity}")

    input("\nPress Enter to roll for Life")
    life_roll = randint(1,6)
    print(outcome + str(life_roll))
    print(f"{str(character_life)} + {str(life_roll)} = ")
    character_life += life_roll
    print(f"Your new Life: {character_life}")
    input("\nPress Enter to continue...")
    cls()

modify_skills()

def current_character_sheet():
    """Displays a neatly formatted current character sheet"""
    global character_name, character_class, character_race, character_strength, character_magic, character_dexterity, character_life
    cls() #should I clear the screen??
    print(f"""
    ~ Current Character Sheet ~
    Name: {character_name.title()}
    Class: {character_class}
    Strength: {character_strength}
    Magic: {character_magic}
    Dexterity: {character_dexterity}
    Life: {character_life}
    """)
    input("\n Press Enter to continue the adventure...")

current_character_sheet()

def Scene_1():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    You have entered the castle dungeon..
    It's dark, but you have a weak flashlight on your phone.
    It's kinda damp in here, with a smell to match exactly what you'd imagine it to be.
    Heading steadily down a corridor, you reach a "T" at which you can turn either way.

    Featureless, other than the matching dampness and smell, you must choose:

    1 - Go left
    2 - Go right
    > """)
        if user_input == "1":
            choice="1"
            Scene_2()
        elif user_input == "2":
            choice="2"
            Scene_3()
        else:
            print("Invalid choice. Type a number.")

def Scene_2():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    Oh, you hear a strange noise... from behind you?

    1 - Continue walking
    2 - Stop and listen
    > """)
        if user_input == "1":
            choice="1"
            combat()
        elif user_input == "2":
            choice="2"
            print("hwaaaa.......\n")
            input("")
            skill_check()
        else:
            print("Invalid choice. Type a number.")

def Scene_3():
    cls()
    choice = None
    while choice is None:
        user_input=input("""
    Oh, you hear a strange noise... from behind you?

    1 - Continue walking
    2 - Stop and listen
    > """)
        if user_input == "1":
            choice="1"
            combat()
        elif user_input == "2":
            choice="2"
            print("bwaaaa.......\n")
            input("")
            skill_check()
        else:
            print("Invalid choice. Type a number.")

def skill_check():
    cls()
    input("A giant rock falls from the ceiling. Press Enter to roll to see if you get squished.")
    roll = randint(1,6)
    input(f"\nYou rolled a {roll}!")
    if roll+character_dexterity > 10:
        print("""
            You quickly jump out of the way of the rock. You're safe.

            For now.

            Except that strange noise is still there. Maybe closer even?
            """)
        input("\nPress Enter to Continue")
        combat()
    else:
        print("""
            Squish.
            
            Drops of moisture break away from the ceiling onto the stone floor. Drip, drip.

            """)
        input("\tDrip\n")
        input("\tDrip\n")
        input("""
            Your already pooling blood is every so slowly diluted and washed away from these slow drips.
            Your lifeless and forgotten body decays until becoming one with the stone floor;
            various unpleasant rodents carry away the remainder of available bones;
            those not forever lost under the giant rock.
            """)
        exit_restart()

def combat():
    cls()
    global character_life
    input("Uh oh.")
    print("\nAn orc attacks you!")
    input("\nPress Enter to combat...")
    orc = [13, 12] #[strength,life]
    while orc[1] > 0 and character_life > 0: 
        print(f"\n{character_name.title()} life: {character_life}")
        print(f"Orc life: {orc[1]}")
        input("BATTLE")
        char_roll=randint(1,6)
        print("You rolled: "+str(char_roll))
        print(f"\tThat means your strength is {char_roll} + {character_strength}")
        monst_roll=randint(1,6)
        print("The orc rolled: "+str(monst_roll))
        print(f"\tThat means the orc strength is {monst_roll} + {orc[0]}")
        if char_roll+character_strength >= monst_roll+orc[0]:
            print("You hit the orc!")
            wound = randint(1,6)
            orc[1] = orc[1] - wound
            print(f"The orc took {wound} damage.")
        else: 
            print("The orc hits you!")
            wound = randint(1,6)
            character_life = character_life - wound
            print(f"You took {wound} damage.")
    if character_life > 0:
        print("\n\tYou killed the orc, nice!")
        exit_restart()
    else:
        input("\n\t'Twas a wonderful battle for the orc and various floor-rodent spectators, but not you.")
        input("Quite unceremoniously, the orc, with his (or her) very orc-like gait, saunters back into the darkness.")
        input("You are now food for mushrooms, assuming they grow here, devoid of natural light;")
        input("nobody will find your body.")
        exit_restart()

def exit_restart():
    while True:
        prompt = "\nType 'x' to Exit or 'r' to restart"
        prompt += "\n'p' for a poem: "
        decision = input(prompt)
        if decision == 'r':
            cls()
            game()
        elif decision == 'x':
            break
        elif decision == 'p':
            print("\n\tSteak on my grill, oh! Sleep on my pillow.")
            print(f"\tI can't think of a word that rhymes with {character_name.title()}.")
        else:
            print("\tInvalid input. Try again.")

def game():
    Intro()
    create_character()
    create_character_skill_sheet()
    modify_skills()
    current_character_sheet()
    Scene_1()

Scene_1()