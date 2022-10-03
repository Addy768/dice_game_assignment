'''Hi player welcome to the to WIzard fighting game this game is inspired by Legendary movie series Harry potter.
This game will let you experience the chronicles of harry potter through a adventarous text based game.
SO SHALL WE BEGIN?? OR YOU ARE SCARED'''

from ast import If
from cgi import print_arguments
import random
from os import system
import os
import time

##dice
import random
from unicodedata import name
 
 
x = "y"
  
while x == "y":
     

    #CHARACTERS ACCORDING TO YOU RESULT
    '''
    
       1= Harry Potter
       2= Rupert Grint
       3= Hermione Granger
       4= Draco Malfoy
       5= Rubeus Hagrid
       6= Albus Dumbledore'''




    no = random.randint(1,6)
     
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if no == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if no == 3:
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
    if no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if no == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
         
    x=input("press y to roll again and n to exit:")
    print("\n")



#animating the welcome text for game

wizard="""
 __          __  _                           __          ___                  _ 
 \ \        / / | |                          \ \        / (_)                | |
  \ \  /\  / /__| | ___ ___  _ __ ___   ___   \ \  /\  / / _ ______ _ _ __ __| |
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   \ \/  \/ / | |_  / _` | '__/ _` |
    \  /\  /  __/ | (_| (_) | | | | | |  __/    \  /\  /  | |/ / (_| | | | (_| |
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|     \/  \/   |_/___\__,_|_|  \__,_
"""
witch="""
 __          __  _                           __          ___ _       _     
 \ \        / / | |                          \ \        / (_) |     | |    
  \ \  /\  / /__| | ___ ___  _ __ ___   ___   \ \  /\  / / _| |_ ___| |__  
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \   \ \/  \/ / | | __/ __| '_ \ 
    \  /\  /  __/ | (_| (_) | | | | | |  __/    \  /\  /  | | || (__| | | |
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|     \/  \/   |_|\__\___|_| |_|
                                                                           
                                                                           
"""

logo="""
 __    __  ____  _____   ____  ____   ___        _____  ____   ____  __ __  ______       ____   ____  ___ ___    ___ 
|  |__|  ||    ||     | /    ||    \ |   \      |     ||    | /    ||  |  ||      |     /    | /    ||   |   |  /  _]
|  |  |  | |  | |__/  ||  o  ||  D  )|    \     |   __| |  | |   __||  |  ||      |    |   __||  o  || _   _ | /  [_ 
|  |  |  | |  | |   __||     ||    / |  D  |    |  |_   |  | |  |  ||  _  ||_|  |_|    |  |  ||     ||  \_/  ||    _]
|  `  '  | |  | |  /  ||  _  ||    \ |     |    |   _]  |  | |  |_ ||  |  |  |  |      |  |_ ||  _  ||   |   ||   [_ 
 \      /  |  | |     ||  |  ||  .  \|     |    |  |    |  | |     ||  |  |  |  |      |     ||  |  ||   |   ||     |
  \_/\_/  |____||_____||__|__||__|\_||_____|    |__|   |____||___,_||__|__|  |__|      |___,_||__|__||___|___||_____|
                                                                                                                     
"""
user_win="""
____    ____  ______    __    __     ____    __    ____  ______   .__   __. 
\   \  /   / /  __  \  |  |  |  |    \   \  /  \  /   / /  __  \  |  \ |  | 
 \   \/   / |  |  |  | |  |  |  |     \   \/    \/   / |  |  |  | |   \|  | 
  \_    _/  |  |  |  | |  |  |  |      \            /  |  |  |  | |  . `  | 
    |  |    |  `--'  | |  `--'  |       \    /\    /   |  `--'  | |  |\   | 
    |__|     \______/   \______/         \__/  \__/     \______/  |__| \__| 
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            
                                                                            
"""

