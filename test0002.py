import time
import sys
import os
import os.path
import pickle
import json

Player_personality_Abrasiveness = str("Abrasiveness\nAbrasiveness can be seen as a negative trait because it describes having trouble being nice in a conversation. You're demanding, and although you can get what you want, you may end up hurting others. It can increase your intimidation stat, but people will find you insufferable, and it can destroy civil discourse.")
Player_personality_AbsentMinded = str("Absent-Minded\nA character who is absentminded is seen as someone who is smart but is always thinking too much. Because of this, they may end up being lost in the conversation or not being aware of where they are. Your character may be someone they rely on for knowledge, but when it comes to being in the present, count them out.")
Player_personality_Aggression = str("Aggression\nAggression is when a character is always ready to fight and is quite a menace. However, because of aggression, they may end up starting fights when there is a more peaceful solution, and their anger and brute force may be a weakness when the battle requires more strategy. Any kind of gestures that might demand power are included in this personality.")
Player_personality_Brawler = str("Brawler\nA brawler is someone who likes to use their fists rather than any weapons. They believe that what they always have with them is the best weapon. A brawler may be quick on their feet because they are less encumbered, but may find it difficult to win a battle where weapons are used. They value anything they can naturally use on their body.")
Player_personality_Cautious = str("Cautious\nA cautious player is always taking steps to make sure they are safe in combat, taking note of everything in nature, every background noise, and going off their history and experience. Cautious and cowardice can be mutually exclusive or come hand in hand depending on the character. Someone cautious may use different strategies to get out in the safest way possible but may be weak to fear attacks. If you need a character who can solve problems in the most peaceful way possible, however, a cautious person is the way to go.")
Player_personality_Detached = str("Detached\nA detached character is always in their little world when it comes to the group. They will be behind and not talk much. This gives them a ranged advantage, but it can mean that no one trusts the characters which can be a good or bad thing depending on how you are playing the game. These members may not use a ton of language or share ideas with other characters. They keep details and aspects to themselves, not out of greed or without reason.")
Player_personality_Dishonesty = str("Dishonesty\nA dishonest character, well, lies a lot. This character has mastered the art of lying and can use it to get what they want. Of course, if the tower of lies falls, it can ruin your character as everyone will find out that you have been dishonest. Especially if they have been exposed and then say something which is the truth. It can end up being a boy who cried wolf situation, and you might lose money or your spot at the table.")
Player_personality_Distinctive = str("Distinctive\nThis is when someone has a physical trait that sets them apart. They can have big ears, a scar, or another characteristic that sets them apart. As you can imagine, this can be a bit of a disadvantage if your character is trying to hide or disguise themselves. However, it gives your character a bit of a reputation. If your character has a limp, they may use it to get sympathy, for example.")
Player_personality_Easygoing = str("Easygoing\nThis is a friendly character. Being friendly means that people like talking to you and you have no problem making friends. However, you have a hard time standing up for yourself or getting into fights, and you may have a problem if you need to be more aggressive in your act. An easygoing character may be gullible as well. Gaining respect while also maintaining your freedom and accomplishments is a great skill of these characters.")
Player_personality_Farsighted = str("Farsighted\nIn a character's traits, a flaw might be farsightedness. In many worlds, glasses are not a thing, so the character has to deal with their vision. Farsighted person has a hard time seeing what's nearby them, but they can see ahead very well. The people on this character sheet may not have as many options or as much choice in deciding what to do in the future since they cannot see as well into the place they are heading.")
Player_personality_Focused = str("Focused\nSomeone who's focused can keep their eyes on the prize no matter how many things try to distract them. However, those who are too focused on one thing may ignore something else important that passes them by. ")
Player_personality_HardOfHearing = str("Hard Of Hearing\nThis is when a character is deaf or has trouble hearing. Despite their impairment, they may have enhanced their other senses to compensate.")
Player_personality_Hardy = str("Hardy\nThese people consider themselves strong, and they may judge those who aren't as hardy. The problem is that they can sometimes overestimate their strength, and they may end up getting hurt as a result.")
Player_personality_Honest = str("Honest\nThis is someone who never wants to tell a lie. Sincerity means that more people will flock to you and trust you. However, there are times when you may need to tell a white lie or lie to survive. In those cases, you may have trouble keeping up a lie, and you may not be able to spot other liars.")
Player_personality_Illiterate = str("Illiterate\nIn the fantasy world, reading can sometimes be a privilege, and someone illiterate won't be able to read. Instead, they may have other skills they use. Sometimes, a character may learn to read over time.")
Player_personality_Inattentive = str("Inattentive\nSomeone who is inattentive will be able to deal with smaller tasks, but when it comes to big projects, they won't do them.")
Player_personality_Polite = str("Polite\nA character who is polite will try to be as well-spoken as possible, even if they don't like the person they're speaking to. They can be genuinely polite, or they may be using politeness to their advantage.")
Player_personality_Quick = str("Quick\nSomeone quick will is faster than more people. They may be able to escape faster, but they may be less skilled in other areas.")
Player_personality_Relentless = str("Relentless\nSomeone who is relentless won't give up no matter what. This is great for situations that require persistence, but characters who are relentless may over-exhaust themselves. This can lead to fatigue.")
Player_personality_Slow = str("Slow\nSlowness gives a character two personality traits. They will not be able to escape as fast, but they may be sturdier. When it's time to run, they'll be left behind. However, they can be able to fight easier.")
Player_personality_Specialized = str("Specialized\nSomeone specialized will be skilled in one particular subject but may have fewer skills in other subjects. For example, a character may be a master at crafting, but poor at fighting. Make sure your skills are balanced or learn to deal with your weakness.")
Player_personality_Suspicious = str("Suspicious\nSuspicious characters are skeptical of everyone they meet. This can help them spot people who are trying to do them wrong, but the problem with that is that it can turn people away from you because of how distrustful you are.")
Player_personality_Uncivilized = str("Uncivilized\nAn uncivilized person was raised in the wild or is just someone who finds themselves being able to define one trait related to animals before people. They may be awkward when it comes to various situations where they must speak, so make sure there are sociable people to prop them up."+"\n")

