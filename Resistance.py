import os
import math
import random

'''
Welcome to ResistanceAssist.
This is a micro app designed to help players of The Resistance be sorted into factions privately.
This code could be easily converted for other games that require secret and random assignment to teams.
'''

#A quick screen clear function
def clear_console():
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')   

print "Welcome to ResistanceAssist, a companion application for the role-playing game The Resistance.\n"

#Get game type and catch input exceptions
while True:
    try:
        avalon_input = raw_input("Are you playing the Avalon variant (with Merlin and Assassin)? Press y or n and Enter.\n")
        if avalon_input == 'Y':
            print "You have chosen AVALON."
            break
        elif avalon_input == 'y':
            print "You have chosen AVALON."
            break
        elif avalon_input == 'N':
            print "You have chosen STANDARD."
            break
        elif avalon_input == 'n':
            print "You have chosen STANDARD."
            break
        else:
            print "Invalid entry. Please enter y or n."
    except ValueError:
        print "You have entered an invalid, um, value. A totally valuless value."

clear_console()

#Get the number of players
while True:

    try:
        player_num = int(raw_input("Enter the number of players: "))
        if int(player_num) in range(4, 13):
            print "The number of players is {0}".format(player_num)
            break
        elif int(player_num) > 12:
            print "Too many players. Try again."
        elif int(player_num) < 4:
            print "Too few players. Try again."
    except ValueError:
        print "Entered number was not an integer? Try again."

clear_console()

#Build a dict of player names
player_name_dict = {}

for i in range(1, player_num + 1):
    player_name_dict[i] = ''

for i in range(1, len(player_name_dict)+1):
    while True:
        try:
            player_name_dict[i] = raw_input("Enter the name of Player {0}: ".format(i))
            break
        except ValueError:
            print "Invalid name; try again."                                

#Calculate how many spies there will be (1/3 of players). 
num_of_spies = math.ceil(player_num * .3333333333)

#Generate a list of random numbers. Players with these numbers are spies
random_list_spies = random.sample(range(1, player_num + 1), int(num_of_spies))

#Assign SPY or LOYAL to each player depending on random_list_spies
player_loyalty_dict = {}
for i in range(1, player_num + 1):
    if i in random_list_spies:
        player_loyalty_dict[i] = 'SPY'
    else:
        player_loyalty_dict[i] = 'LOYALIST'

#Assign a random SPY to ASSASSIN and LOYALIST to MERLIN if players chose Avalon
if avalon_input == 'y' or avalon_input == 'Y':

    merlin_chosen = 0
    assassin_chosen = 0
    
    while merlin_chosen == 0 or assassin_chosen == 0:
        
        for i in range(1, player_num + 1):
            x = random.randrange(1, player_num + 1)
            if x in player_name_dict and player_loyalty_dict[i] == 'LOYALIST' and merlin_chosen == 0:
                player_loyalty_dict[i] = 'MERLIN'
                merlin_chosen += 1
            elif x in player_name_dict and player_loyalty_dict[i] == 'SPY' and assassin_chosen == 0:
                player_loyalty_dict[i] = 'ASSASSIN'
                assassin_chosen += 1
        
#Display everyone's roles with a blank screen in between
for i in range(1, player_num + 1):
    raw_input("Press ENTER to see Player {0}'s ROLE.".format(i))
    print" Hello, {0}. As Player {1}, you happen to be a {2} this round.\n".format(player_name_dict[i], i, player_loyalty_dict[i])

    if player_loyalty_dict[i] == 'MERLIN':
        print "As Merlin, you know all.\n"
        for j in range(1, player_num + 1):
            if player_loyalty_dict[j] == 'ASSASSIN':
                #ASSASSIN == SPY from MERLIN POV
                print "Player {0} is played by {1}, who is a SPY\n".format(j, player_name_dict[j])
            else:
                print "Player {0} is played by {1}, who is a {2}\n".format(j, player_name_dict[j], player_loyalty_dict[j])
    if player_loyalty_dict[i] == 'SPY' or player_loyalty_dict[i] == 'ASSASSIN':
        print "As a spy, you get to know who the other spies are.\n"
        for k in range(1, player_num + 1):
            if player_loyalty_dict[k] == 'SPY' or player_loyalty_dict[k] == 'ASSASSIN':
                print "Player {0}, {1}, is a SPY.".format(k, player_name_dict[k])
    if i <= player_num - 1:
        raw_input("Press ENTER to clear the screen, and hand the computer to {0}.".format(player_name_dict[i+1]))
        clear_console()
    else:
        raw_input("Press ENTER to clear the screen, and get ready to play!")
        clear_console()

#Clear the screen again and have a screen prompt. Pressing ENTER again will list all the players' alliances (if players are curious)         
print "Now everyone has seen their roles. Leave this screen up and PRESS ENTER to see everyone's roles after the game has ended."
raw_input("Press ENTER after the game has ended.")

print "THE PLAYERS:\n"
for i in range(1, player_num + 1):
    print "Player {0}, was played by {1}, who was a {2}\n".format(i, player_name_dict[i], player_loyalty_dict[i])
    
#Promt for exit.
raw_input("Press Enter to Exit.")


    


