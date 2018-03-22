"""
Implementing ython Practice Project
"""
import random

def name_to_number(name):
    """
    Take string name as input (rock/Spock/paper/lizard/scissors)
    and returns integer(0/1/2/3/4)
    """
    if name == 'rock' :
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    
def number_to_name(number):
    """
    Take integer number as input(0/1/2/3/4)
    and returns string(rock/Spock/paper/lizard/scissors)
    """
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    
def rpsls(player_choice):
    print("")
    print("Player chooses ", player_choice)
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(5)
    comp_choice = number_to_name(comp_number)
    print("Computer chooses ", comp_choice)
    
    difference = (comp_number-player_number) % 5
    
    if difference == 0:
        print("Player and Computer tie!")
    elif difference == 1 | difference == 2:
         print("Computer wins!")
    else:
        print("Player wins!")
        
rpsls('paper')