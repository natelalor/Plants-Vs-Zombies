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


def norm(x, waves):
    equation = 0.0
    for i in waves.keys():
        coefficient = 1 / (waves[i]['intensity'] * math.sqrt(2 * math.pi))
        exponent = -waves[i]['weight'] * ((x - waves[i]['x']) / waves[i]['intensity']) ** 2
        equation += coefficient * sp.E ** exponent
    return equation



def setup_waves():
    print("----------------- EXAMPLE -----------------")
    total_weight = 0
    attackers = []
    level = 3
    print("RUNNING LEVEL", level)
    print()
    for i in c.levelsDict[level]:
        total_weight += i[0] * i[1]
        for attacker in range(i[1]):
            attackers.append(i[0])

    print("ATTACKERS' TYPES:", attackers)
    r.shuffle(attackers)
    print("SHUFFLED:", attackers)

    area = quad(norm, -np.inf, np.inf, args=c.waves)[0]  # integrate
    print("AREA OF WAVES:", area)
    scaled_attackers = []
    for attacker in attackers:
        scaled_attackers.append(attacker / total_weight * area)
    rounded = [round(item, 3) for item in scaled_attackers]
    print("SCALED ATTACKERS(rounded):", rounded, "\n")

    run_waves(attackers, scaled_attackers)


def run_waves(attackers, scaled_attackers):
    print("----------------- RUNNING WAVES -----------------\n\n")
    current_total = scaled_attackers.pop(0)
    print("SPAWNING:", attackers.pop(0))
    for timestep in range(120):
        print("TIME -", timestep)
        if len(attackers) != 0:
            area = quad(norm, -np.inf, timestep/5, args=c.waves)[0]  # integrate
            # print(area,current_total)
            if area > current_total:
                current_total += scaled_attackers.pop(0)
                current_attacker = attackers.pop(0)
                print("SPAWNING: TYPE {} ({})".format(current_attacker, c.enemiesDict[current_attacker]))


    # full_eqn = quad(norm, -np.inf, np.inf, args=waves)


setup_waves()