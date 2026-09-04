# Function Definitions
import random
import time
import textwrap

TEXT_WIDTH = 100

def say(text):
    text = str(text)

    # Multi-line strings are ASCII/layout blocks and are already formatted.
    if "\n" in text:
        print(text)
        return

    if len(text) <= TEXT_WIDTH:
        print(text)
        return

    print(textwrap.fill(
        text,
        width=TEXT_WIDTH,
        break_long_words=False,
        break_on_hyphens=False
    ))

def wake_up(name):
    say(f"{name} wakes up in a dark room.")


death_announced = False

def continued(name, health):
        global death_announced
        if health <= 0:
            if not death_announced:
                print(fr"""
                                            {name} has died
                                                 _______
                                               /         \
                                              |  X     X  |
                                              |     ^     |
                                              |   _____   |
                                               \ |_____| /
                                                \_______/
                                                 /|   |\
                                                /_|___|_\
                                                   RIP
                """)
                death_announced = True
            return False
        else: 
             return True


def fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, enemy_name, enemy_health, enemy_damage):
        defending = False
        escaped = False
        if inventory.get("rusty breastplate", 0) >= 1:
            armoured = True
        else:
            armoured = False
        say(f"{player_name}'s health is {health}")
        while health > 0 and enemy_health > 0:
                say(f"The {enemy_name}'s health is {enemy_health}")
                action = input("Choose: attack, heal, defend, or run: ")
                if action == "attack":
                    say(f"{player_name} attacks the {enemy_name}")
                    enemy_health = enemy_health - player_damage
                elif action == "heal":
                    if inventory.get("potions") >= 1:
                        health = min(health + potion_healing, max_health)
                        inventory["potions"] = inventory["potions"] -1
                        say(f"{player_name} has used a healing potion, {player_name} health is now {health}")
                        say(f"{player_name} has {inventory["potions"]} healing potions left.")
                    else:
                        say(f"{player_name} does not appear to have any healing potions.")
                elif action == "defend":
                        say(f"{player_name} braces for the attack")
                        defending = True
                elif action == "run":
                    escaped = True
                    say(f"{player_name} managed to escape the enemy. Phew!")
                    time.sleep(2)
                    break
                if enemy_health <= 0:
                    say(f"{player_name} has defeated {enemy_name}.")
                    break
                say(f"{enemy_name} hits {player_name}")
                if armoured and defending:
                     health = health
                elif armoured:
                     health = health - enemy_damage // 2
                elif defending:
                     health = health - enemy_damage // 2
                else:
                     health = health - enemy_damage
                defending = False 
                say(f"{player_name}'s health is {health}")
                if health <= 0:
                    break
            
        return health, enemy_name, escaped

def broke_bitch(player_name):
    print(fr"""
                         ____________________________________________________
                        |,---.        ) No Money, Sad Clown  (          ,---.|
                        |) 1 (        `====---    _   ---===='          ) 1 (|
                        | \ /                    | |                     \ / |
                        |  V      ,-.            |-|                      V  |
                        |        ( D )          _|-|_         good  for      |
                        |         `-'         _(_) (_)           N O         |
                        |                    (_) | | L_.       c-l-u-e       |
                        |      M21141815E    '      (_  \                    |
                        | / \               (        /  /                / \ |
                        |( 1 )                                          ( 1 )|
                        | \ / ---==<   B R O K E    B I T C H    >==---  \ / |
                        |____________________________________________________|

                        I'm sorry it looks like {player_name} is a broke bitch.
                                  Try again or select continue.
    """)

def press_y():
    while True:
        key = input("Press Y to continue: ").lower()
        if key == "y":
            break
        else:
            say("It's in the middle of they keyboard under the numbers.... looks like this.... Y...")


def buy(player_name, inventory, store, player_damage):
    say(f"I currently have: {store["stock"]["potion"]} potions for {store["price"]["potion"]} gold coins, {store["stock"]["lock pick"]} lockpicks for {store["price"]["lock pick"]} gold coins, {store["stock"]["rusty breastplate"]} rusty breastplate's for {store["price"]["rusty breastplate"]} gold coins, {store["stock"]["pointy stick"]} pointy stick's for {store["price"]["pointy stick"]} gold coins and {store["stock"]["shiny paper"]} shiny paper's for {store["price"]["shiny paper"]} gold coins.")
    while True:
        say(f"{player_name} has {inventory["gold coin"]} Gold Coins.")
        purchase = input("Select: Potion, Lock Pick, Rusty Breastplate, Pointy Stick, Shiny Paper, Continue:").lower()
        if purchase == "potion":
           if store["stock"]["potion"] >= 1:
               if inventory["gold coin"] >= 50:
                    store["stock"]["potion"] = store["stock"]["potion"] -1
                    inventory["potions"] = inventory["potions"] +1
                    inventory["gold coin"] = inventory["gold coin"] -50
                    say(f"{player_name} has successfully purchased healing potion.")
                 
               else:
                   broke_bitch(player_name)

           else:
               say("I'm out of stock right now, come back later.")

        elif purchase == "lock pick":
            if store["stock"]["lock pick"] >= 1:
                if inventory["gold coin"] >= 25:
                    store["stock"]["lock pick"] = store["stock"]["lock pick"] -1
                    inventory["lock pick"] = 1
                    inventory["gold coin"] = inventory["gold coin"] -25
                    say(f"{player_name} has successfully purchased lock pick.")
                else: 
                    broke_bitch(player_name)
            else:
                say("I'm out of stock right now, come back later.")

        elif purchase == "rusty breastplate":
           if store["stock"]["rusty breastplate"] >= 1:
               if inventory["gold coin"] >= 150:
                store["stock"]["rusty breastplate"] = store["stock"]["rusty breastplate"] -1
                inventory["rusty breastplate"] = 1
                inventory["gold coin"] = inventory["gold coin"] -150
                defending = True
                say(f"{player_name} has successfully purchased healing Rusty Breastplate.")
               else: 
                broke_bitch(player_name) 
           else:
               say("I'm out of stock right now, come back later.")

        elif purchase == "pointy stick":
           if store["stock"]["pointy stick"] >= 1:
               if inventory["gold coin"] >= 25:
                store["stock"]["pointy stick"] = store["stock"]["pointy stick"] -1
                inventory["pointy stick"] = 1
                player_damage = 30
                inventory["gold coin"] = inventory["gold coin"] -25
                say(f"{player_name} has successfully purchased Pointy Stick.")
               else: 
                broke_bitch(player_name) 
           else:
                say("I'm out of stock right now, come back later.")

        elif purchase == "shiny paper":
           if store["stock"]["shiny paper"] >= 1:
               if inventory["gold coin"] >= 50:
                store["stock"]["shiny paper"] = store["stock"]["shiny paper"] -1
                inventory["shiny paper"] = 1
                inventory["gold coin"] = inventory["gold coin"] -50
                say(f"{player_name} has successfully purchased Shiny Paper.")
               else: 
                broke_bitch(player_name) 
           else:
               say("I'm out of stock right now, come back later.")

        elif purchase == "continue":
             return player_name, inventory, store, player_damage
             break
        else:
             say("Oh dear, You've had an aneurysm.... When you're feeling up to it, try a valid response.")


def menu(player_name, health, inventory, player_damage, potion_healing, max_health, description):
    while True:
        choice = input("Use Menu: Yes, or No: ").lower()
        if choice == "yes":
            while True:
                options = input("Select: Inventory, Stats, Heal or Continue: ").lower()

                if options == "inventory":
                    for item, quantity in inventory.items():
                       if quantity > 0:
                           say(f"{item}: {quantity}.")
                    selected_item = input("Inspect an item: ").lower()
                    if inventory.get(selected_item, 0) >= 1:
                        say(f"{description[selected_item]}")
                        if selected_item == "potions":
                            if inventory.get("potions") >= 1:
                                healies = input("Use Potion Now: Yes or No: ").lower()
                                if healies == "yes":
                                    health = min(health + potion_healing, max_health)
                                    inventory["potions"] = inventory["potions"] -1
                                    say(f"{player_name} has used a healing potion, {player_name} health is now {health}")
                                    say(f"{player_name} has {inventory["potions"]} healing potions left.")
                    if selected_item == "continue":
                        break                      
                    else:
                        say(f"{player_name} would you like a link to a typing lesson? Could be fun.... definitely neccessary at this point.")
                elif options == "stats":
                    say(f"{player_name}'s health is {health}, and {player_name} attack is {player_damage}.")
                    continue
                elif options == "heal":
                    if inventory.get("potions") >= 1:
                        health = min(health + potion_healing, max_health)
                        inventory["potions"] = inventory["potions"] -1
                        say(f"{player_name} has used a healing potion, {player_name} health is now {health}")
                        say(f"{player_name} has {inventory["potions"]} healing potions left.")
                elif options == "continue":
                    return health, inventory
                    break
                else:
                    say("This one is a clear case of PEBKAC....")
        elif choice == "no":
            return health, inventory
        else:
            say("This one is a clear case of PEBKAC....")