file_exists = os.path.isfile('savefile001.txt')
def clear():
    os.system('cls')

def license():
    print("[SYSTEM]This work © 2022 by Diamond Wolf is licensed under CC BY-NC-SA 4.0")

def sys_Player_refsheet_pop():
    print("\n")
    time.sleep(0.5)
def sys_Player_personalitya():
    while True:
        Player_personality = input(Player_personality_Abrasiveness + "\n\n" + Player_personality_AbsentMinded + "\n\n" + Player_personality_Aggression + "\n\n" + Player_personality_Brawler + "\n\n" + Player_personality_Cautious + "\n\n" + Player_personality_Detached + "\n\n" + Player_personality_Dishonesty + "\n\n" + Player_personality_Distinctive + "\n\n" + Player_personality_Easygoing + "\n\n" + Player_personality_Farsighted + "\n\n" + Player_personality_Focused + "\n\n" + Player_personality_HardOfHearing + "\n\n" + Player_personality_Hardy + "\n\n" + Player_personality_Honest + "\n\n" + Player_personality_Illiterate + "\n\n" + Player_personality_Inattentive + "\n\n" + Player_personality_Polite + "\n\n" + Player_personality_Quick + "\n\n" + Player_personality_Relentless + "\n\n" + Player_personality_Slow + "\n\n" + Player_personality_Specialized + "\n\n" + Player_personality_Suspicious + "\n\n" + Player_personality_Uncivilized + "\nEnter personality:")
        if Player_personality == "Abrasiveness" or Player_personality == "Absent-Minded" or Player_personality == "Aggression" or Player_personality == "Brawler" or Player_personality == "Cautious" or Player_personality == "Detached" or Player_personality == "Dishonesty" or Player_personality == "Distinctive" or Player_personality == "Easygoing" or Player_personality == "Farsighted" or Player_personality == "Focused" or Player_personality == "Hard of Hearing" or Player_personality == "Hardy" or Player_personality == "Honest" or Player_personality == "Illiterate" or Player_personality == "Inattentive" or Player_personality == "Polite" or Player_personality == "Quick" or Player_personality == "Relentless" or Player_personality == "Slow" or Player_personality == "Specialized" or Player_personality == "Suspicious" or Player_personality == "Uncivilized":
            break
        else:
            print("[SYSTEM]Incorrect input ! Try again\n")


