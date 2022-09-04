import time
import random
import enum


class Color(enum.Enum):
    red = '\033[91m'
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    black = '\033[0m'
    bold = '\033[1m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def print_pause(message_to_print, delay=1):
    print(Color.get_color() + message_to_print)
    time.sleep(delay)


def valid_input(prompt, options):
    while True:
        choice = input(prompt).lower()
        if choice in options:
            return choice
        print_pause(f'Sorry, the option "{choice}" is invalid. Try again!')


def intro():
    print_pause("You find yourself standing in a forest, "
                "filled with huge trees and yellow wildflowers.",)
    print_pause("This feels like a scene from the medieval "
                "movie you watched last night before bed.")
    print_pause("You see a figure running towards "
                "you from the distance.")
    print_pause("It's an elf!")
    print_pause("She tells you that she's so glad you came "
                "to slay the wicked troll who has been "
                "terrifying the nearby village.")
    print_pause("She tells you to follow her.")
    print_pause("You're no hero but you figure this is dream "
                "so you might as well do it.")
    print_pause("She leads you deeper into the forest "
                "and says her journey ends here.")
    print_pause("She leaves you with her favorite "
                "albeit useless dagger.")
    print_pause("To your left leads to an abandoned hut.")
    print_pause("To your right leads to a dungeon.\n")


def fight_or_flight(items, your_weapon):
    choice = valid_input("Would you like to (1) fight "
                         " or (2) run away?\n",
                         "'1', '2'")
    if choice == "1":
        fight(items, your_weapon)
    elif choice == "2":
        print_pause("You run back into the forest.\n"
                    "Luckily, you don't seem to have"
                    "been followed.")
        forest(items, your_weapon)


def fight(items, your_weapon):
    print_pause("You have chosen to fight")
    if your_weapon in items:
        print_pause("As the wicked troll moves to attack,"
                    f"you take out your cool new {your_weapon}")
        print_pause("The brightness alone coming of"
                    f"your {your_weapon} is enough to blind the troll")
        print_pause("He runs away from his own house crying like a baby")
        print_pause("You're victorious! The townpeople are"
                    "so grateful that they decide to throw"
                    "a large feast in your honour")
        print_pause("You're eating like royalty tonight"
                    "and all you just had to do was flash"
                    "some bling!")

    else:
        print_pause("You feel a bit under-prepared for this,"
                    "what with only having a useless dagger.")
        print_pause("You decide to give it a shot anyways,"
                    "since it's just a dream")
        print_pause("You do your best....")
        print_pause(f"But your {your_weapon} is no match for the troll.")
        print_pause("You have been defeated!")


def hut(items, your_weapon):
    print_pause("You approach the door of the hut.")
    print_pause("You are about to knock when the door "
                "opens and out steps a huge green troll.")
    print_pause("Eep! This must be the wicked troll's house!")
    print_pause("The troll roars and braces to pounce on you")
    fight_or_flight(items, your_weapon)


def dungeon(items, your_weapon):
    if your_weapon in items:
        print_pause("You peer cautiously into the dungeon")
        print_pause("You've been here before, and gotten all the good stuff.")
        print_pause("It's just an empty dungeon now")
        print_pause("You walk back to the forest")
        forest(items, your_weapon)
    else:
        print_pause("You peer cautiously into the dungeon")
        print_pause("Its not as bad as you expected, quite beautiful actually")
        print_pause("But wait, what's that sticking out of that rock?")
        print_pause(f"Its the magical {your_weapon}!")
        print_pause("It must be your lucky day!\n")
        print_pause("You swap the useless dagger out "
                    f"for your fancy new {your_weapon}")
        print_pause("You walk back to the forest")
        items.append(your_weapon)
        forest(items, your_weapon)


def forest(items, your_weapon):
    choice = valid_input("Enter 1 to knock on the door of the hut.\n"
                         "Enter 2 to peer into the dungeon.\n"
                         "What would you like to do?\n",
                         "(Please enter 1 or 2.)\n")
    if choice == "1":
        hut(items, your_weapon)
    elif choice == "2":
        dungeon(items, your_weapon)


def play_game():
    items = []
    weapons = ["sword", "axe", "lance"]
    your_weapon = random.choice(weapons)
    intro()
    forest(items, your_weapon)


def play_again():
    choice = valid_input("Would you like to play again? (y/n)\n", "'y', 'n'")
    if choice == 'y':
        print_pause("Excellent! Restarting the game ...")

    elif choice == 'n':
        print_pause("Thanks for playing! See you next time.")
        exit(0)


def game():
    while True:
        play_game()

        play_again()


if __name__ == '__main__':
    game()