draw="""
 _______  .______          ___   ____    __    ____ 
|       \ |   _  \        /   \  \   \  /  \  /   / 
|  .--.  ||  |_)  |      /  ^  \  \   \/    \/   /  
|  |  |  ||      /      /  /_\  \  \            /   
|  '--'  ||  |\  \----./  _____  \  \    /\    /    
|_______/ | _| `._____/__/     \__\  \__/  \__/     
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
"""
enemy_win="""
 _______ .__   __.  _______ .___  ___. ____    ____    ____    __    ____  ______   .__   __. 
|   ____||  \ |  | |   ____||   \/   | \   \  /   /    \   \  /  \  /   / /  __  \  |  \ |  | 
|  |__   |   \|  | |  |__   |  \  /  |  \   \/   /      \   \/    \/   / |  |  |  | |   \|  | 
|   __|  |  . `  | |   __|  |  |\/|  |   \_    _/        \            /  |  |  |  | |  . `  | 
|  |____ |  |\   | |  |____ |  |  |  |     |  |           \    /\    /   |  `--'  | |  |\   | 
|_______||__| \__| |_______||__|  |__|     |__|            \__/  \__/     \______/  |__| \__| 
                                                                                              
                                                                                              
                                                                                              
                                                                                              
                                                                                              
                                                                                              
                                                                                              
                                                                                              
"""
comp_spells_easy=["Bat-Bogey Hex","Incarcerous","Confringo","Bombarda","Expulso"
        ,"Petrificus Totalus","Levicorpus","Rictusempra","Sectumsempra","Stupefy","Enneverate","Episkey","Liberacorpus","Rennervate",
        "Expelliarmus","Impedimenta","Langlock","Protego"]
comp_spells_hard=["Bat-Bogey Hex","Incarcerous","Confringo","Bombarda","Expulso"
        ,"Petrificus Totalus","Levicorpus","Rictusempra","Sectumsempra","Stupefy","Enneverate","Episkey","Liberacorpus","Rennervate",
        "Expelliarmus","Impedimenta","Langlock","Protego","Imperio","Crucio","Avada-Kedavara"]
attack_spells=["Bat-Bogey Hex","Incarcerous","Confringo","Bombarda","Expulso"
        ,"Petrificus Totalus","Levicorpus","Rictusempra","Sectumsempra","Stupefy"
        
        ]
healing_spells=["Enneverate","Episkey","Liberacorpus","Rennervate"]
defense_spells=["Expelliarmus","Impedimenta","Langlock","Protego"]
unforgivable_curses=["Imperio","Crucio","Avada-Kedavara"]
user_health=100
comp_health=100
comp_spell=""
should_continue=True
def exit_game():
    global should_continue
    should_continue=False
    

    
    
def game(name):
    global comp_health
    global user_health
    global difficulty
    damage=random.randint(1, 20)
    health=random.randint(1,20)
    if difficulty=="easy":
        comp_spell=random.choice(comp_spells_easy)
    else:
        comp_spell=random.choice(comp_spells_hard)
    
    user_spell=input("\n\nChoose a spell to fight your enemy: ").lower()
    if user_spell>="0" and user_spell<="9":
        print(f"\n\n{name} attacked with {attack_spells[int(user_spell)-1]}")
        print("Damage Dealt to Enemy")
        comp_health-=damage
        #print(comp_health)
    elif user_spell>="a" and user_spell<="d":
        print(f"\n\n{name} healed themselves with {user_spell}")
        print("Health Healed")
        user_health+=health
        #print(user_health)
    if user_spell>="e"and user_spell<="h" and comp_spell in attack_spells:
        print(f"\n\nEnemy attacked with {comp_spell} which {name} defended with {user_spell}")
        print(f"0 Damage done to you")
        print("0 Damage Done to you")
    if comp_spell in attack_spells:
        print(f"\n\nEnemy attacked with {comp_spell}")
        print("Damage dealt to You")
        user_health-=damage