def dprint001(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.10)
def dprint002(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.50)
def dprint003(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.80)

def saveload():
    if file_exists:
        file=open("savefile001.txt","r")
        checkpoint = file.read()
        file.close()
    else:
        checkpoint = "0"
        print("[SYSTEM]No savefile found")
        sys_nosavefound_yn = input("[SYSTEM]Would you like to start from the beginning ? (y/n)\n")
        while True:
            if sys_nosavefound_yn.lower() in ("yes", "y"):
                room_all()

            elif sys_nosavefound_yn.lower() in ("no", "n"):
                print("[SYSTEM]Program finished\n")
                input("[SYSTEM]Press enter to exit")
                sys.exit()

            else:
                print("[SYSTEM]Incorrect input ! Try again\n")



def save():
    file=open("savefile001.txt","w")
    file.write()
    file.close()

def room_all():
    room_1()

def room_1():
    time.sleep(3)
    license()
    time.sleep(3)
    os.system('cls')
    time.sleep(2)
    dprint001("Welcom")
    dprint002("e...\n")
    dprint001("I'd like to introduce mysel")
    dprint002("f...\n")
    time.sleep(3)
    dprint001("I'm Diamond, ")
    time.sleep(1)
    dprint001("Diamond Wolf,")
    time.sleep(2)
    dprint001(" the creator of thi")
    dprint002("s...")
    dprint001("thing or ")
    time.sleep(1)
    dprint001("whatever it i")
    dprint002("s...\n")
    time.sleep(3)
    dprint001("While I continue, ")
    time.sleep(1)
    dprint001("would you mind filling thi")
    dprint002("s..?\n")
    print("**hands you a paper and a pen**")
    time.sleep(3)
    Player_FName = input("First Name:")
    print("\n")
    Player_LName = input("Last Name:")
    print("\n")
    dprint001(Player_FName+"..."+Player_LName+"\nOk ! Hope I would remember it for at least a few minute")
    dprint002("s...\n")
    while True:
        Player_Age = input("Age:")
        if Player_Age.isnumeric() and 13 <= int(Player_Age) <= 40 :
            break
        else:
            if Player_Age.isnumeric():
                if Player_Age < 13:
                    print("[SYSTEM]Too young!")
                elif Player_Age > 40:
                    print("[SYSTEM]Too old!")
            else:
                print("[SYSTEM]Incorrect input ! Try again\n")
    print("\n\n")
    sys_Player_personalitya()
    print("\n")


    while True:
        sys_NSFW = input("!! Warning !! \nDo you want NSFW content to be included in the scenes descriptions ? The game by default includes details about blood and some else details, to continue with the full experience type 'yes', else, if you want to exclude the details and just get a faster description about the NSFW scenes, type 'no'\n")
        if sys_NSFW.lower() in  ("yes", "y"):
            NSFW = str("true")
            break
        elif sys_NSFW.lower() in  ("no", "n"):
            NSFW = str("false")
            break
        else:
            print("[SYSTEM]Incorrect input ! Try again\n")

    print("\n")
    save()
    print("[SYSTEM]Checkpoint reached")

    def checkpoint1():
        print("[SYSTEM]Checkpoint '1' loaded")

    input("[SYSTEM]Press enter to exit")