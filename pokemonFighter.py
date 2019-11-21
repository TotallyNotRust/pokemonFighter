import json
import random
from tkinter import *
import time

pkmn = ""
epkmn = ""
moves = []
ehealth = 0
health = 0
window = ""


def victory_you():
    print("You win")
    window.destroy()

def enemy_victory():
    print("You loose")
    window.destroy()

def whofirst(moven, pkmn, epkmn, text2):
    global health
    global ehealth
    with open("pokemon.json") as f:
        pokemon = json.load(f)
    if pokemon[pkmn]['stats']['speed'] >= pokemon[epkmn]['stats']['speed']:
        move(moven, pkmn, text2, health)
        enemy_attack(text2)
    elif pokemon[pkmn]['stats']['speed'] <= pokemon[epkmn]['stats']['speed']:
        enemy_attack(text2)
        move(moven, pkmn, text2, health)
    
    else:
        wmf = random.randint(1,2)
        if wmf == 1:
            move(moven, pkmn, text2, health)
            enemy_attack(text2)
        elif wmf == 2:
            enemy_attack(text2)
            move(moven, pkmn, text2, health)
    
    if ehealth == 0 or ehealth <= 0:
        victory_you()
    elif health == 0 or health <= 0:
        enemy_victory()
            


def move(moven : int, pkmn, text2, health):
    global ehealth
    global moves
    with open("pokemon.json") as f:
        pokemon = json.load(f)
    move = moves[moven]
    hit = random.randint(0, 100)
    if hit <= pokemon[pkmn]['moves'][move]['accuracy'] or hit == pokemon[pkmn]['moves'][move]['accuracy']:
        damage = calcStrength(pokemon[pkmn]['moves'][move]['damage'], pkmn, epkmn)
        ehealth -= damage
        text2.insert(END, 'YOU : {} used {} doing {} damage ({} health remains)\n'.format(pkmn, move, damage, ehealth))
    else:
        text2.insert(END, 'YOU : {} used {}, and missed\n'.format(pkmn, move))
        
def calcStrength(damage, pkmn, epkmn):
    with open("pokemon.json") as f:
        pokemon = json.load(f)
    strenthMultiplier = pokemon[pkmn]['stats']['strength']
    defenseMultiplier = pokemon[epkmn]['stats']['defense']
    damageDone = round(damage * strenthMultiplier / defenseMultiplier)
    print(damage * strenthMultiplier)
    return damageDone


def enemy_attack(text2):

    global epkmn
    global pkmn
    global health
    global ehealth
    
    with open("pokemon.json") as f:
        pokemon = json.load(f)

    moven = random.randint(1,4)
    count = 1
    for key in pokemon[epkmn]['moves']:
        if count == moven:
            hit = random.randint(0, 100)
            if hit <= pokemon[epkmn]['moves'][key]['accuracy'] or hit == pokemon[epkmn]['moves'][key]['accuracy']:
                damage = calcStrength(pokemon[epkmn]['moves'][key]['damage'], epkmn, pkmn)
                health -= damage
                text2.insert(END, 'ENEMY : {} used {} doing {} damage ({} health remains)\n'.format(epkmn, key, damage, health))
            else:
                text2.insert(END, 'ENEMY : {} used {}, and missed\n'.format(epkmn, key))
        count += 1
    if health <= 1:
        enemy_victory()
    
    

    
def choose():
    global ehealth
    global health
    global epkmn
    global pkmn
    
    with open("pokemon.json") as f:
        pokemon = json.load(f)

        aopkmn = sum(1 for key in pokemon) - 1
        
        pid = 0
        for key in pokemon:
            print("Name", key, "| Id:", pid)
            pid += 1
    while not pkmn in pokemon:
        pkmn = str(input("Please select a pokemon: "))

    health += pokemon[pkmn]['stats']['health']

    print(aopkmn)
    nepkmn = random.randint(0, aopkmn)
    print("Right here", nepkmn)
    pid2 = 0
    for key in pokemon:
        print(key, pid2)
        if nepkmn == pid2:
            epkmn = key
            ehealth = pokemon[key]['stats']['health']
        pid2 += 1

    print("This should have a value >> ", epkmn)

    fight()

def fight():
    global ehealth
    global epkmn
    global health
    global window
    
    window = Tk()


    with open("pokemon.json") as f:
        pokemon = json.load(f)
        for key in pokemon[pkmn]['moves']:
            moves.append(key)
                
    print(moves[0])
        
    text2 = Text(window, height=20, width=50)
    scroll = Scrollbar(window, command=text2.yview)
    text2.pack()

    text2.insert(END, "You :  Go {} ({} health)\n".format(pkmn, health))
    text2.insert(END, "Enemy :  Go {} ({} health)\n".format(epkmn, ehealth))


    Button(window, text=moves[0], command= lambda *args: whofirst(0, pkmn, epkmn, text2)).pack()
    Button(window, text=moves[1], command= lambda *args: whofirst(1, pkmn, epkmn, text2)).pack()
    Button(window, text=moves[2], command= lambda *args: whofirst(2, pkmn, epkmn, text2)).pack()
    Button(window, text=moves[3], command= lambda *args: whofirst(3, pkmn, epkmn, text2)).pack()




choose()
