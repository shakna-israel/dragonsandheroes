import time
import os
import random

def clear():
    os.system(['clear','cls'][os.name == 'nt'])

def kill_hermit():
    """Return a hermit death as a string"""
    deaths = []
    deaths.append("The hermit suddenly keels over and dies, screaming in agony.")
    deaths.append("The hermit seems to gasp, clutching at his chest as he drops to the ground slowly.")
    deaths.append("The hermit appears to dissolve like snow, his voice screaming in terror.")
    deaths.append("The hermit collapses into pixie dust.")
    deaths.append("A shadowy figure appears behind the hermit, and drags him into the ground.")
    deaths.append("A scythe swipes through the hermit, tearing him in twain.\nDeath waves at you with a skeletal smile as he walks away.")
    return random.choice(deaths)

def storyOne(player):
    """First Story Event"""
    player.story += 1
    clear()
    print("The dust gathers around, swirling, shaking, taking some sort of shape.")
    time.sleep(2)
    print("Its the bloody hermit again!")
    time.sleep(2)
    clear()
    print("Hermit: Greetings, " + str(player.name) + ". It is good to see you.")
    print(str(player.name) + ": Really? You still alive?")
    time.sleep(5)
    clear()
    print("Hermit: Shut up.\n\nAlso, incidentally, I'm here to warn you. The world has noticed you... Your progress will become... Difficult.")
    time.sleep(4)
    clear()
    print("Hermit: Now, a choice awaits you. I have the power to offer you a gift!")
    time.sleep(2)
    clear()
    print("0: A better weapon.")
    print("1: Better armor.")
    print("2: A better enchantment.")
    print("3: A rank increase.")
    choice = input("Enter a number between 0 and 3: ")
    if choice == "0":
        player.weapon += 1
    elif choice == "1":
        player.armor += 1
    elif choice == "2":
        player.enchantment += 1
    elif choice == "3":
        player.level += 1
    else:
        pass
    clear()
    print("Hermit: Excellent!")
    print(kill_hermit())
    time.sleep(4)
    clear()
    return True

def storyTwo(player):
    """Second Story Event"""
    player.story += 1
    pass

def storyThree(player):
    """Third Story Event"""
    player.story += 1
    pass

def storyFour(player):
    """Fourth Story Event"""
    player.story += 1
    pass

def storyFive(player):
    """Fifth Story Event"""
    player.story += 1
    pass

def storySix(player):
    """Sixth Story Event"""
    player.story += 1
    pass

def storySeven(player):
    """Seventh Story Event"""
    player.story += 1
    pass

def storyEight(player):
    """Eighth Story Event"""
    player.story += 1
    pass

def storyNine(player):
    """Ninth Story Event"""
    player.story += 1
    pass

def storyTen(player):
    """Tenth Story Event"""
    player.story += 1
    pass

def storyOver(player):
    """End the Story."""
    print("Game Over")
    # We should restart the story here somehow...
    os._exit(0)
    pass
