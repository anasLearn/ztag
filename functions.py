# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:58:04 2017

@author: aanas / anasLearn / Anas Aamoum
"""
import data as DT

import math
import random
# === 

    
def getNewPosition(old_x, old_y, target, angle, speed, chased, rotate="na"):
    """
    Computes and returns the new Position after a single clock-tick has
    passed, calculated using the current position, the
    specified target, angle and speed.
    Does NOT test whether the returned position fits inside the field.
    target: the point the player is trying to reach. it can be None
    angle: number representing angle in degrees, 0 <= angle < 360
    speed: positive float representing speed
    Returns: a tuple representing the coordinates of the new position.
    """
    if target is not None:
        distance = math.sqrt((target.y - old_y)**2 + (target.x - old_x)**2)
        if distance == 0:
            delta_y = 0
            delta_x = 0
        else:
            delta_y = speed * (target.y - old_y)/distance
            delta_x = speed * (target.x - old_x)/distance
        if chased:
            if rotate == "clockwise":
                delta_x, delta_y = delta_y, - delta_x
            elif rotate == "c_clockwise":
                delta_x, delta_y = -delta_y, delta_x
            else:
                delta_x = - delta_x
                delta_y = - delta_y
            

    else:
        angle = float(angle)
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
    # Add that to the existing position
    new_x = old_x + delta_x
    new_y = old_y + delta_y
    return (new_x, new_y)


        
def setTarget(min_distance, chaser, target):    
    distance = chaser.calculateDistance(target)
    if chaser.target is None:  
        min_distance = distance
        chaser.target = target
    elif distance < min_distance:
        chaser.target = target
        min_distance = distance
    return min_distance
    
def setStartingPosition(positions, num_of_zombies, abscissa):
    dist = DT.height / (num_of_zombies + 1)
    for i in range(num_of_zombies):
        x = DT.width/2 - 4 + 8 * random.random()
        y = DT.height/2 - 4 + 8 * random.random()
        positions.append((x, y))
    dist = DT.height / (DT.team_size - num_of_zombies + 1)
    for i in range(DT.team_size - num_of_zombies):
        positions.append((abs(abscissa - 0.1), (i + 1) * dist))
        