def game():
    global death_announced
    death_announced = False
    # Starting Game State

    max_health = 100
    health = max_health
    enemy_health = 100
    player_damage = 25
    enemy_damage = 20
    inventory = {
        "gold coin": 50,
        "potions": 3,
        "rusty key": 0,
        }
    potion_healing = 30
    store = {
            "stock": {
                "potion": 2,
                "lock pick": 3,
                "rusty breastplate": 1,
                "pointy stick": 1,
                "shiny paper": 3,
            },
            "price": {
                "potion": 50,
                "lock pick": 25,
                "rusty breastplate": 150,
                "pointy stick": 25,
                "shiny paper": 50,
            }
            }
    description = {
        "gold coin": r"""

                                         ,=-="'""'""=-=,,
                                     ,= -'  |\ |   /\   ` - =,
                                  ,="'|\    | \|  /__\   /\  `"=,
                                /"    |,"\  |  | /'  `\ /  )     "\
                              /"  ,"  |                 `\/    /|  "\
                             /'  |   ,                       /",|   `\
                            /'   ",/"                           |    `\
                           /'      I=I=I               ,d8ba,___      `\
                          /'     I=8=8=8=I_I_          88888P"'"       `\
                          |   xXXXXXXXXXXXXXXXxIxx    ,888"             |
                          | ~XXXXXXXXXXXXXXX~-~-~-~-~ d888~-~-~-~-~-~-~ |
                          | ~-~-~-~-~-~-~-~-,aad888ba,8888,-~-~-~-~-~-~ |
                          | ~-~-~-~-~-~-,ad888888888888888b-~-~-~-~-~-~ |
                          \ ~-~-~-~-~,ad8888888888888888888-~-~-~-~-~-~ /
                          `\ -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~- /'
                           `\ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~,-,~~~~~ /'
                            `\    /"\         1 9 9 4        \ /\    /'
                             `\  "\,/'                   |\   `\ `  /'
                               "\      /""\   |    |     |,'\     /"
                                 `"=,_ \__/   |__  |__   |    ,="'
                                    `""=,__             __,=""'
                                         `` "= = = = ="''

                          A Golden Coin. Used to trade for items of value.
                        Not made of chocolate... It hurt my teeth to bite it...""",
        "potions": r"""

                                               (
                                                )  )
                                            ______(____
                                           (___________)
                                            /         \
                                           /     |      \
                                          |    --+--     |
                                      ____\      |       /____
                                     ()____'.__     __.'____()
                                          .'` .'```'. `-.
                                         ().'`       `'.()

                               A brewed healing potion, made from herbs.
                               I'd pinch my nose if I had to drink it...


                          """,
        "rusty key": r"""

                                   8 8 8 8                     ,ooo.
                                   8a8 8a8                    oP   ?b
                                  d888a888zzzzzzzzzzzzzzzzzzzz8     8b
                                   `""^""'                    ?o___oP'

                                 A rusty key, I wonder what it opens...


                                """,

        "lock pick": r"""

                                                       \\       .-""-.
                                                        \\     / .--. \
                                                         \\   / /    \ \
                                                          \\  | |    | |
                                                           \\ | |.-""-.|
                               A specialy shaped           ///`.::::.`\
                              tool to pick locks.          ||| ::/  \:: ;
                                                           ||; ::\__/:: ;
                                                            \\\ '::::' /
                                                             `=':-..-'`


                       """,

        "rusty breastplate": r"""

                                           .=-'\   /`-=.
                                         .'\   (`:')   /`.
                                       _/_ |_.-' : `-._|__\_
                                      <___>'\    :   / `<___>
                                             >=-=-=-=<
                                            /  ,-:-.  \
                                           |__/v^v^v\__)


                                   A Rusty Breastplate, surely it can
                                       still help in some way?


                            """,

 
        "pointy stick": r"""

                                             ,@@@@@@@,
                                    ,,,.   ,@@@@@@/@@,  .oo8888o.
                                  ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
                                 ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
                                  %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
                                  %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
                                  `&%\ ` /%&'    |.|        \ '|8'
                                      |o|        | |         | |
                                      |.|        | |         | |
                                \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_

                                 A Pointy Stick, probably fell from one
                                 of those big green things over there.
                                 It hurts if I poke my eye with it.....


            """,

        "shiny paper": r"""


                                    88888b.  8888b. 88888b.  .d88b. 888d888
                                    888 "88b    "88b888 "88bd8P  Y8b888P"
                                    888  888.d888888888  88888888888888
                                    888 d88P888  888888 d88PY8b.    888
                                    88888P" "Y88888888888P"  "Y8888 888
                                    888             888
                                    888             888
                                    888             888

                                 Bit like this only shinier....
                             Has a turtle scribbled on it in ketchup...


                               """,

        "silver dagger": r"""

                                              ____
                                             (____)
                                             /____\
                                             |___.-~-.-~-.
                                             |__(  __|__  )_
                                             |/ \/\_/^\._)/ \
                                            (  (__{(@)}\_)  )
                                             |\_/ (/(_)\_))_/
                                             ______|_(  (__)_)_/ )
                                            /_________\_/  |  \_/
                                            |/   /' |\  /'-~'~-'\|
                                            |  (| \/ |
                                            |   `\   |
                                             `\  `\  |    ___
                                              `\  `\|  /' ..'>
                                                ___`\  `\: ,' /'
                                          /' _ /''`\  '__'
                                         < .'./'   |  |
                                          `~' |    |  |
                                              |    |/'
                                              |    |
                                              |    |
                                              |    |
                                               \  /
                                                \/


                              If you have this, you are one lucky ducky.
                              With the style of a coding clown, you pulled
                                    a 2/5 chance to SLAY QUEEN!!!


                                 """,


        "sophisticated hat": fr"""


                                                     _.--._
                                                _.-.'      `.-._
                                               .' ./`--...--' \  `.
                                      .-.      `.'.`--.._..--'   .'
                                   _..'.-.`-._.'( (-..__    __..-'
                                    >.'   `-...' ) )    ````
                                    '           / /
                                           .._.'.'
                                            >.-'
                                             '

                                A very Sophisticated Hat, and no-one
                                   could pull it off like you!
                                Bonus: This hat is Shorty approved,
                              permamenent increase to death circle skill.


                                          """,
        "dinted broadsword": fr"""
                                       ___
                                      ( ((
                                       ) ))
              .::.                    / /(
             'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
            (J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
             `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
              `::'                    \ \(
                                       ) ))
                                      (_((

                            Dinted from battle, This heavy sword can still pack a punch.
                            """,
        
        "mysterious green leaf": fr"""

                                               .
                                               M
                                              dM
                                              MMr
                                             4MMML                  .
                                             MMMMM.                xf
                             .              "MMMMM               .MM-
                              Mh..          +MMMMMM            .MMMM
                              .MMM.         .MMMMML.          MMMMMh
                               )MMMh.        MMMMMM         MMMMMMM
                                3MMMMx.     'MMMMMMf      xnMMMMMM"
                                '*MMMMM      MMMMMM.     nMMMMMMP"
                                  *MMMMMx    "MMMMM\    .MMMMMMM=
                                   *MMMMMh   "MMMMM"   JMMMMMMP
                                     MMMMMM   3MMMM.  dMMMMMM            .
                                      MMMMMM  "MMMM  .MMMMM(        .nnMP"
                          =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*
                            "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"
                             "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""
                               ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"
                                  *PMMMMMMhn. *x > M  .MMMM**""
                                     ""**MMMMhx/.h/ .=*"
                                              .3P"%....
                                            nP"     "*MMnx

                            A mysterious green leaf with magical properties.
                            Often associated with numbers linked to teens
                           meeting in a field to hunt for fields of this leaf.
               """



    }
    #Game Script

    player_name = input("What is your name? ")
    wake_up(player_name)
    wake_up("Ghoulish Ogre")
    health, enemy_name, escaped = fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, "Ghoulish Ogre", 100, 20)
    if not continued(player_name, health):
        return "death"
    if continued(player_name, health):
    
        if escaped == True:
            pass
        else: 
            say(f"{enemy_name} has dropped a rusty key")
            say(f"{player_name} put the rusty key in thier inventory")
            inventory["rusty key"] = 1
        health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)
        print(f"""                            The path ahead is clear.
                                              You walk down a dark hallway.
                                              At the end are two doors:
                                              +----------+     +----------+
                                              |          |     |          |
                                              |   LEFT   |     |  RIGHT   |
                                              |       O  |     |  O       |
                                              |          |     |          |
                                              +----------+     +----------+
        """)
        while True:
            door = input("Choose: Left, Right: ").lower()
            if door == "left":
                print(fr"""               {player_name} reaches for the Left door handle.
                                                  The door slowly creaks open....
                               {player_name} finds themselves in the middle of a small treasure room.
   *******************************************************************************
            |                   |                  |                     |
   _________|________________.=""_;=.______________|_____________________|_______
   |                   |  ,-"_,=""     `"=.|                  |
   |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
   _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
   |                   |    __.--" , ; `"=._o." ,-""-._ ".   |
   |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
   _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
   |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
   |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
   ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
   /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
   ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
   /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
   ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
                    """)

                if inventory["rusty key"] >= 1:
                    print(fr"""
                          {player_name} uses the rusty key in their inventory.
                           dust falls off the lid as the chest opens.""")
                    press_y()
                    inventory["rusty key"] = inventory["rusty key"] -1
                    dagger_chance = random.randint(1, 10)
                    if dagger_chance <= 3:
                        inventory["silver dagger"] = 1
                        player_damage = 35

                    inventory["gold coin"] = 200
                
                    inventory["sophisticated hat"] = 1
                    print(inventory)
                    print(fr"""
     {player_name} Looks rather smart with their new hat, if only it actually helped defense rather
     then just style.
                         .----.
                        /  _   \
                        |=[_]==|
                    (`.--.____.---.'\
                        `-./'\\_.'
                       |  /.  .||
                         \:-: .'
                          `-'
                        """)
                    press_y()
                    break
                else:
                    print(fr"""
                                  Where you in a rush and forget to loot the ogre?
                                    _
                                   | |
                      ___  __ _  __| |_ __   ___  ___ ___
                     / __|/ _` |/ _` | '_ \ / _ \/ __/ __|
                     \__ \ (_| | (_| | | | |  __/\__ \__ \
                     |___/\__,_|\__,_|_| |_|\___||___/___/
                            """)
                    time.sleep(3)
                    break
            elif door == "right":
                say(f"{player_name} grasps the Right door handle")
                say(f"{player_name} is suddenly faced with a Vile Goblin.")
                health, enemy_name, escaped = fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, "Vile Goblin", 50, 25)
                if not continued(player_name, health):
                    return "death"
                if escaped == False:
                    inventory["gold coin"] = inventory["gold coin"] +100
               
                break

            else:
                print(r"""
                               That isn't a valid door. Please try again.
                                              .-'''''''-.
                                            .'           '.
                                           /   _       _   \
                                          |   (_)     (_)   |
                                          |       /\        |
                                          |      /  \       |
                                           \    |____|     /
                                            |  /| || |\   |
                                            | | | || | |  |
                                             \|_|_||_|_|_/
                                              '--------'
                     """)

    if continued(player_name, health):
        health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)
        say(f"{player_name} is staring down a long dimly lit hallway")
        say("The dim yellow light flickers as a cold gust blows towards you.")
        while True:
            path = input("Choice: Continue, Wait: ").lower()
            if path == "continue":
                print(fr"""
               88888888888888888888888888888888888888888888888888888888888888888888888
               88.._|      | `-.  | `.  -_-_ _-_  _-  _- -_ -  .'|   |.'|     |  _..88
               88   `-.._  |    |`!  |`.  -_ -__ -_ _- _-_-  .'  |.;'   |   _.!-'|  88
               88      | `-!._  |  `;!  ;. _______________ ,'| .-' |   _!.i'     |  88
               88..__  |     |`-!._ | `.| |_______________||."'|  _!.;'   |     _|..88
               88   |``"..__ |    |`";.| i|_|MMMMMMMMMMM|_|'| _!-|   |   _|..-|'    88
               88   |      |``--..|_ | `;!|l|MMoMMMMoMMM|1|.'j   |_..!-'|     |     88
               88   |      |    |   |`-,!_|_|MMMMP'YMMMM|_||.!-;'  |    |     |     88
               88___|______|____!.,.!,.!,!|d|MMMo * loMM|p|,!,.!.,.!..__|_____|_____88
               88      |     |    |  |  | |_|MMMMb,dMMMM|_|| |   |   |    |      |  88
               88      |     |    |..!-;'i|r|MPYMoMMMMoM|r| |`-..|   |    |      |  88
               88      |    _!.-j'  | _!,"|_|M)(MMMMoMMM|_||!._|  `i-!.._ |      |  88
               88     _!.-'|    | _."|  !;|1|MbdMMoMMMMM|l|`.| `-._|    |``-.._  |  88
               88..-i'     |  _.''|  !-| !|_|MMMoMMMMoMM|_|.|`-. | ``._ |     |``"..88
               88   |      |.|    |.|  !| |u|MoMMMMoMMMM|n||`. |`!   | `".    |     88
               88   |  _.-'  |  .'  |.' |/|_|MMMMoMMMMoM|_|! |`!  `,.|    |-._|     88
               88  _!"'|     !.'|  .'| .'|[@]MMMMMMMMMMM[@] \|  `. | `._  |   `-._  88
               88-'    |   .'   |.|  |/| /                 \|`.  |`!    |.|      |`-88
               88      |_.'|   .' | .' |/                   \  \ |  `.  | `._    |  88
               88     .'   | .'   |/|  /                     \ |`!   |`.|    `.  |  88
               88  _.'     !'|   .' | /                       \|  `  |  `.    |`.|  88
               88888888888888888888888888888888888888888888888888888888888888888888888

                                 {player_name} comes to a door at the end of the hallway.

                """)
                say(f"A warmth emenates from the door. {player_name} cautiously reaches for the handle...")
                press_y()
                break
            elif path == "wait":
                say(f"{player_name} so.... you uh just enjoying the high end graphics?")
                say("Or is it the gripping story line that's got you contemplating life?")
                say(f"{player_name} shall we continue when your ready?")
                press_y()
            else:
                say("Sorry, That does not appear to be a valid response. Please Choose Continue.")


    print(fr"""

                                       _______________________
                                       \_____________________/
                                        \       __O__       /
                                         \      =(_)=      /              +
                        +                _\  ___________  /_         .  . . .
                         . . +          ( \\/ ___   ___.\// )       +.. .. .+
                         .. .. :         \    (o)) ((o)    /       ... .. . .
                         .. : .. .:. .    (_)    /   \    (_)      ..+.. + ...+
                         . .+ . ++. .       \:. (_   _) .:/         +  + :.. + :
                          . __... . +        )::::\_/::::(            :. __  . .
                          _(  \ __ .        (:::\_|_|_/:::)          __ /  )_
                         (  \  (  \      __  \:::\_|_/:::/  __      /  )  /  )
                          \  \  \  \    /  )  \:::::::::/  (  \    /  /  /  /
                         ( \  \  \  \__/  /    |\:::::/|    \  \__/  /  /  //)
                          \ \_ \_ \_     / ____| |___| |____ \     _/ _/ _/ /
                           \            /_/ ||   |___|   || \_\            /
                            \          /\   ||  (_____)  ||   /\          /
                             \________/ \\  ||___________||  // \________/
                ______________\\_______//    |___________|   \\______//_________________
                               \______/_:                   :_\______/

                                  You find a friendly Merchant.
                            {player_name} has {inventory["gold coin"]} gold coins.
          """)
    press_y()
    say("The merchant looks over and smiles")
    say(f"{player_name} would you like to browse my goods? I have a few things I think you might be interested in...")
    player_name, inventory, store, player_damage = buy(player_name, inventory, store, player_damage)
    health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)

    #second game state after common functions established and stable

    say(f"{player_name} takes the back door, and exits the merchant.")
    print(fr"""
                           In front of {player_name} is what seems to be a normal neighbourhood.
                                                                  ______________
                                                                 |##############
                      __             __                          |##############
        _____________|  |_____     _(   )                        |##############
        UUUUUUUUUUUUU|__|UUUUU| ,-'      )_                      |##############
        UUU_UUUUUU_UUUUUU_UUUU|(   (  /    )                     |   __   __   _
        UU|_|UUUU|_|UUUU|_|UUU|.  \   )  _) )                    |  |  | |  | |
        UUUUUUUUUUUUUUUUUUUUUU| `.  .    )  )                    |  |__| |__| |_
        ======================|(_   |  )  _)                     |
             __     __    __  |(__(_|____)_______________________|   __   __   _
        |   |__|   |__|  |__| |uuuuuuuuuuuuuuuuuuuuuuuuuuuu,'.uuu|  |  | |  | |
        |   |__|   |__|  |__| |uuuuuuuuuuuuuuuuuuuuuuuuuu,'   `.u|  |__| |__| |_
        ======================|uuuu_uuuuuu_uuuuuu_uuuuu,'__   __`.
             __     __    __  |uuu| |uuuu| |uuuu| |uuuu||  | |  ||   __   __   _
        |   |__|   |__|  |__| |uuu|_|uuuu|_|uuuu|_|uuuu||__| |__||  |  | |  | |
        |   |__|   |__|  |__| |=_====__================'         |  |__| |__| |_
        ======================||  | |  |  __   __   __   __   __ |______________
          ___  __    ________ ||__| |__| |  | |  | |  | |  | |  ||+++++++++++++_
        ||_|_||  |  |  |     || _______  |__| |__| |__| |__| |__||++.-------.+|
        ||_|_||- |  | -|     |||   |   |                         |++|   |   |+|_
         |_|_||  |  |  |_____|||   |o  |  _     ____________  _  |++|   |-  |+++
        ---. _|--|__|--|_____|||===|   |_|_|_  /_|__|_______| _|_|++|___|___|+++
        ----`. ___             ;---'---'      |  |_-|       |__     |       \
        --(_)-'_ _\___________/________|____/_'-(_)-----(_)-' _\____|________\__
        ________________________________________________________________________
                        """)
    press_y()
    say(f"{player_name} does not recognise the area.")
    print(r"""
                                        "Was I abducted?"
                           "why are there ogres, and goblins in suburbia???"
                               "And who was the drugged out merchant?"
                                "I need to find a way out of here.."
            """)
    press_y()
    say(f"A swarm of rats suddenly charges at {player_name}.")
    while True:
        leg_it = input("Select an Option: Fight or Leg It: ").lower()
        if leg_it == "fight":
            health, enemy_name, escaped = fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, "Stringy Rat", 50, 10)
            if not continued(player_name, health):
                return "death"
            health, enemy_name, escaped = fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, "Random Rat with Glasses", 50, 10)
            if not continued(player_name, health):
                return "death"
            health, enemy_name, escaped = fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, "Diseased Rat", 25, 20)
            if not continued(player_name, health):
                return "death"
            if continued(player_name, health):
                if escaped == False:
                    inventory["gold coin"] = inventory["gold coin"] +100
                    inventory["lock pick"] = inventory.get("lock pick", 0) +1
                    say(f"{player_name} has recieved 100 gold coins, and a lock pick.")
            break
        elif leg_it == "leg it":
            escaped = True
            say(f"{player_name} managed to escape the enemy. Phew!")
            break
        else:
            say(f"{player_name} appears a bit nervous. Slow down and type your answer deliberately.... It's only a few rodents....")
    print(fr"""
                                                          ,////,
                                                          /// 6|
                                                          //  _|
                                                         _/_,-'
                                                    _.-/'/   \   ,/;,
                                                 ,-' /'  \_   \ / _/
                                                 `\ /     _/\  ` /
                                                   |     /,  `\_/
                                                   |     \'
                                       /\_        /`      /\
                                     /' /_``--.__/\  `,. /  \
                                    |_/`  `-._     `\/  `\   `.
                                              `-.__/'     `\   |
                                                            `\  \
                                                              `\ \
                                                                \_\__
                                                                 \___)
                                  {player_name} is out of here before
                                       anymore Rats turn up....""")
    press_y()
    say(f"{player_name} comes across a dingy diner.")
    say(f"As if from a scene in the matrix, {player_name} see's their name with an arrow below all over the window.")
    say(r" 'Something Clearly Wants Me to Go Inside' ")
    say(f"{player_name} spots a sign saying, 'Rats are not welcome' ")
    print(r"""
                           "Did I follow My socks into another dimension?"
                                   "Who would need to state that?"
                        "It must be some sort of sign, maybe they can help me."
          """)
    say("The diner appears empty. Like everyone left in a rush, half eaten meals left on tables, the faint hum of the fans in the kitchen.")
    say(f"{player_name} checks the kitchen for staff.")
    press_y()
    print(r"""
                 ____________________________________________________________________
                /|    |__I__I__I__I__I__I__I__I__I_|       _-       %       %         |\
                 | _- |_I__I__I__I__I__I__I__I__I__|-_              %       %     _-  |
                 |    |__I__I__I__I__I__I__I__I__I_|                %       %         |
                 |  - |_I__I__I__I__I__I__I__I__I__|               ,j,      %w ,      |
                 | -  |__I__I__I__I__I__I__I__I__I_|  -_ -        / ) \    /%mMmMm.   |
                 |    |_I__I__I__I__I__I__I__I__I__|             //|  |   ;  `.,,'    |
                 |-_- /                            \             w |  |   `.,;`       |
                 |   /                              \    -_       / ( |    ||         |
                 |  /                                \           //\_'/    (.\    -_  |
                 | /__________________________________\          w  \/   -  ``'       |
                 | |__________________________________|                               |
                 |    |   _______________________   |     _-            -             |
                 |_-  |  |                       |  |                        _-       |
                 |    |  |                     _ |  |  T  T  T  T  T                  |
                 | _-_|  |    __.'`'`'`''`;__ /  |  |  |  |  |  |  |        _-     -  |
                 |    |  | _/U  `'.'.,.,".'  U   |  |  | (_) |  |  |                  |
                 |    |  |   |               |   |  | / \    @ [_]d b    _@_     |    |
                 |    |  |   |      `', `,   |   |  | |_|   ____         [ ]     |    |
                 |_-  |  |   |   `') ( )'    |   |  | ______\__/_________[_]__   |    |
                 |    |  |   |____(,`)(,(____|   |  |/________________________\  |    |
                 |    |  |  /|   `@@(@@)@)'  |\  |  | ||            _____   ||   |    |
                 |    |  | //!\  @@)@@)@@@( /!\\ |  | ||   _--      \   /   ||  /|\   |
                 |__lc|__|/_____________________\|__|_||____________/###\___||_|||||__|
                / -_  _ -      _ -   _-_    -  _ - _ -|| -_    _  - \___/_- || |||||-_ \
                 """)
    press_y()
    say(f"The kitchen is like something from morrowind, in fact its almost the same design as {player_name} made when they were a teenager.")
    say("On the table is a small chest.")
    say(f"Drawn by the faint golden glow emenating from the chest. {player_name} slowly opens it.")
    lucky = random.randint(1, 4)
    if lucky == 1:
        inventory["lock pick"] = inventory.get("lock pick", 0) +1
        say(f"{player_name} has found a Lock Pick.")
        say(f"{player_name} places the Lock Pick in their Inventory. I'm sure this will come in handy.")
    elif lucky == 2:
        inventory["gold coin"] = inventory["gold coin"] +100
        say("The chest contained 100 Gold Coins.")
        say(f"{player_name} places the Gold Coins in thier Inventory.")
    elif lucky == 3:
        inventory["shiny paper"] = inventory.get("shiny paper", 0) +1
        say("OOOOOHHHHHH SHINY....... wait its just Shiny Paper???")
        say(f"{player_name} places the Shiny Paper in thier Inventory.")
    elif lucky == 4:
        inventory["potions"] = inventory["potions"] +1
        say("Always neccessary, a tried and true Healing Potion.")
        say(f"{player_name} places the Healing Potion in thier Inventory.")
    press_y()
    health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)
    print(fr"""
                                         aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa,
                                         8                           8"b,    "Ya
                                         8                           8  "b,    "Ya
                        /\               8                    aaaaaaa8,   "b,    "Ya
                   UP   ||               8                    8"b,    "Ya   "8""'""'8
                                         8                    8  "b,    "Ya  8      8
                  DOWN  ||               8             aaaaaaa8,   "b,    "Ya8      8
                        \/               8   A         8"b,    "Ya   "8""'""'"      8
                                         8             8  "b,    "Ya  8             8
                                         8      aaaaaa88,   "b,    "Ya8         B   8
                                         8      8"b,    "Ya   "8""'""'"             8
                                         8      8  "b,    "Ya  8                    8
                                         8aaaaaa8,   "b,    "Ya8                    8
                                         8"b,    "Ya   "8""'""'"                    8
                                         8  "b,    "Ya  8                           8
                                         8,   "b,    "Ya8                           8
                                          "Ya   "8""'""'"                           8
                                            "Ya  8                                  8
                                              "Ya8                                  8
                                                ""'""'""'""'""'""'""'""'""'""'""'""'"
                                         Before {player_name} is two sets of stairs.
                                             One leads up, The other leads down.
           """)
    while True:
        direction = input("Up or Down:").lower()

        if direction == "up":
            say(f"{player_name} has decided on going up the stairs. Perhaps they believe in... higher... enlightenment...")
            say("Sorry not sorry. Or maybe they just can't get stairway to heaven out of their head. I have to admit, it is a catchy riff.")

            health, enemy_name, escaped = fight_enemy(
                player_name, health, max_health, player_damage, inventory,
                potion_healing, "Dainty Wizard", 100, 10
            )

            if not continued(player_name, health):
                return "death"

            if not escaped:
                inventory["gold coin"] = inventory["gold coin"] + 50
                inventory["potions"] = inventory["potions"] + 1
                say(f"{player_name} has defeated Dainty Wizard.")
                say(f"{player_name} has recieved a Healing Potion and 50 Gold Coins.")
                say("I guess you should be proud of that.... I'll leave that one up to you.")

            break

        elif direction == "down":
            say(f"{player_name} has decided to go down. It's like they say, It's all down hill from here...")
            say("Its oddly warm and damp down here..... Humid....")

            health, enemy_name, escaped = fight_enemy(
                player_name, health, max_health, player_damage, inventory,
                potion_healing, "Burly Boulder of a Brute", 125, 20
            )

            if not continued(player_name, health):
                return "death"

            if not escaped:
                inventory["gold coin"] = inventory["gold coin"] + 100
                inventory["rusty breastplate"] = inventory.get("rusty breastplate", 0) + 1
                inventory["potions"] = inventory["potions"] + 2
                say(f"{player_name} has defeated Burly Boulder of a Brute.")
                say("Now even I'm impressed by that one.")
                say(f"{player_name} has recieved a Healing Potion, 100 Gold Coins and a Rusty Breastplate.")

            break

        else:
            say("Are we still doing this? This isn't the easter egg. It's August for crying out loud...")

    if continued(player_name, health):
        health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)
    print(fr"""
              88            \       _                           _        /              88
              88             \     (_)       .                 (_)      /               88
              88              \     |                           |      /                88
              88               \   /|\        ___________      /|\    /                 88
              88                \   |        /           \      |    /                  88
              88                 \  |       /             \     |   /                   88
              88                  \        /               \       /                    88
              88                   \      /                 \     /                     88
              88                    \    /                   \   /                      88
              88                     \  /                     \ /                       88
              88                      \/                       V                        88
              88                      /\                                                88
              88                     /  \                                               88
              88____________________/____\______________________________________________88
              88   _/____/____/____/______\____\____\____\____\____\____\____\____\___  88
              88 _/____/____/____/__________\____\____\____\____\____\____\____\____\___88
              8888888888888888888888888888888888888888888888888888888888888888888888888888
             """)
    say(f"{player_name} is faced with another dimly lit hallway.")
    say(f"With no other options but to move forward. {player_name} hesitantly moves forward.")
    press_y()
    print(fr"""


                                                *CLICK*








           """)
    say(f"A stone beneath {player_name}'s foot sinks slightly.")
    say("That's probably fine...")
    press_y()
    say("Set into the wall beside him is a small iron mechanism, with a narrow keyhole.")
    say(f"{player_name} notices the opposite wall is lined with holes. They appear to have a cylindrical metal mechanism inside them.")
    press_y()
    if inventory.get("lock pick", 0) >= 1:
        print(inventory.get("lock pick", 0))
        say(f"{player_name} remembers the Lock Pick from earlier.")
        say(f"{player_name} rummages through their pockets and finds the Lock Pick.")
        print(fr"""
                                      HHHHHHHHHHHHHHHHHHHHHHHH
                                      HHHHHHHHHHHHHHHHHHHHHHHH
                                      HHHHHHHHHHHHHHHHHHHHHHHH
                                      HHHHH'H`HHHHH'H`HHHHHHHH
                                      HHHHHbodHHHHHbodHHHHHHHH
                                      HHHHHHHHHH'`HHHHHHHHHHHH
                                      HHHHHHHHHHooHHHHHHHHHHHH
                                      HHHHHHP`HHHHHH'`HHHHHHHH
                                      HHHHHHb  "''"  dHHHHHHHH
                                      HHHHHHHboooooodHHHHHHHHH
                                      HHHHHHHHHHHHHHHHHHHHHHHH
                                      HHHHHHHHHHHHHHHHHHHHHHHH

                                               HOORAY!

                                    With a soft click the lock pick.
                                     is wedged in the mechanism.
                                     {player_name} slowly steps
                                       off the sunken stone.
             """)
        say("That was too close for comfort, ignorance is bliss on the effects of this trap.")
        press_y()
    else:
        say(f"{player_name} does not appear to have anything in their Inventory to fit in the hole.")
        print(fr"""
                               "I have a feeling, this is going to hurt"
                                "What is the kids say again... oh yeah"

                                             "YOLO"
              """)

        say(f"In one swift movement. {player_name} leaps forward. In a vein effort to jump past the trap.")
        say(f"{player_name} was not prepared for what happened next.")
        press_y()
        print(fr"""
                                               (  .      )
                                      )           (              )
                                       .  '   .   '  .  '  .
                                (    , )       (.   )  (   ',    )
                                .' ) ( . )    ,  ( ,     )   ( .
                                ). , ( .   (  ) ( , ')  .' (  ,    )
                               (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
                             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

                             Suddenly {player_name} is engulfed in flames.
             """)
        press_y()

        health = health -30
        say(f"{player_name} was badly burnt by the trap.")
        if not continued(player_name, health):
            return "death"
        say(f"{player_name} health is now {health}.")
        if inventory.get("sophisticated hat", 0) >= 1:
            inventory["sophisticated hat"] = 0
            say("Sophisticated hat was burnt in the fire.")
            print(r"""
                                  "How sad, Now no one will know just
                                 how sophisticated you really are...."
                  """)
        press_y()
    if continued(player_name, health):
        print(fr"""
                                                        ,---.
                                                       /    |
                                                      /     |
                                                     /      |
                                                    /       |
                                               ___,'        |
                                             <  -'          :
                                              `-.__..--'``-,_\_
                                                 |o/ ` :,.)_`>
                                                 :/ `     ||/)
                                                 (_.).__,-` |\
                                                 /( `.``   `| :
                                                 \'`-.)  `  ; ;
                                                 | `       /-<
                                                 |     `  /   `.
                                 ,-_-..____     /|  `    :__..-'\
                                /,'-.__\\  ``-./ :`      ;       \
                                `\ `\  `\\  \ :  (   `  /  ,   `. \
                                  \` \   \\   |  | `   :  :     .\ \
                                   \ `\_  ))  :  ;     |  |      ): :
                                  (`-.-'\ ||  |\ \   ` ;  ;       | |
                                   \-_   `;;._   ( `  /  /_       | |
                                    `-.-.// ,'`-._\__/_,'         ; |
                                       \:: :     /     `     ,   /  |
                                        || |    (        ,' /   /   |
                                        ||                ,'   /    |

                                       Have you seen my brother around?
                                        He can be a bit dainty, always
                                            getting himself lost.
        """)
        print(fr"""
                              Doesn't matter I'm sure I'll find him soon.
                              Can I interest you in some of my inventory?
              """)
        press_y()
        store["stock"]["dinted broadsword"] = 1
        store["price"]["dinted broadsword"] = 100
        store["stock"]["potion"] = 3
        while True:
            shop2 = input("Yeah Nah Nah Yeah or Nah Yeah Yeah Nah: ").lower()
            if shop2 == "nah yeah yeah nah":
                break
            elif shop2 == "yeah nah nah yeah":
                say(f"I currently have: {store["stock"]["potion"]} potions for {store["price"]["potion"]} gold coins, {store["stock"]["lock pick"]} lockpicks for {store["price"]["lock pick"]} gold coins, {store["stock"]["rusty breastplate"]} rusty breastplate's for {store["price"]["rusty breastplate"]} gold coins, {store["stock"]["dinted broadsword"]} Dinted Broadsword for {store["price"]["dinted broadsword"]} gold coins and {store["stock"]["shiny paper"]} shiny paper's for {store["price"]["shiny paper"]} gold coins.")
                while True:
                    say(f"{player_name} has {inventory["gold coin"]} Gold Coins.")
                    purchase = input("Select: Potion, Lock Pick, Rusty Breastplate, Dinted Broadsword, Shiny Paper, Continue:").lower()
                    if purchase == "potion":
                       if store["stock"]["potion"] >= 1:
                           if inventory["gold coin"] >= 50:
                                store["stock"]["potion"] = store["stock"]["potion"] -1
                                inventory["potions"] = inventory["potions"] +1
                                inventory["gold coin"] = inventory["gold coin"] -50
                                say(f"{player_name} has successfully purchased healing potion.")
                 
                           else:
                                broke_bitch(player_name) 
                       else:
                           say("I'm out of stock right now, come back later.")

                    elif purchase == "lock pick":
                        if store["stock"]["lock pick"] >= 1:
                            if inventory["gold coin"] >= 25:
                                store["stock"]["lock pick"] = store["stock"]["lock pick"] -1
                                inventory["lock pick"] = 1
                                inventory["gold coin"] = inventory["gold coin"] -25
                                say(f"{player_name} has successfully purchased lock pick.")
                            else: 
                                broke_bitch(player_name) 
                        else:
                            say("I'm out of stock right now, come back later.")

                    elif purchase == "rusty breastplate":
                       if store["stock"]["rusty breastplate"] >= 1:
                           if inventory["gold coin"] >= 150:
                            store["stock"]["rusty breastplate"] = store["stock"]["rusty breastplate"] -1
                            inventory["rusty breastplate"] = 1
                            inventory["gold coin"] = inventory["gold coin"] -150
                            defending = True
                            say(f"{player_name} has successfully purchased healing Rusty Breastplate.")
                           else: 
                            broke_bitch(player_name) 
                       else:
                           say("I'm out of stock right now, come back later.")

                    elif purchase == "dinted broadsword":
                       if store["stock"]["dinted broadsword"] >= 1:
                           if inventory["gold coin"] >= 100:
                            store["stock"]["dinted broadsword"] = store["stock"]["dinted broadsword"] -1
                            inventory["dinted broadsword"] = 1
                            player_damage = 45
                            inventory["gold coin"] = inventory["gold coin"] -100
                            say(f"{player_name} has successfully purchased Dinted Broadsword.")
                           else: 
                            broke_bitch(player_name) 
                       else:
                            say("I'm out of stock right now, come back later.")

                    elif purchase == "shiny paper":
                       if store["stock"]["shiny paper"] >= 1:
                           if inventory["gold coin"] >= 50:
                            store["stock"]["shiny paper"] = store["stock"]["shiny paper"] -1
                            inventory["shiny paper"] = 1
                            inventory["gold coin"] = inventory["gold coin"] -50
                            say(f"{player_name} has successfully purchased Shiny Paper.")
                           else: 
                            broke_bitch(player_name) 
                       else:
                           say("I'm out of stock right now, come back later.")

                    elif purchase == "continue":
                         break
                    else:
                         say("Oh dear, You've had an aneurysm.... When you're feeling up to it, try a valid response.")
            else:
                         say("Oh dear, You've had an aneurysm.... When you're feeling up to it, try a valid response.")

    health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)
    say(f"{player_name} uses the back door and leaves the wizards shop.")
    say(f"Once again, {player_name} finds themselves in an unfamiliar neighbourhood.")
    say("A quiet street. It also seems somewhat abandoned. A broken streetlight buzzes loudly as it flickers.")
    say(f"{player_name} looks left and right.")
    while True:
            street = input("Left or Right: ").lower()
            if street == "left":
                say("Something is telling me I should go left.")
                say(f"{player_name} turns left and starts walking at a steady pace.")
                break
            elif street == "right":
                say("I have a hunch that right is right....")
                say(f"{player_name} turns to the right, and begins their journey once more.")
                break
            else:
                say("I do apologise but I only speak english. Please try entering left or right?")
    print(fr"""
                                                   ___
                                                   T T
                                                   ===
                                                   |.|
                                                  .'.`.
                                                .'.' `.`.
                                  %%          .'.' ___ `.`.
                                  %%%%       .'.'  |_|_|  `.`.
                                  %%%%%%    .'.'    |_|_|    `.`.
                                  %%%%%__.--`'| []  |_|_|  [] |`'---.
                  __              %%%%|------||               |||||||
                   /\     =========%%%|    _&||      ___      ||===='
                  /  \   ///////////H/| j |  ||     |_|_|     ||    |
                  ||||  ////////////H%|   |- ||     |_|_|     ||____|
                  |||| /////////////H/|   |  ||     |_|_|     ||  TT|       .   &
                  |||| @@@@@@@@@@@@@H@|======||               ||====|  "==='   (f
                  |\//|\/|/\//\||//|\|||/\//|//\||\//||//|\||\||\/|/\//\||////|//\/||

                   As {player_name} continues along the street. Things start to appear
                       more normal. And best of all, no ogres in sight!
        """)
    press_y()
    say(f"As {player_name} looks around. Everything is how you'd expect in a normal neighbourhood.")
    say("Street lights aren't all broken anymore, there's parked cars lining the streets even wheelie bins.")
    print(fr"""
                                                                          ______________
                                                                         |##############
                              __             __                          |##############
                _____________|  |_____     _(   )                        |##############
                UUUUUUUUUUUUU|__|UUUUU| ,-'      )_                      |##############
                UUU_UUUUUU_UUUUUU_UUUU|(   (  /    )                     |   __   __   _
                UU|_|UUUU|_|UUUU|_|UUU|.  \   )  _) )                    |  |  | |  | |
                UUUUUUUUUUUUUUUUUUUUUU| `.  .    )  )                    |  |__| |__| |_
                ======================|(_   |  )  _)                     |
                     __     __    __  |(__(_|____)_______________________|   __   __   _
                |   |__|   |__|  |__| |uuuuuuuuuuuuuuuuuuuuuuuuuuuu,'.uuu|  |  | |  | |
                |   |__|   |__|  |__| |uuuuuuuuuuuuuuuuuuuuuuuuuu,'   `.u|  |__| |__| |_
                ======================|uuuu_uuuuuu_uuuuuu_uuuuu,'__   __`.
                     __     __    __  |uuu| |uuuu| |uuuu| |uuuu||  | |  ||   __   __   _
                |   |__|   |__|  |__| |uuu|_|uuuu|_|uuuu|_|uuuu||__| |__||  |  | |  | |
                |   |__|   |__|  |__| |=_====__================'         |  |__| |__| |_
                ======================||  | |  |  __   __   __   __   __ |______________
                  ___  __    ________ ||__| |__| |  | |  | |  | |  | |  ||+++++++++++++_
                ||_|_||  |  |  |     || _______  |__| |__| |__| |__| |__||++.-------.+|
                ||_|_||- |  | -|     |||   |   |                         |++|   |   |+|_
                 |_|_||  |  |  |_____|||   |o  |  _     ____________  _  |++|   |-  |+++
                ---. _|--|__|--|_____|||===|   |_|_|_  /_|__|_______| _|_|++|___|___|+++
                ----`. ___             ;---'---'      |  |_-|       |__     |       \
                --(_)-'_ _\___________/________|____/_'-(_)-----(_)-' _\____|________\__
                ________________________________________________________________________
        """)
    press_y()
    say(f"Suddenly, {player_name} hears something they haven't heard since they waking up in this nightmare.")
    print(r"""
                                    ____           3                                   _
                .,               _ '    `_      _______                               ( )
              --+-[---------.---(-)-----(@)----|-------|--.-----|-------------.-------|~--
                | ]         |   |~      |~ (@) _          |     |          |} |       |
              --+-[-----|---+---|-------|--|--(@)---------+-----|----------|}-+---|---|---
                |/      |   |   |       |  |  |~  (@)  _  | |  _| ..       |  |   |   |
              --Y-------|---+---|-------|--|--|---|---(@)-+-|>( )------|---|--+---|-------
               /|_     _|   |           `=_|  |   |   |~  |    ~       |>(@)  |  _|
              |-@-)---(@)---+-----------------|---|---|---+-------------------+-(@)-------
                  \_|/     ~    |                     |   |   |                   |  ~
              --+-----------"-------------------------|---"-------------------"-----------
                            |
               ._}    --                           -MUSIC-
        """)
    say(f"As {player_name} continues, the music is steadily getting louder.")
    say("But thats not all you notice. There is more activity, you even saw someone entering a house")
    press_y()
    print(r"""
                     ______________________________________________________________
                     ______________________________________________________________
                            | |                                         | |
                            | |                                         | |
                            | |         [ ] ______________ [ ]          | |
                      ____  | |            |              |             | |    ____
                        ||  | |            |   ________   |             | |   ||
                        ||  | |            |  |        |  |             | |   ||
                        ||  | |            |  |________|  |             | |   ||
                      __||  | |            |       (   )  |             | |   ||___
                        ||  | |            |   ___(() ()) |             | |   ||
                        ||  | |            |  |    ()_()  |            | |   ||
                        ||  | |            |  |___/() ()\||     ///\    | |   ||
                      __||  | |            |     //)   (\/|   //\\//\\  | |   ||___
                            | |            |   __\\|___|  |    ///\\\   | |
                            | |            |  |  )//- -\  |   ////\\\\  | |
                            | |            |  |____|_|_|  |   ////\\\\  | |
                      ______| |____________|_______| | |__|___/////\\\__| |________
                            | |            /       |_|_|  \   \\\  ///  | |
                            | |           /________/_|_\___\  ///  \\\  | |
                      ______|_|_______________________________(_)__(_)__|_|________
                                 @       /__________________\    @
                      ________@_\|/@_____|__________________|__@\|/_@______________
                      jro    \|/  \|/   /____________________\\|/  \|/
                                        |____________________|
        """)
    press_y()
    say(f"{player_name} decides to keep heading towards the music.")
    print(r"""
                           "Where there's Music, There's got to be people..."
    """)
    say("The music appears to be coming from a building at near the end of a cul de sac.")
    say(f"Now {player_name} is closer, they can see the music is coming from a bar.")
    press_y()
    print(r"""
                           .======================================.
                           | ___ ___ ___               _   _   _  |
                           | \_/ \_/ \_/ C|||C|||C||| |-| |-| |-| |
                           | _|_ _|_ _|_  ||| ||| ||| |_| |_| |_| |
                           '===================================== ,sSSSs
                                        THE RUSTY OGRE           SSSS "(
                                .:.                              SSS@ =/  \~/
                               C|||'                             SSSS_(_  _Y_
                             ___|||______________________________SS/ _)_) /.-
                            [____________________________________] \   /\//
                             |   ____    ____    ____    ____   | \|==(\_/
                             |  (____)  (____)  (____)  (____)  | (/   ;
                             |  |    |  |    |  |    |  |    |  | |____|
                             |  |    |  |    |  |    |  |    |  |  \  |\
                             |  |    |  |    |  |    |  |    |  |   ) ) )
                             |  |____|  |____|  |____|  |____|  |  (  |/
                             |  I====I  I====I  I====I  I====I  |  /\ |
                             |  |    |  |    |  |    |  |    |  | /.(=\
                                                                    Y\_\
        """)
    say(f"Absolutely exhausted from the rats, wizards, ogres and goblins. {player_name} doesn't even look around as they enter the bar.")
    say("It's not until they look up at the bartender to order a drink that they notice it.")
    press_y()
    print(fr"""
                                                        __,='`````'=/__
                        "What can I get ya pal?"      '//  (o) \(o) \ `'
                                                      //|     ,_)   (`\
                                                    ,-~~~\  `'==='  /-,
                                                   /        `----'     `\
                                                ,-`                  ,   \
                                                /      ,               \,-`\
                                                ,`    ,/,              ,>,   )
                                                (      `\`---'`  `-,-'`_,<   \
                                                 `.      `--. _,-'`_,-`  |    \
                                                  [`-.___   <`_,-'`------(    /
        """)
    say("The bartender is an ogre...")
    say("At least this one seems friendly.")
    say(f"{player_name} looks around the room, theres a strange mix of creatures and humans. All having a great time as if it is completely normal.")
    say(f"Two goblins appear to be arguing over a poker game in one corner, theres a conga line of ogres doing laps of the dance floor, a clearly intoxicated pixie making glitter angels on the bar because they can't get up and a collection of rats at the shorter tables in the middle of the room. One of which looks suspiciously like the Rat with Glasses {player_name} fought earlier.")
    press_y()
    say(f"Unsure if just confused or angry. {player_name} asks the bartender:")
    print(fr"""
                        "What is going on? I was playing pokemon on my gameboy,
                        falling asleep on the couch, next thing I wake up in a
                        strange room, getting attacked by an ogre."
        """)
    say("The smile suddenly drops from the ogres face.")
    say("Slightly concerned by the sudden change in demenour you look the ogre straight in the eyes.")
    print(r"""
                  "Mate, I think I might have to cut you off for tonight. I don't
              know what pookermoans are but sounds like you've had a few too many brews."
        """)
    say(fr" 'I havn't even had a drink!' {player_name} exclaims.")
    say("And as suddenly as the bartenders mood had changed it flipped just as quickly again.")
    print(fr"""
                      "HA HA HA HA Well in that case I think that's your problem!

                                      Here, first one's on me."
        """)
    say("His deep laugh shook the bar you were leaning on. This is not someone you want to upset. With a pained smile you accept the drink and sit back on the bar stool.")
    say(f"With no help from the bartender. {player_name} decides to ask some of the other patrons if they know whats going on.")
    press_y()
    print(fr"""
 {player_name} approaches what he believes to be a human. They look a lot like frankenstiens monster...

                      ,...,
                      |. .|
                      q - p
                      |\'/|
                   .-''---''-.
                  / ,       , \
                 /\/\   Y   /\/\
                 \ \ | ~ ~ | / /
        """)
    print("""
                      "Can you tell me why theres mythical creatures everywhere?"
        """)
    say("The monster of a man turns and considers you for a long moment.")
    press_y()
    say("After what feels like 2 entire minutes of staring at eachother, he opens his mouth.")
    say("However, instead of words. He just makes a low gurgling growling sound. He does this twice more then smiles.")
    say("Seeming satisfied he had solved my problem, he turned back to the bar.")
    say(f"{player_name} looks around the bar for a more helpfull face. He can see a goblin sitting alone, and from what he can tell Daria.... from the 2000's cartoon.")
    while True:
        secret = input("Choose one: Goblin or Daria: ").lower()
        if secret == "goblin":
            say(f"{player_name} decides to approach the goblin. Sitting at a table far too large for him. He appeared deep in thought, staring in the distance.")
            say(f"{player_name} clears their throat nervously as they aproach. 'E..E..Excuse me sir'.")
            say("The goblin turns to look at you. Unable to decipher his expression.")
            say(fr"""{player_name}: "What's happening around here?" """)
            print(r"""
                                                ,      ,
                                               /(.-''-.)\
                                           |\  \/      \/  /|
                                           | \ / =.  .= \ / |
                                           \( \   o\/o   / )/
                                            \_, '-/  \-' ,_/
                                              /   \__/   \
                                              \  s__/\__  /
                                            ___\ \|--|/ /___
                                          /`    \      /    `\
                                         /       '----'       \
                             "Wot's appenin'? Wot koinda qwastion is zat?
                            Things is appenin'. Things is orlways appenin'"
            """)
            press_y()
            break
        elif secret == "daria":
            say(f"{player_name} loved that show as a kid, it's incredible she looks just like her.")
            say(f"{player_name} approaches the woman")
            print(r"""
                             .-------,
                          ../         \
                         /  ,   ,   ,  \
                       /  , \__\___\   \      Sometime's your shallowness
                      |   | __ || __',. \     is so thorough,
                      |   \_'_/ \_'_/.   |    it's almost like depth.
                      |  (|    v    |)   |    ---   -----
                     ,    |       |    .       /
                      |    \  ~  /     |   ---'
                       |   /. | | .\    .
                      / ,/ |/   \| \,  |,
                     ( <-,  \___/  ,->   )
                      |  ,_ \   / _,  .|
                      | \  \ \ / /   / |
                      | |   \ * /    | |
                      | |     #      | |

                                           "Oh sorry thought you were someone else"
            """)
            print(fr"""
                                "Can you tell me what's going on here?
                               And your name doesn't happen to be Daria?"
            """)
            press_y()
            if inventory.get("shiny paper", 0) >= 1:
                say("Wait, what's that in your pocket.")
                say(f"Before {player_name} can even react. Daria suddenly reaches into {player_name}'s pocket.")
                say("Where did you get this paper?")
                say(f"Unsure of what is happening {player_name} just stares blankly.")
                say(f"{player_name} watches in horror as Daria unfolds the paper. With one large deliberate lick, the turtle was removed.")
                print("""
                                "Hmmm, ketchup... Your one of us? Well
                                why didn't you say so? Well it doesn't
                                matter. All that matters is I know that
                                you like turtles. I like turtles.
                                Follow me."
                """)
                say(f"And with that Daria swiftly turned and started walking towards a red door near the back of the bar. With no better option {player_name} jogs over to catch up.")
                say(f"{player_name} follows Daria into the dark mysterious room.")
                press_y()
                print(fr"""
                       _________________________________________________________
                      ||-------------------------------------------------------||
                      ||.--.    .-._                        .----.             ||
                      |||==|____| |H|___            .---.___|"''"|_____.--.___ ||
                      |||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|---|||
                      |||==|    | | |   | \         |   |   |_\/_|Black|  | ^ |||
                      |||  |    | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|  | ^ |||
                      |||  |    | | |   |_\ \_( oo )|   |   |    |Magus|  | ^ |||
                      |||==|====| |H|xxx|  \ \ |''| |+++|=-=|"''"|-=+=-|==|---|||
                      ||`--^----'-^-^---'   `-' ""  '---^---^----^-----^--^---^||
                      ||-------------------------------------------------------||
                      ||-------------------------------------------------------||
                      ||               ___                   .-.__.-----. .---.||
                      ||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|||
                      ||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| Q |||
                      ||      _a'  / (|===|+|   |++|  |==|   | |  |Illum| | R |||
                      ||      '/\\/ _(|===|-|   |  |''|  |:x:|=|  |inati| | Y |||
                      ||_____  -\ ___(|   |-|   |  |  |  |   | |  |     | | Z |||
                      ||       _(____)|===|+|[I]|DK|''|==|:x:|=|XX|<(*)>|=|^^^|||
                      ||              `---^-^---^--^--'--^---^-^--^-----^-^---^||
                      ||-------------------------------------------------------||
                      ||_______________________________________________________||

                         Daria walks over to a bookshelf. The only thing in the
                        small room. A floor lamp stands in the corner casting a
                                  yellowish glow over the two figures.
                """)
                press_y()
                say("Without a word, she turns and hands you a book.")
                say("It's a fairly heavy book for its size. As you open it you realise why.")
                say("It is not a book at all. It's a tablet disguised as a book.")
                say(f"Unsure what to do, {player_name} looks up at Daria. She makes a tapping motion with her hand.")
                say(f"{player_name} repeats the motion activating the tablet...")
                press_y()
                print(fr"""
                                            _.- -.
                                      _/"'"',. ` ,ooooo.___
                                    .'`'\    `. \"''''`"'"PP8ooo._
                                   (  .-)`.    `.\            '`"P8oo_
                                ,o8P\ `-.  `.     `.               ``Y8o.
                             ,dPP'   `.  `. '-.  ,.`-._                `Y8o_
                           d8P'        \. `.  (`-. `-._/     -.\/.-       `Yb.
                         d8P            `( ') `',`-._.`                     `Y8.
                       ,8P      /'.      )  (   ).-'   \            .'\      `Yb_
                      dP'       )  '.    `-._)_/    \             .'  (        `8L
                    ,8P         \    '.    \  `.  \    `.       .'    /          Yb
                   ,8P           '.*   '.       .-=^=-.       .'   *.'            Yb
                  ,8P   -.\/.-    )  `.  \     ;:)(\)(/`     /  .'  (              Yb
                  8P            .'     :  '.  (`(/ (/ /(.  .'  :     `.     -.\/.-  8b
                 d8'          .'  *     \   \//,)<*)(*>(.\/   /    *   `.           `8.
                ,8P          '.             (/():  ^  :(\(              .'           Yb
                d8             '-._   "-    )( :)._=_.(: ))   -"    _.-'             `8.
                8P               \         ( ))(()   ( )(( )         /                8b
                8b               '.  *   .'  .           .  `.   *  .'                8b
                8b    -.\/.-       ''--.'  .''  .  :  .  ''.  '.--''                  8b
                Yb                    `  -`_* `._.` `._.` *_`-  `                    ,8P
                Y8.                   \  '. '- '       ' -' .'  /                    d8'
                 8b                            '   ^ .-'                             8P
                 Y8.                    ^ -._  |`-.''.-`\  _.- ^      ~       -._   d8'
                  Yb    ~   ^ _ .-  '         /     . `-.\     ~    ,   ^- _  _    ,8P
                   8b        ~           ~   '.,-._  `. .':  ` -._          ~      8P
                    Yb              ,   .-   |     '`--.__]        ~         .   ,8F
                     Yb         ~            |     '     /                ~     ,8P
                      Y8L           . - ~    '     |    '    ~      .  `-._     o8'
                        Yb.     .              ,     ~             ~          d8P
                         `Yb.        ~                    ~   ` -._         d8P
                           `Y8L           ~       ~           ,  .       _o8P
                              YYb._        _.-'                       _o8P'
                                `"Ybo._           ,     ~         _,o8P'
                                    `"P8oo._                __ooo8P"'
                                        `'"YPP8oooooooooooLGB"''
                                              `''''''''''
                """)
                press_y()
                say(f"Without a word {player_name} turns and leaves the room.")
                break
            elif inventory.get("shiny paper", 0) <= 0:
                say("There is nothing in life that can't be improved with pizza.")
                say(f"{player_name} just stares blankly at Daria.")
                say("With no further explanation, she turns and simply walks away.")
                break
            else:
                say("Normally I'd talk slower but thats hard in text.... GOBLIN OR DARIA.... its really rather easy choice.")
    say(f"{player_name} somehow more confused now then before they entered the bar. Decides it would be best to just head home, wherever that is from here...")
    say(f"With a new found determination. {player_name} hastily heads for the exit.")
    say(f"Unfortunately just as {player_name} is nearing the door, they tripped over the tail of the weird rat wearing glasses.")
    say(f"Unable to regain their balance. {player_name} as if straight from a cartoon, arms swinging in a desperate swimming motion, falls face first into a rather obtuse looking Orc. Knocking all the drinks off his table in the process.")
    press_y()
    print(r"""
                                       _,.---''```````'-.
                                   ,-'`                  `-._
                                 ,-`                   __,-``,\
                                /             _       /,'  ,|/ \
                              ,'         ,''-<_`'.    |  ,' |   \
                             /          / _    `  `.  | / \ |\  |
                             |         (  |`'-,---, `'  \_|/ |  |
                             |         |`  \  \|  /  __,    _ \ |
                             |         |    `._\,'  '    ,-`_\ \|
                             |         |        ,----      /|   )
                             \         \       / --.      {/   /|
                              \         | |       `.\         / |
                               \        / `-.                 | /
                                `.     |     `-        _,--V`)\/        _,-
                                  `,   |           /``V_,.--`  \.  _,-'`
                                   /`--'`._        `-'`         )`'
                                     /        `-.            _,.-'`
                                                 `-.____,.-'`

                                  "RRRHHHAAAAAAGH-KKHHHRAAAAAA!!"
    """)
    say(f"The Orc turns and roars directly in {player_name}'s face.")
    press_y()
    print(fr"""
                              "Uh...I...I...I'm so sorry, please let me
                              buy you another drink! Here take mine even"
    """)
    say(f"In a gutteral growl, the Orc bellows:")
    print(r"""
                               "I'LL DRINK YOUR BLOOD!!! HOW DARE YOU
                            CHALLENGE ZORK! THE GREATEST ORC OF ALL ORCS!!!"
    """)
    say("And with that, He reached for the hefty sword strapped to his waist. The rusty handle making a metalic clink as the Orc's gauntlet unsheathes it.")
    say(fr""" "Well that's not good" {player_name} thinks to themselves. """)
    health, enemy_name, escaped = fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, "Zork: Orc Champion", 120, 25)
    if not continued(player_name, health):
        return "death"
    if continued(player_name, health):
        if escaped == False:
                 inventory["gold coin"] = inventory["gold coin"] +75
                 inventory["potions"] = inventory["potions"] +1
                 say(f"{player_name} has defeated Zork: Orc Champion.")
                 say(f"{player_name} has recieved a Healing Potion and 75 Gold Coins.")
    health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)
    say("The entire bar fell into a thick silence.")
    say(f"{player_name} looks around, all the patrons avert their gaze. From rat to pixie, Goblin to Orc, even the gargoyles turned to stone and stood silent.")
    print(r"""
                              "That Orc must have been someone important.
                           I better split before anyone else wants a turn..."
    """)
    say(f"As {player_name} makes their way towards the door, everyone shuffles back to clear a path.")
    say(f"Free from the confusing bar. {player_name} takes a moment to compose themselves.")
    say(f"{player_name} looks around. They are in the back alley behind the bar. The music loud an pumping again, as if {player_name} was never here.")
    say(f"Finally {player_name} spots a familiar site. The metro sign for the train home.")
    say(f"Utterly bewildered. {player_name} looks around once again. Even though they don't recognise any buildings around them, directly in front of {player_name} is the metro sing.")
    print(fr"""
                 888888888888888888888888888888888888888888888888888888888888888888888
                 8P'                                                               `Y8
                 8      888       __  __  _____  _____  ____    ___                  8
                 8    ww888ww    |  \/  || ____||_   _||  _ \  / _ \                 8
                 8     Y888P     | |\/| ||  _|    | |  | |_) || | | |                8
                 8      'Y'      | |  | || |___   | |  |  _ < | |_| |                8
                 8               |_|  |_||_____|  |_|  |_| \_\ \___/                 8
                 8b.                                                               .d8
                 888888888888888888888888888888888888888888888888888888888888888888888
    """)
    while True:
        no_choice = input("Select One: Metro or Bar: ").lower()
        if no_choice == "bar":
            say("Really.... You want to try your chances in that bar again?")
            say("I don't think their going to get you another drink after that last scene you caused...")
            say("I highly recomend trying the Metro. Could be fun....")
        elif no_choice == "metro":
            say("This seems like the best choice. The worlds gone mad. Might as well go home.")
            say(f"{player_name} hurriedly makes their way across the dark alley.")
            break
        else:
            say("We have been through a lot, and still you havn't learnt to type? Can I suggest the game: TypingMaster Bubbles, it has pretty colours....")
    say(f"The moment {player_name} foot steps into the light past the alley. They suddenly feel a heavy thump across their stomach.")
    print(r"""
                                 \     \      |      /     /
                              ----\     \     |     /     /----
                                   \     \    |    /     /
                                    \     \   |   /     /
                             =========\    \  |  /    /=========
                                        _____________
                              _______ _    _  _    _   __  __   ____    _
                             |__   __| |  | || |  | | |  \/  | |  __ \ | |
                             | |  | |  | || |  | | | \  / | | |__) || |
                             | |  | |__| || |  | | | |\/| | |  ___/ | |
                             | |  |  __  || |__| | | |  | | | |     |_|
                             |_|  |_|  |_| \____/  |_|  |_| |_|     (_)
                             =========/    /  |  \    \=========
                                    /     /   |   \     \
                                   /     /    |    \     \
                              ----/     /     |     \     \----
    """)
    press_y()
    say(f"{player_name} is launched backwards. Into the brick wall of the alleway.")
    say('"BOOYAH!"')
    say(f"{player_name} looks up...")
    print(fr"""
                                                                             .---.--.       .--.
                                                                           ,(     ),.`.   .'.--.`.
                                                                           ; \   / : \ ;.'.'    \ ;
                  888                            \                         ; _; :_ :""-/ /-.     ;:
                  888                             \                        ;'-;":-':"-/ /-._^.   ;:
                  888                              \ \                       :  : ;  ; / /  / \ \  ;:
  .d8888b888  88888888b.  .d88b. 888d888 .d88b.     \\ \                      :\  V  / : :  :   ; ;-';
  d88P"   888  888888 "88bd88""88b888P"  d88P"88b    \\ \                     ; ;._.':,' ;  ;   : :-'
  888     888  888888  888888  888888    888  888   \ \\ \                   : : ; : ;o /-._;   : :
  Y88b.   Y88b 888888 d88PY88..88P888    Y88b 888    \ \\ \                 _;o; : ; '-'.'.-"`. :-^,
  "Y8888P "Y8888888888P"  "Y88P" 888     "Y88888      \ \\ \            .-.;:_"  _..--"/ /  _  ;y  ;
              888                            888       \ \\ \         .' / '-,; ::    : :  (o) ;   :
         Y8b d88P                       Y8b d88P        \ \\ "-.     /  :    ;: ;;    ; ;     /    :
          "Y88P"                         "Y88P"          : \\   \   :   ;    :: ;;  .' ;._..+:     ;
                                                         :  \\   \  :  _:    ;: :: /   ; ;  ; ;(o):
                                                    "-.   \  \\   \/ Y' '.  // ^ \Y   / /  :  '._.;
                                                    \  \   \  ;"-. ;/     7"" / \ :.-'.' .';  /  /
                                                    \\  \   \ :   ":_    :"\ ;..-^'--" .' /  /  /
                                                     \\  \   "+.;-"" )._..^-""        /  / .' .'
                                                     ;"+.;_.-" :--=<___)    __..__  /  :-" .'
                                                   \ :/_. ;  .-" \ _____.--""__..--""   ;.-"
                                                    ":  '+'  __..-\/\  "''"T__..___..-":
                                                     :   :\."      \/;     ;: () ;  .-" ;
                                                      "--q/\        "      :;    :-"    :
                                                          \/;              ;:    ;   ..-(
                                                           "               :-\__/-+""-. .^.
                                                                            ; \  (     \;  `.
                                                                           /`. `-/\ ,=. '.   `.
                                                                          : \ \ :"-:/ .`. \    \
                                                                          ;  ; ;;"-;\/ .'`."-.  ;
                                                                         :   : ;"-.: \/ .' j  "-:
                                                                         ;   : :"-.;  `: ,' ;    \
                                                                        :    : :"-:     "..':     ;
                                                                        ;    ; ;"-;       `=;  ;  :
    """)
    say(f'"You have GOT to be kidding me." {player_name} exclaims.')
    health, enemy_name, escaped = fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, "Cyborg", 135, 20)
    if not continued(player_name, health):
        return "death"
    if escaped == False:
        if continued(player_name, health):
            say(f"Thinking the fight is over, {player_name} leans closer to see what was inside of the machine that attacked them.")
            say("Suddenly something moves from inside the broken robotic shell.")
            say(f"{player_name} jumps backwards, startled by the sudden movement.")
            say("Something wet and slimy emerges from the wreckage.")
            print(fr"""
                                                /;;.
                                      ,o--.._(((,:;_,,,,
                                      (__         `` ```````''-.__
                                       `')_\'''''''------''-.__,'
            """)
            press_y()
            say(f'"Is that a mudskipper?" {player_name} thinks to themselves.')
            health, enemy_name, escaped = fight_enemy(player_name, health, max_health, player_damage, inventory, potion_healing, "Carl", 80, 35)
            if not continued(player_name, health):
                return "death"
            if continued(player_name, health):
                if escaped == False:
                         inventory["gold coin"] = inventory["gold coin"] +150
                         inventory["potions"] = inventory["potions"] +1
                         say(f"{player_name} has defeated Carl.")
                         say(f"{player_name} has recieved a Healing Potion and 150 Gold Coins.")
    health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)
    say(f"Battered and bruised, {player_name} stumbles down the stairs.")
    say(f"Determined to make it home, they make their way onto the platform.")
    say("The subway station is almost empty. Save for a couple of ogres at the far end. They were all wearing precariously tight suits, giving them an oddly comical appearance.")
    print(r"""
                                                                         \  /
                                   __                                     \/
                      _   ----==##==----_________________________--------------  _
                     [ ~~~=================###=###=###=###=###=================~~ ]
                     /  ||  | |~\  ;;;;     PKP    ;;;  ET22-689  ;;;;  /~| |  ||  \
                    /___||__| |  \ ;;;;            [_]            ;;;; /  | |__||___\
                    [\        |__| ;;;;  ;;;; ;;;; ;;; ;;;; ;;;;  ;;;; |__|        /]
                   (=|    ____[-]_______________________________________[-]____    |=)
                   /  /___/|#(__)=o########o=(__)#||___|#(__)=o#########o=(__)#|\___\
                  _________-=\__/=--=\__/=--=\__/=-_____-=\__/=--=\__/=--=\__/=-______

    """)
    press_y()
    say("With a loud hiss from the air brakes, the train pulls into the platform.")
    say(f"{player_name} steps onto the train. It's just a standard train completely normal all the way down to the gum stuck under the seats.")
    say(f"As {player_name} sits down, the familiar announcer voice sounds over the radio 'Next stop, Carlton'.")
    say(f'"Thats only two stops from my house" {player_name} mutters to themselves.')
    say(f"On the seat beside {player_name} there's a backpack.")
    say(f"{player_name} looks up and down the aisle. But there is still no one in sight.")
    say(f'"Cant hurt to have a peak." {player_name} thought to themself.')
    say(f"{player_name} opens the ordinary backpack.")
    say(f"{player_name} has recieved: 2 Healing Potions, 100 Gold Coins, 1 Rusty Breastplate and a Mysterious Green Leaf.")
    inventory["potions"] = inventory["potions"] +2
    inventory["gold coin"] = inventory["gold coin"] +100
    inventory["rusty breastplate"] = 1
    inventory["mysterious green leaf"] = 1
    say('"Right."')
    say(f"{player_name} places the now empty bag back onto the seat beside them.")
    say(f"{player_name} rests their head against the cold window, as the thoughts start racing.")
    say("How did that bag do that?")
    say("If there's an ogre at my house.......")
    say(f'"No point worrying bout what ifs or elifs..." {player_name} thinks to themselves.')
    say(f"And that's how the train went. Suddenly normalcy, {player_name} alone with their thoughts. It felt just like a regular work commute, minus the fact there were no other people, or mythical creatures for that matter.")
    press_y()
    say(f"When {player_name} arrived at their stop. They looked out the door cautiously before leaving the safety of the train.")
    say("The platform was completely empty.")
    say(f"{player_name} leaves the empty metro behind. As they walk the short trek home, they notice everything seems normal again.")
    say(f"There's people going about their business. Cars driving on the street. Bird's flying in the sky. Not a single sign of the madness {player_name} just experianced.")
    say(f"{player_name} makes it all the way back to their house without any other incidents.")
    health, inventory = menu(player_name, health, inventory, player_damage, potion_healing, max_health, description)
    say(f'{player_name} thinks to themselves "The lack of weird is even weirder now then the weird was.... that hurt my brain..."')
    say(f"When {player_name} enters their house, they discover they are not infact alone.")
    print(r"""
                                    ______         ______________
                                          |       |      ||      |
                                          |       |      ||      |
                                          |       |______||______|
                                          |       |      ||      |
                                        o |       |      ||      |
                                          |       |______||______|
                                          |      /______________/
                                          |            __((())__
                                    ______|____ ______|_))O O((_|__
                                            ////      | ((\O/)) |
                                            ( 00      | /\~V~/\ |
                                            \-/       |//(_ _)\\|
                                            /\\      /// \   / \\\
                                            |//     /_\)_/   \_(/_\
                                           //\\     | |_/_____\_| |
                                           \\ \\    | |  \ \\ \ | |
                                           (_)(_)   | |  / // / | |
    """)
    press_y()
    say("Mom?")
    say(f"Sitting on a chair in the middle of the living room is {player_name}'s mother.")
    say(f'"WHERE HAVE YOU BEEN?" She screams at {player_name} "THIS IS ALL YOUR FAULT!"')
    say('"I WARNED YOUA ABOUT THAT SHIT!" still screaming like a banshee "I AM GOING TO SLAP YOU TO NEXT WEEK!"')
    say(f"{player_name} stares at their mother in horror. Who is this person, this is not my mother.")
    say(f"Just as {player_name} thinks this might be an imposter, she suddenly transforms")
    print(r"""
                                                                       ,--,  ,.-.
                                    ,                   \,       '-,-`,'-.' | ._
                                   /|           \    ,   |\         }  )/  / `-,',
                                   [ '          |\  /|   | |        /  \|  |/`  ,`
                                   | |       ,.`  `,` `, | |  _,...(   (      _',
                                   \  \  __ ,-` `  ,  , `/ |,'      Y     (   \_L\
                                    \  \_\,``,   ` , ,  /  |         )         _,/
                                     \  '  `  ,_ _`_,-,<._.<        /         /
                                      ', `>.,`  `  `   ,., |_      |         /
                                        \/`  `,   `   ,`  | /__,.-`    _,   `\
                                    -,-..\  _  \  `  /  ,  / `._) _,-\`       \
                                     \_,,.) /\    ` /  / ) (-,, ``    ,        |
                                    ,` )  | \_\       '-`  |  `(               \
                                   /  /```(   , --, ,' \   |`<`    ,            |
                                  /  /_,--`\   <\  V /> ,` )<_/)  | \      _____)
                            ,-, ,`   `   (_,\ \    |   /) / __/  /   `----`
                           (-, \           ) \ ('_.-._)/ /,`    /
                           | /  `          `/ \\ V   V, /`     /
                        ,--\(        ,     <_/`\\     ||      /
                       (   ,``-     \/|         \-A.A-`|     /
                      ,>,_ )_,..(    )\          -,,_-`  _--`
                     (_ \|`   _,/_  /  \_            ,--`
                      \( `   <.,../`     `-.._   _,-`
                       `                      ```
    """)
    while True:
        health, enemy_name, escaped = fight_enemy(
            player_name, health, max_health, player_damage, inventory,
            potion_healing, f"{player_name}'s Mom", 160, 40
        )

        if not continued(player_name, health):
            return "death"

        if escaped:
            say(f"HAHAHAHHA. You thought it was that easy? Now you get to face a full strength DragonMomster again....")
            continue

        break

    say(f"{player_name} has defeated {player_name}'s Mom.")
    say("...")
    say(f"Well that was unexpected. {player_name} looks around the now empty living room. Apart from the still twitching momster, everything was how it should be. {player_name} looks at the clock on their desk.")
    print(r"""
                              +------------------------------------------+
                              |                                          |
                              |      8888888       888888   888888       |
                              |           88      88    88 88    88      |
                              |          88   88  88    88 88    88      |
                              |         88        88    88 88    88      |
                              |        88     88  88    88 88    88      |
                              |       88          88    88 88    88      |
                              |      88            888888   888888       |
                              |                                          |
                              +------------------------------------------+
    """)
    say(f'"Its getting late." {player_name} thinks to themselves.')
    say(f"Completely and utterly exhausted from the nonsense day {player_name} just experienced. They turn on thier PC, looking for a bit of an escape. Youtube, games, movies surely something is better then sitting here thinking about the madness.")
    say(f"With a heavy slump, {player_name} sits into their chair. The old faithful gaming chair, yeah we use it for work and emails. But this was one of the big luxuries {player_name} allowed themselves. There was finally a sign of relief today. The familiar chair hugged {player_name} easing the aches enough to relax just slightly.")
    say(f"{player_name} looks to the left side of their desk. The gameboy they were playing last they remember. Funny I remember laying in bed with it.")
    say(f"{player_name} looks the right side of their desk. Their sits Bongzilla. {player_name}'s prized glass piece, sniped on ebay when that was still a thing, it would always start a conversation.")
    press_y()
    say(f"That looks tempting. {player_name} turns to the monitor in front of them. The log in screen sits there waiting for an input.")
    say(f"{player_name} just sits and stares for a moment after they log in. The events of the day slowly setting in.")
    print(r"""
                                  *        \      |      /        *
                                    \       \     |     /       /
                               ======\=======\====|====/=======/======
                                      888888  888888  888b   888   888888
                                      88   88   88    8888b  888  88
                                      88   88   88    88 88b 888  88  888
                                      88   88   88    88  88b888  88   88
                                      888888  888888  88   88888   888888
                               ======/=======/====|====\=======\======
                                    /       /     |     \       \
                                  *        /      |      \        *
    """)
    press_y()
    say(f"{player_name} looks at the screen....")
    say("You have 47 unread email notifications.")
    say(f'"Fuck this." {player_name} exclaims out loud.')
    say("Suddenly remembering the Mysterious Green Leaf from earlier they pull it out of their pocket to inspect it.")
    say(f"As they inspect the scrunched up leaf they know exactly what it is.")
    press_y()
    print(r"""
                     o                         .                         ()
                                              .                     o
                         .          .-.                          .--------.
                                   (   )            o           (          )
                            ()      `-'                          `--------'       .

                                               O
                                   o                        .                 o
                          .                 .----.
                                           (      )                    ()
                               o            `----'          .

                                                           .-.
                         ()              .                (   )             o
                                                           `-'
                                  .                 O

                             .--------.                               .
                            (          )             o                        ()
                             `--------'                       .
                                                o

                        o            ()                  .              .----.
                                                                     (      )
                                  .                    o                `----'

                                              .-.
                             O               (   )                            .
                                              `-'              o

                                   o                            ()
                         .                       .------.
                                                (        )              .
                                  ()             `------'

                                                             O
                            .             o                            .
                                                   .-.
                                                  (   )
                             ()                    `-'                       o
    """)
    press_y()
    say(f"In one giant pull, {player_name} inhales the entire Mysterious Green Leaf.")
    say(f"{player_name} coughed hard enough to recover jewellery they'd long since considered lost.....")
    say(f'"Damn thats some good shit" was the last thought {player_name} had as their eyes start to close.')
    print()
    print()
    print(r"""
                                               z
                                              z
                                               Z
                                     .--.  Z Z
                                    / _(c\   .-.     __
                                   | / /  '-;   \'-'`  `\______
                                   \_\/'/ __/ )  /  )   |      \--,
                                   | \`""`__-/ .'--/   /--------\  \
                                    \\`  ///-\/   /   /---;-.    '-'
                                                 (________\  \
                                                           '-'
    """)
    print("\n" * 35)
    return "ending"


## Game Controller

while True:
    result = game()

    if result == "death":
        while True:
            retry = input("Try Again? Yes or No: ").lower()

            if retry == "yes":
                break
            elif retry == "no":
                break
            else:
                say("Yes or No please. We have been over this in depth....")
        if retry == "yes":
                continue
        elif retry == "no":
                break
    elif result == "ending":
        continue

       
                                             
                                             
                                             
   

 
 
  
              
         
                  
       
       
       
       