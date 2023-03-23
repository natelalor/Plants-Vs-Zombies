import time

from scipy.optimize import fsolve

from game import Game
import constants as c
import sympy as sp
import math
from scipy.integrate import quad
import numpy as np
import random as r


def testLevelCreation():
    for level in c.levelsDict:
        print("\nLevel", level)
        numEnemies = {1: 0,
                      2: 0,
                      3: 0,
                      4: 0}
        game = Game(level)
        for i in game.enemies:
            numEnemies[i] += 1
        for i in numEnemies.keys():
            if numEnemies[i] > 0:
                print(c.enemiesDict[i], "-", numEnemies[i])


"""
    Create a multimodal Gaussian Curve
    :param var x: variable for integration
    :param dict waves: a dictionary of dictionaries storing the variables for each of the waves
"""
def norm(x, waves):
    equation = 0.0
    for i in waves.keys():  # for each wave
        coefficient = 1 / (waves[i]['intensity'] * math.sqrt(2 * math.pi))  # #math
        exponent = -waves[i]['weight'] * ((x - waves[i]['x']) / waves[i]['intensity']) ** 2  # #moremath
        equation += coefficient * sp.E ** exponent  # combine the wave
    return equation


"""
    Organize a list semi-randomly
    :param List attacker: the list to be randomized 
"""
def randomize(attackers: []):
    r.shuffle(attackers)
    first_min = attackers.index(min(attackers))  # find the index of the first instance of minimum
    attackers.insert(0, attackers.pop(first_min))  # move it to the front
    first_max = attackers.index(max(attackers))  # find the index of the first instance of the max
    attackers.append(attackers.pop(first_max))  # move it to the end
    return attackers


def setup_waves(level):
    print("----------------- EXAMPLE -----------------")
    total_weight = 0
    attackers = []
    print("RUNNING LEVEL", level)
    print()

    for i in c.levelsDict[level]:  # loop through each tyoe of attacker in dictionary
        total_weight += i[0] * i[1]  # multiply type by weight
        for attacker in range(i[1]):  # add all the attackers to a list
            attackers.append(i[0])
    print("ATTACKERS' TYPES:", attackers)
    attackers = randomize(attackers)  # randomize the list

    print("SHUFFLED:", attackers)

    area = quad(norm, -np.inf, np.inf, args=c.waves)[0]  # integrate to find area under curve
    print("AREA OF WAVES:", area)
    scaled_attackers = []
    for attacker in attackers:  # scale the attacker's individual weight in relation to the area
        scaled_attackers.append(attacker / total_weight * area)

    rounded = [round(item, 3) for item in scaled_attackers]  # this is just for displaying
    print("SCALED ATTACKERS(rounded):", rounded, "\n")

    run_waves(attackers, scaled_attackers)


"""
    Determines when to spawn attackers
    How it works:
    - while there are still attackers to release
    - if the area bounded by negative infinity and the current timestep is greater than the total weight of the attackers
        released so far, release a new attacker 
        
    :param List attackers: list of attackers id
    :param List scaled_attackers: list of scaled attackers weights corresponding to the attackers list
"""
def run_waves(attackers, scaled_attackers):
    print("----------------- RUNNING WAVES -----------------\n\n")
    current_total = scaled_attackers.pop(0)  # Spawn the first attacker
    print("SPAWNING:", attackers.pop(0))
    timestep = 0
    while len(attackers) != 0:  # while there are still attackers to spawn
        print("TIME -", timestep)
        area = quad(norm, -np.inf, timestep / 5, args=c.waves)[0]  # integrate and find bounded area (-inf, timestep)
        if area > current_total:
            current_total += scaled_attackers.pop(0)  # add scaled attacker weight to the current total
            current_attacker = attackers.pop(0)  # spawn attacker
            print("SPAWNING: TYPE {} ({})".format(current_attacker, c.enemiesDict[current_attacker]))
        timestep += 1


setup_waves(3)
