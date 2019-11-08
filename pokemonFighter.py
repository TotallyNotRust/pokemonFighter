import json
import random
from tkinter import *
import time
import random

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

def move1(pkmn, text2, health, enemyhealth):
    global ehealth
    with open("pokemon.json") as f:
        pokemon = json.load(f)
    moves = getmoves(pkmn)
    move = moves[0]
    damage = pokemon[pkmn]['moves'][move]['damage']
    hit = random.randint(0, 100)
    if hit <= pokemon[pkmn]['moves'][move]['accuracy'] or hit == pokemon[pkmn]['moves'][move]['accuracy']:
        damage = pokemon[pkmn]['moves'][move]['damage']
        enemyhealth -= damage
        text2.insert(END, 'YOU : {} used {} doing {} damage ({} health remains)\n'.format(pkmn, move, damage, enemyhealth))
        ehealth = enemyhealth
    else:
        text2.insert(END, 'YOU : {} used {}, and missed\n'.format(pkmn, move))
    if not ehealth <= 1:
        enemy_attack(text2)
    else:
        victory_you()
        
                
def move2(pkmn, text2, health, enemyhealth):
    global ehealth
    with open("pokemon.json") as f:
        pokemon = json.load(f)
    moves = getmoves(pkmn)
    move = moves[1]
    damage = pokemon[pkmn]['moves'][move]['damage']
    hit = random.randint(0, 100)
    if hit <= pokemon[pkmn]['moves'][move]['accuracy'] or hit == pokemon[pkmn]['moves'][move]['accuracy']:
        damage = pokemon[pkmn]['moves'][move]['damage']
        enemyhealth -= damage
        text2.insert(END, 'YOU : {} used {} doing {} damage ({} health remains)\n'.format(pkmn, move, damage, enemyhealth))
        ehealth = enemyhealth
    else:
        text2.insert(END, 'YOU : {} used {}, and missed\n'.format(pkmn, move))
    if not ehealth <= 1:
        enemy_attack(text2)
    else:
        victory_you()
        

def move3(pkmn, text2, health, enemyhealth):
    global ehealth
    with open("pokemon.json") as f:
        pokemon = json.load(f)
    moves = getmoves(pkmn)
    move = moves[2]
    damage = pokemon[pkmn]['moves'][move]['damage']
    hit = random.randint(0, 100)
    if hit <= pokemon[pkmn]['moves'][move]['accuracy'] or hit == pokemon[pkmn]['moves'][move]['accuracy']:
        damage = pokemon[pkmn]['moves'][move]['damage']
        enemyhealth -= damage
        text2.insert(END, 'YOU : {} used {} doing {} damage ({} health remains)\n'.format(pkmn, move, damage, enemyhealth))
        ehealth = enemyhealth
    else:
        text2.insert(END, 'YOU : {} used {}, and missed\n'.format(pkmn, move))
    if not ehealth <= 1:
        enemy_attack(text2)
    else:
        victory_you()
    

def move4(pkmn, text2, health, enemyhealth):
    global ehealth
    with open("pokemon.json") as f:
        pokemon = json.load(f)
    moves = getmoves(pkmn)
    move = moves[3]
    hit = random.randint(0, 100)
    if hit <= pokemon[pkmn]['moves'][move]['accuracy'] or hit == pokemon[pkmn]['moves'][move]['accuracy']:
        damage = pokemon[pkmn]['moves'][move]['damage']
        enemyhealth -= damage
        text2.insert(END, 'YOU : {} used {} doing {} damage ({} health remains)\n'.format(pkmn, move, damage, enemyhealth))
        ehealth = enemyhealth
    else:
        text2.insert(END, 'YOU : {} used {}, and missed\n'.format(pkmn, move))
    if not ehealth <= 1:
        enemy_attack(text2)
    else:
        victory_you()


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
                damage = pokemon[epkmn]['moves'][key]['damage']
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
        pid = 0
        for key in pokemon:
            print("Name", key, "| Id:", pid)
            pid += 1
    while not pkmn in pokemon:
        pkmn = str(input("Please select a pokemon: "))

    health += pokemon[pkmn]['stats']['health']

    aopkmn = sum(1 for key in pokemon)
    print(aopkmn)
    nepkmn = random.randint(1, aopkmn)
    pid2 = 1
    for key in pokemon:
        print(key)
        if nepkmn == pid:
            epkmn = key
            ehealth += pokemon[key]['stats']['health']
            pid += 1
        pid2 += 1

    print(epkmn)

    fight()

def fight():
    global ehealth
    global health
    global window
    
    window = Tk()


    moves = getmoves(pkmn)
                
    print(moves[0])
        
    text2 = Text(window, height=20, width=50)
    scroll = Scrollbar(window, command=text2.yview)
    text2.pack()

    text2.insert(END, "You :  Go {} ({} health)\n".format(pkmn, health))
    text2.insert(END, "Enemy :  Go {} ({} health)\n".format(epkmn, ehealth))


    Button(window, text=moves[0], command= lambda *args: move1(pkmn, text2, health, ehealth)).pack()
    Button(window, text=moves[1], command= lambda *args: move2(pkmn, text2, health, ehealth)).pack()
    Button(window, text=moves[2], command= lambda *args: move3(pkmn, text2, health, ehealth)).pack()
    Button(window, text=moves[3], command= lambda *args: move4(pkmn, text2, health, ehealth)).pack()




def getmoves(pkmn):
    with open("pokemon.json") as f:
        pokemon = json.load(f)
            
    for key in pokemon[pkmn]['moves']:
        moves.append(key)
        print(moves)
    return moves

choose()    
