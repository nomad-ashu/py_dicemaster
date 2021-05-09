# -*- coding: utf-8 -*-
"""
Created on Sat May  8 17:13:47 2021

@author: Ashu
"""
from dicefaces import diceroll

import random
scores = [0,0]
player = 0

def roll(scores, player):
    a = random.randint(1,6)
    diceroll(a)
    print(f'Player:{player+1} - {a}')
    if (a == 6):
        print(f'Player{1+player} has lost the chance. Score is: {scores[player]}')
        if (player == 0):
            player = 1
            roll(scores, player)
        else:
            player =0
            roll(scores, player)
    else:
        scores[player] += a
        if (scores[player] >= 100):
            print('Final Scores :', scores)
            print(f'Player{1+player} has won the game!!!')
        else:
            roll(scores, player)
            
roll(scores, player)