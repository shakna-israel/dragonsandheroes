import time
import os
import random
import json
import locale
import stories

def clear():
    os.system(['clear','cls'][os.name == 'nt'])

class Player(object):
    def __init__(self):
        self.health = 100
        self.armor = 0
        self.weapon = 0
        self.enchantment = 0
        self.level = 0
        self.progress = 0
        self.name = "Unknown"
        self.pronoun = "He"
        self.status = 0
        self.gold = 0
        self.story = 0

    def save_to_file(self):
        save_data = {}
        save_data['health'] = self.health
        save_data['armor'] = self.armor
        save_data['weapon'] = self.weapon
        save_data['enchantment'] = self.enchantment
        save_data['level'] = self.level
        save_data['progress'] = self.progress
        save_data['name'] = self.name
        save_data['pronoun'] = self.pronoun
        save_data['status'] = self.status
        save_data['gold'] = self.gold
        save_data['story'] = self.story
        with open("dragonsAndHeroes.save","w+") as openFile:
            json.dump(save_data, openFile)
        return True

    def load_from_file(self):
        if os.path.isfile("dragonsAndHeroes.save"):
            with open("dragonsAndHeroes.save","r") as openFile:
                save_data = json.load(openFile)
            try:
                self.health = int(save_data['health'])
            except KeyError:
                self.health = 100
            try:
                self.armor = int(save_data['armor'])
            except KeyError:
                self.armor = 0
            try:
                self.weapon = int(save_data['weapon'])
            except KeyError:
                self.weapon = 0
            try:
                self.enchantment = int(save_data['enchantment'])
            except KeyError:
                self.enchantment = 0
            try:
                self.level = int(save_data['level'])
            except KeyError:
                self.level = 0
            try:
                self.progress = int(save_data['progress'])
            except KeyError:
                self.progress = 0
            try:
                self.name = save_data['name']
            except KeyError:
                self.name = "Samuel the Corrupted"
            try:
                self.pronoun = save_data['pronoun']
            except KeyError:
                self.pronoun = "Xir"
            try:
                self.status = int(save_data['status'])
            except KeyError:
                self.status = 0
            try:
                self.gold = int(save_data['gold'])
            except KeyError:
                self.gold = 0
            try:
                self.story = int(save_data['story'])
            except KeyError:
                self.story = 0
            return True
        else:
            return False

    def start_game(self):
        clear()
        print("""
        DRAGONS
           &
        Heroes
        """)
        time.sleep(2)
        clear()
        print("In a far away land, in a time long since forgotten...")
        print("...")
        time.sleep(5)
        clear()
        print("DRAGONS roamed the land, and harrowed the people into terror.")
        print("Yet, one HOPE remained.")
        print("...")
        time.sleep(5)
        clear()
        print("Your village was attacked, and everyone you know was killed before your eyes!")
        print("Yet, somehow, you survived.")
        print("...")
        time.sleep(5)
        clear()
        print("You stumble upon an old hermit, as you search for the nearest town.")
        self.name = input("Hermit: What is your name? ")
        print("Hermit: HA! " + str(self.name) + " is a terrible name! Well, at least for you.\nYou are a HERO!")
        print(str(self.name) + ": What?")
        print("...")
        time.sleep(5)
        clear()
        print("Hermit: Well... Maybe not a hero... What are you?")
        print("0: Hero")
        print("1: Lord")
        print("2: Lady")
        print("3: Eunuch")
        print("4: Mistress")
        print("5: Deadpool")
        print("6: Villain")
        print("7: Bandit")
        print("8: Imperial Sympathiser")
        print("9: Samurai")
        print("10: Mage")
        print("11: One of them, I guess.")
        print("12: None of those. Go to hell.")
        title = input("Enter a number between 0 and 10: ")
        if title == "0":
            self.name = self.name + " the Hero"
        elif title == "1":
            self.name = self.name + " the Lord"
        elif title == "2":
            self.name = self.name + " the Lady"
        elif title == "3":
            self.name = self.name + " the Eunuch"
        elif title == "4":
            self.name = self.name + " the Mistress"
        elif title == "5":
            self.name = "Deadpool"
        elif title == "6":
            self.name = self.name + " the Villain"
        elif title == "7":
            self.name = self.name + " the Bandit"
        elif title == "8":
            self.name = self.name + " the Imperial"
        elif title == "9":
            self.name = self.name + " the Samurai"
        elif title == "10":
            self.name = self.name + " the Mage"
        elif title == "11":
            self.name = self.name + random.choice([" the Hero", " the Lord", " the Lady", " the Eunuch", " the Mistress", " the Villain", " the Bandit", " the Imperial", " the Samurai", " the Mage"])
        else:
            pass
        time.sleep(5)
        clear()

        if self.name != "Deadpool":
            print("Hermit: Wait... Are you a boy... Or?")
            print("0: Male")
            print("1: Female")
            print("2: Indeterminate")
            print("3: Faerie")
            print("4: Halfling")
            print("5: Demonspawn")
            pronoun = input("Enter a number between 0 and 5: ")
            if pronoun == "0":
                self.pronoun = "He"
            elif pronoun == "1":
                self.pronoun = "Her"
            elif pronoun == "2":
                self.pronoun = random.choice(["Schkler", "Schklee"])
            elif pronoun == "3":
                self.pronoun = "Fae"
            elif pronoun == "4":
                self.pronoun = "Hobbitses"
            elif pronoun == "5":
                self.pronoun = random.choice(["Xe", "Xir"])
            else:
                self.pronoun = "Idiot"
            time.sleep(5)
            clear()
        else:
            self.pronoun = "He"

        print("Hermit: It is your FATE to save this world, " + str(self.name) + "!")
        print("...")
        time.sleep(10)
        clear()
        print("The hermit dissolved into pixie dust.")
        print("That was kinda weird.")
        print("Maybe it might have some relevance later.")
        print(str(self.name) + " sets off on their journey... Not knowing if they will save the world... Or burn it.")
        print("...")
        clear()

    def print_stats(self):
        locale.setlocale(locale.LC_ALL, 'en_US')
        gold = locale.format("%d", self.gold, grouping=True)
        print(str(self.name) + " is a " + str(self.level_string()) + ".\n" + str(self.pronoun) + " is wearing " + str(self.armor_string()) + " armor.\n" + str(self.pronoun) + " is using a " + str(self.weapon_string()) + " to fight.\n" + str(self.pronoun) + " have the enchantment of " + str(self.enchantment_string()) + ".\n" + str(self.pronoun) + " have " + str(self.health) + "% health remaining.\n" + str(self.pronoun) + " is currently " + str(self.get_status()) + ".\n" + str(self.pronoun) + " has " + str(gold) + " gold coins.")

    def get_bad_guy(self):
        bad_guys = []
        bad_guys.append("Vampire")
        bad_guys.append("Werewolf")
        bad_guys.append("Gnome")
        bad_guys.append("Troll")
        bad_guys.append("Dwarf")
        bad_guys.append("Hermit")
        bad_guys.append("Wolf")
        bad_guys.append("Cat")
        bad_guys.append("Bear")
        bad_guys.append("Deadpool")
        bad_guys.append("Abandon")
        bad_guys.append("Angel")
        bad_guys.append("Ant-Lion")
        bad_guys.append("Arch Demon")
        bad_guys.append("Bahamas")
        bad_guys.append("Behemoth")
        bad_guys.append("Belial")
        bad_guys.append("Samuel")
        bad_guys.append("Snake")
        bad_guys.append("Cursed Snake")
        bad_guys.append("Baal")
        bad_guys.append("Leviathan")
        bad_guys.append("Draco")
        bad_guys.append("Nephilim")
        bad_guys.append("Goat")
        bad_guys.append("Golem")
        bad_guys.append("Gibborim")
        bad_guys.append("Wooden Pallet")
        bad_guys.append("Oceanus")
        return bad_guys

    def get_sentence_end(self):
        sentence_ends = []
        sentence_ends.append(" by beating it senseless.")
        sentence_ends.append(" with extreme sensitivity.")
        sentence_ends.append(" effortlessly.")
        sentence_ends.append(" after greatly struggling.")
        return sentence_ends

    def verify(self):
        if self.health > 100:
            self.health = 100
        elif self.health < 0:
            self.health = 10
        if self.gold > 1000000:
            self.gold = self.gold - 1000000
            self.armor += 1
            self.weapon += 1
            self.enchantment += 1
            self.level += 1
            self.progress = 0
            print("Using 1 million gold to pay for new armor, weaponry, and enchantments!")
            time.sleep(1)
        if self.story == 0 and self.level > 10:
            stories.storyOne(self)
        elif self.story == 1 and self.level > 15:
            stories.storyTwo(self)
        elif self.story == 2 and self.level > 20:
            stories.storyThree(self)
        elif self.story == 3 and self.level > 25:
            stories.storyFour(self)
        elif self.story == 4 and self.level > 30:
            stories.storyFive(self)
        elif self.story == 5 and self.level > 35:
            stories.storySix(self)
        elif self.story == 6 and self.level > 40:
            stories.storySeven(self)
        elif self.story == 7 and self.level > 45:
            stories.storyEight(self)
        elif self.story == 8 and self.level > 50:
            stories.storyNine(self)
        elif self.story == 9 and self.level > 55:
            stories.storyTen(self)
        elif self.armor > 99 and self.level > 99 and self.weapon > 99 and self.story > 9:
            stories.storyOver(self)
        return True

    def benefit(self):
        choice = random.choice([0, 1, 2])
        if choice == 0:
            self.armor += 1
        elif choice == 1:
            self.weapon += 1
        elif choice == 2:
            self.enchantment += 1
        self.progress += 1
        if self.progress > 10:
            self.level += 1
            self.progress = 0
        return True

    def found_string(self):
        found_strings = []
        found_strings.append("stumbled upon a")
        found_strings.append("discovered a")
        found_strings.append("found a")
        found_strings.append("spotted a")
        return random.choice(found_strings)

    def defeat_string(self):
        defeat_strings = []
        defeat_strings.append("defeated the")
        defeat_strings.append("butchered the")
        defeat_strings.append("murdered the")
        defeat_strings.append("decimated the")
        return random.choice(defeat_strings)

    def lost_string(self):
        lost_strings = []
        lost_strings.append("lost to the")
        lost_strings.append("was beaten by the")
        lost_strings.append("was defeated by the")
        return random.choice(lost_strings)

    def event(self):
        if self.status % 5:
            print(str(self.name) + " is selling loot.")
            self.gold += random.choice(range(0, 100 * (self.progress + 1)))
            self.health += random.choice(range(0, 20))
            self.status += 1
            return True
        elif self.status % 10 or self.status % 3:
            bad_guy = random.choice(self.get_bad_guy())
            sentence_end = random.choice(self.get_sentence_end())
            print(str(self.name) + " " + str(self.found_string()) + " " + str(bad_guy) + "!")
            if random.choice([0, 1]) == 1:
                print(str(self.name) + " " + str(self.defeat_string()) + " " + str(bad_guy) + str(sentence_end))
                self.benefit()
                self.status += 1
                self.health = self.health - random.choice(range(0, 25))
                return True
            else:
                print(str(self.name) + " " + str(self.lost_string()) + " " + str(bad_guy) + "...")
                self.health = self.health - random.choice(range(0, 50))
                self.status += 1
                return True
        else:
            self.status += 1
            self.health += random.choice(range(0, 40))
            print(str(self.name) + " is sleeping.")
            return True

    def get_status(self):
        if self.status == 0:
            return "sleeping"
        elif self.status == 1:
            return "hunting"
        elif self.status == 2:
            return "brawling"
        elif self.status == 3:
            return "fighting"
        elif self.status == 4:
            return "kicking ass"
        elif self.status == 5:
            self.gold += random.choice(range(0,20))
            return "selling loot..."
        elif self.status == 6:
            return "killing"
        elif self.status == 7:
            return "butchering"
        elif self.status == 8:
            return "assassinating"
        elif self.status == 9:
            return "executing"
        elif self.status == 10:
            self.gold += random.choice(range(0,20))
            return "selling loot..."
        else:
            return "deleting enemies from existence..."

    def enchantment_string(self):
        if self.enchantment == 0:
            return "Weak Apathy"
        elif self.enchantment == 1:
            return "Apathy"
        elif self.enchantment == 2:
            return "Strong Apathy"
        elif self.enchantment == 3:
            return "Strength"
        elif self.enchantment == 4:
            return "Ironhide"
        elif self.enchantment == 5:
            return "Steelhide"
        elif self.enchantment == 6:
            return "Titaniumhide"
        elif self.enchantment == 7:
            return "Minor Deflect Spell"
        elif self.enchantment == 8:
            return "Deflect Spell"
        elif self.enchantment == 9:
            return "Major Deflect Spell"
        elif self.enchantment == 10:
            return "Minor Absorb Spell"
        elif self.enchantment == 11:
            return "Absorb Spell"
        elif self.enchantment == 12:
            return "Major Absorb Spell"
        elif self.enchantment == 13:
            return "Magical Drain"
        elif self.enchantment == 14:
            return "Vampiric Magical Drain"
        elif self.enchantment == 15:
            return "Howling Vampiric Magical Drain"
        elif self.enchantment == 16:
            return "Zombification"
        elif self.enchantment == 17:
            return "Resurrection"
        elif self.enchantment == 18:
            return "Holy Grail"
        elif self.enchantment == 19:
            return "Telepathy"
        elif self.enchantment == 20:
            return "Telekinesis"
        elif self.enchantment == 21:
            return "Clairvoyance"
        elif self.enchantment == 22:
            return "Pyrokenesis"
        elif self.enchantment == 23:
            return "Retrocognition"
        elif self.enchantment == 24:
            return "Psychic Link"
        elif self.enchantment == 25:
            return "Demonic Rage"
        elif self.enchantment == 26:
            return "Demonic Hunger"
        elif self.enchantment == 27:
            return "Soul Sucker"
        elif self.enchantment == 28:
            return "Soul Summoner"
        elif self.enchantment == 29:
            return "We are Legion"
        elif self.enchantment == 30:
            return "Weak Prescience"
        elif self.enchantment == 31:
            return "Prescience"
        elif self.enchantment == 32:
            return "Great Prescience"
        else:
            return "Magnificent Prescience"

    def weapon_string(self):
        if self.weapon == 0:
            return "Stick"
        elif self.weapon == 1:
            return "Sharpened Stick"
        elif self.weapon == 2:
            return "Really Sharp Stick"
        elif self.weapon == 3:
            return "Blunt Spear"
        elif self.weapon == 4:
            return "Spear"
        elif self.weapon == 5:
            return "Sharp Spear"
        elif self.weapon == 6:
            return "Light Club"
        elif self.weapon == 7:
            return "Club"
        elif self.weapon == 8:
            return "Heavy Club"
        elif self.weapon == 9:
            return "Blunt and Light Axe"
        elif self.weapon == 10:
            return "Blunt Axe"
        elif self.weapon == 11:
            return "Heavy Blunt Axe"
        elif self.weapon == 12:
            return "Heavy Axe"
        elif self.weapon == 13:
            return "Heavy and Sharp Axe"
        elif self.weapon == 14:
            return "Light Dagger"
        elif self.weapon == 15:
            return "Dagger"
        elif self.weapon == 16:
            return "Sharp Dagger"
        elif self.weapon == 17:
            return "Light Sword"
        elif self.weapon == 18:
            return "Sword"
        elif self.weapon == 19:
            return "Sharp Sword"
        elif self.weapon == 20:
            return "Sharp Longsword"
        elif self.weapon == 21:
            return "Small Wand"
        elif self.weapon == 22:
            return "Wand"
        elif self.weapon == 23:
            return "Long Wand"
        elif self.weapon == 24:
            return "Short Magical Staff"
        elif self.weapon == 25:
            return "Magical Staff"
        elif self.weapon == 26:
            return "Large Magical Staff"
        elif self.weapon == 27:
            return "Short Mage's Staff"
        elif self.weapon == 28:
            return "Mage's Staff"
        elif self.weapon == 29:
            return "Large Mage's Staff"
        elif self.weapon == 30:
            return "Short Wizard's Staff"
        elif self.weapon == 31:
            return "Wizard's Staff"
        elif self.weapon == 32:
            return "Large Wizard's Staff"
        elif self.weapon == 33:
            return "Short Warlock's Staff"
        elif self.weapon == 34:
            return "Warlock's Staff"
        elif self.weapon == 35:
            return "Large Warlock's Staff"
        elif self.weapon == 36:
            return "Scroll of Fireball"
        elif self.weapon == 37:
            return "Scroll of Hurricane"
        elif self.weapon == 38:
            return "Scroll of Tornado"
        elif self.weapon == 39:
            return "Scroll of Boulder"
        elif self.weapon == 40:
            return "Scroll of Burning Tornado"
        elif self.weapon == 41:
            return "Scroll of Burning Tsunami"
        elif self.weapon == 42:
            return "Scroll of Earthquake"
        elif self.weapon == 43:
            return "Scroll of Volcano"
        elif self.weapon == 44:
            return "Scroll of Torture"
        elif self.weapon == 45:
            return "Scroll of Mind Control"
        elif self.weapon == 46:
            return "Scroll of Death"
        elif self.weapon == 47:
            return "Scroll of Zomibification"
        elif self.weapon == 48:
            return "Scroll of Summon Ghouls"
        elif self.weapon == 49:
            return "Scroll of Summon Deadpool"
        elif self.weapon == 50:
            return "Scroll of Summon Wyrm"
        elif self.weapon == 51:
            return "Scroll of Summon Fire Wyrm"
        elif self.weapon == 52:
            return "Scroll of Summon Imperial Paladin"
        elif self.weapon == 53:
            return "Scroll of Summon Necromancer"
        elif self.weapon == 54:
            return "Scroll of Summon Bat Swarm"
        elif self.weapon == 55:
            return "Scroll of Summon Death"
        else:
            return "Scroll of Apocalypse"

    def level_string(self):
        if self.level == 0:
            return "Homeless Wanderer"
        elif self.level == 1:
            return "Hermit"
        elif self.level == 2:
            return "Pub Brawler"
        elif self.level == 3:
            return "Fighter"
        elif self.level == 4:
            return "Boxer"
        elif self.level == 5:
            return "Martial Artist"
        elif self.level == 6:
            return "Homeowner"
        elif self.level == 7:
            return "Homewrecker"
        elif self.level == 8:
            return "Bandit"
        elif self.level == 9:
            return "Scout"
        elif self.level == 10:
            return "Squire"
        elif self.level == 11:
            return "Archer"
        elif self.level == 12:
            return "Crossbowman"
        elif self.level == 13:
            return "Knight"
        elif self.level == 14:
            return "Paladin"
        elif self.level == 15:
            return "Imperial Scout"
        elif self.level == 16:
            return "Imperial Squire"
        elif self.level == 17:
            return "Imperial Archer"
        elif self.level == 18:
            return "Imperial Crossbowman"
        elif self.level == 19:
            return "Imperial Knight"
        elif self.level == 20:
            return "Imperial Paladin"
        elif self.level == 21:
            return "Samurai Scout"
        elif self.level == 22:
            return "Samurai Archer"
        elif self.level == 23:
            return "Samurai Squire"
        elif self.level == 24:
            return "Samurai Knight"
        elif self.level == 25:
            return "Samurai Paladin"
        elif self.level == 26:
            return "Manslayer Scout"
        elif self.level == 27:
            return "Manslayer Archer"
        elif self.level == 28:
            return "Manslayer Squire"
        elif self.level == 29:
            return "Manslayer Knight"
        elif self.level == 30:
            return "Manslayer Paladin"
        elif self.level == 31:
            return "True Manslayer"
        elif self.level == 32:
            return "Apprentice Mage"
        elif self.level == 33:
            return "Mage"
        elif self.level == 34:
            return "Wizard"
        elif self.level == 35:
            return "Warlock"
        elif self.level == 36:
            return "Imperial Mage"
        elif self.level == 37:
            return "Imperial Wizard"
        elif self.level == 38:
            return "Imperial Warlock"
        elif self.level == 39:
            return "Imperial Arch Mage"
        elif self.level == 40:
            return "Samurai Mage"
        elif self.level == 41:
            return "Samurai Wizard"
        elif self.level == 42:
            return "Samurai Warlock"
        elif self.level == 43:
            return "Samurai Arch Mage"
        elif self.level == 44:
            return "Vampire"
        elif self.level == 45:
            return "Werewolf"
        elif self.level == 46:
            return "Gnome"
        elif self.level == 47:
            return "Necromancer"
        elif self.level == 48:
            return "Blood Mancer"
        elif self.level == 49:
            return "Wyrm Hunter"
        elif self.level == 50:
            return "Adept Wyrm Hunter"
        elif self.level == 51:
            return "Intermediate Wyrm Hunter"
        elif self.level == 52:
            return "Expert Wyrm Hunter"
        elif self.level == 53:
            return "Dragonling Hunter"
        elif self.level == 54:
            return "Adept Dragonling Hunter"
        elif self.level == 55:
            return "Intermediate Dragonling Hunter"
        elif self.level == 56:
            return "Expert Dragonling Hunter"
        elif self.level == 57:
            return "Grimm"
        elif self.level == 58:
            return "Hansel"
        elif self.level == 59:
            return "Witchling"
        elif self.level == 60:
            return "Swamp Hag"
        elif self.level == 61:
            return "Witch"
        elif self.level == 62:
            return "Undead"
        elif self.level == 63:
            return "Resurrected"
        elif self.level == 64:
            return "Demon"
        elif self.level == 65:
            return "Angel"
        elif self.level == 66:
            return "Dampyre"
        elif self.level == 67:
            return "Alien"
        elif self.level == 68:
            return "Rich guy dressing up like a nightmare"
        elif self.level == 69:
            return "Deadpool"
        elif self.level == 70:
            return "Demigod"
        elif self.level == 71:
            return "Small Deity"
        elif self.level == 72:
            return "Deity"
        elif self.level == 73:
            return "Enlightened Deity"
        elif self.level == 74:
            return "Angry Deity"
        elif self.level == 75:
            return "God"
        else:
            return "Lord of all Creation"

    def armor_string(self):
        if self.armor == 0:
            return "Sackcloth"
        elif self.armor == 1:
            return "Hide"
        elif self.armor == 2:
            return "Leather"
        elif self.armor == 3:
            return "Crab Leather"
        elif self.armor == 4:
            return "Studded Leather"
        elif self.armor == 5:
            return "Bull Leather"
        elif self.armor == 6:
            return "Notched Leather"
        elif self.armor == 7:
            return "Fur Armor"
        elif self.armor == 8:
            return "Bandit"
        elif self.armor == 9:
            return "Squire"
        elif self.armor == 10:
            return "Knight"
        elif self.armor == 11:
            return "Imperial Scout"
        elif self.armor == 12:
            return "Imperial Archer"
        elif self.armor == 13:
            return "Imperial Squire"
        elif self.armor == 14:
            return "Imperial Knight"
        elif self.armor == 15:
            return "Paladin"
        elif self.armor == 16:
            return "Imperial Paladin"
        elif self.armor == 17:
            return "Samurai Scout"
        elif self.armor == 18:
            return "Samurai Archer"
        elif self.armor == 19:
            return "Samurai Squire"
        elif self.armor == 20:
            return "Samurai Knight"
        elif self.armor == 21:
            return "Samurai Paladin"
        elif self.armor == 22:
            return "Manslayer Scout"
        elif self.armor == 23:
            return "Manslayer Archer"
        elif self.armor == 24:
            return "Manslayer Squire"
        elif self.armor == 25:
            return "Manslayer Knight"
        elif self.armor == 26:
            return "Manslayer Paladin"
        elif self.armor == 27:
            return "True Manslayer"
        elif self.armor == 28:
            return "Platinum"
        elif self.armor == 29:
            return "Studded Platinum"
        elif self.armor == 30:
            return "Platinum Scout"
        elif self.armor == 31:
            return "Platinum Archer"
        elif self.armor == 32:
            return "Platinum Squire"
        elif self.armor == 33:
            return "Platinum Knight"
        elif self.armor == 34:
            return "Platinum Paladin"
        elif self.armor == 35:
            return "Assassin"
        elif self.armor == 36:
            return "Adept Assassin"
        elif self.armor == 37:
            return "Intermediate Assassin"
        elif self.armor == 38:
            return "Expert Assassin"
        elif self.armor == 39:
            return "Invisibility"
        elif self.armor == 40:
            return "Hardened Invisibility"
        elif self.armor == 41:
            return "Crystalised Invisibility"
        elif self.armor == 42:
            return "Fire-proof Invisibility"
        elif self.armor == 43:
            return "Spell-proof Invisibility"
        elif self.armor == 44:
            return "Apprentice Mage"
        elif self.armor == 45:
            return "Mage"
        elif self.armor == 46:
            return "Wizard"
        elif self.armor == 47:
            return "Warlock"
        elif self.armor == 48:
            return "Imperial Mage"
        elif self.armor == 49:
            return "Imperial Wizard"
        elif self.armor == 50:
            return "Imperial Warlock"
        elif self.armor == 51:
            return "Imperial Arch Mage"
        elif self.armor == 52:
            return "Samurai Mage"
        elif self.armor == 53:
            return "Samurai Wizard"
        elif self.armor == 54:
            return "Samurai Warlock"
        elif self.armor == 55:
            return "Samurai Arch Mage"
        elif self.armor == 56:
            return "Forbidden"
        elif self.armor == 57:
            return "Human Skin"
        elif self.armor == 58:
            return "Werewolf Skin"
        elif self.armor == 59:
            return "Vampire Skin"
        elif self.armor == 60:
            return "Gnome Skin"
        elif self.armor == 61:
            return "Necromantic"
        elif self.armor == 62:
            return "Uncursed Necromantic"
        elif self.armor == 63:
            return "Blood Mancer's"
        elif self.armor == 64:
            return "Werewolf Blood"
        elif self.armor == 65:
            return "Vampire Blood"
        elif self.armor == 66:
            return "Gnome Blood"
        elif self.armor == 67:
            return "Wyrm Skin"
        elif self.armor == 68:
            return "Wyrm Scale"
        elif self.armor == 69:
            return "Water Wyrm Skin"
        elif self.armor == 70:
            return "Water Wyrm Scale"
        elif self.armor == 71:
            return "Wind Wyrm Skin"
        elif self.armor == 72:
            return "Wind Wyrm Scale"
        elif self.armor == 73:
            return "Earth Wyrm Skin"
        elif self.armor == 74:
            return "Earth Wyrm Scale"
        elif self.armor == 75:
            return "Fire Wyrm Skin"
        elif self.armor == 76:
            return "Fire Wyrm Scale"
        elif self.armor == 77:
            return "Elemental Wyrm Skin"
        elif self.armor == 78:
            return "Elemental Wyrm Scale"
        elif self.armor == 79:
            return "Dragon Tongue"
        elif self.armor == 80:
            return "Dragon Skin"
        elif self.armor == 81:
            return "Dragon Scale"
        elif self.armor == 82:
            return "Imperial Dragon Tongue"
        elif self.armor == 83:
            return "Imperial Dragon Skin"
        elif self.armor == 84:
            return "Imperial Dragon Scale"
        elif self.armor == 85:
            return "Samurai Dragon Tongue"
        elif self.armor == 86:
            return "Samurai Dragon Skin"
        elif self.armor == 87:
            return "Samurai Dragon Scale"
        elif self.armor == 88:
            return "Dragonslayer"
        elif self.armor == 89:
            return "Dragonslayer Scout"
        elif self.armor == 90:
            return "Dragonslayer Archer"
        elif self.armor == 91:
            return "Dragonslayer Squire"
        elif self.armor == 92:
            return "Dragonslayer Knight"
        elif self.armor == 93:
            return "Dragonslayer Mage"
        elif self.armor == 94:
            return "Dragonslayer Wizard"
        elif self.armor == 95:
            return "Dragonslayer Warlock"
        elif self.armor == 96:
            return "Dragonslayer Arch Mage"
        elif self.armor == 97:
            return "Dragonslayer Arch Wizard"
        elif self.armor == 98:
            return "Dragonslayer Arch Warlock"
        elif self.armor == 99:
            return "Dragonslayer Paladin"
        else:
            return "Dragonslayer Arch Paladin"


if __name__ == "__main__":
    clear()
    print("""
    DRAGONS
       &
    Heroes
    """)
    time.sleep(2)
    clear()
    player = Player()
    if player.load_from_file():
        pass
    else:
        player.start_game()
    while True:
        player.verify()
        player.print_stats()
        player.event()
        player.save_to_file()
        time.sleep(2)
        clear()
