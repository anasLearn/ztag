# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 11:37:07 2017

@author: aanas / anasLearn / Anas Aamoum
"""
import random

import data as DT


class Checkpoint(object):
    """
    
    """
    def __init__(self, number):
        self.number = number
        self.x = 0
        self.y = 0
        
        print("Checkpoint %d Created" % number)
        
        
class Field(object):
    """
    A Field represents a rectangular region (width * height)
    """
    def __init__(self):
        """
        
        """
        #Checkpoints
        self.checkpoints = [] 
        self.all_checkpoints = []       
        for i in range(DT.num_of_checkpoints):            
            self.checkpoints.append(Checkpoint(i + 1))
            self.all_checkpoints.append((self.checkpoints[-1], {"state":"Activable", "counter" : 0}))
            
        print("Field Created")
        
    def getNewCheckpoints(self):
        """
        Used to set new checkpoints at the beginning of each game
        """
        self.checkpoints = []
        for checkpoint in self.all_checkpoints:
            self.checkpoints.append(checkpoint[0])
            self.checkpoints[-1].x = 1 + (DT.width - 2) * random.random()
            self.checkpoints[-1].y = 1 + (DT.height - 2) * random.random()
            
            checkpoint = (checkpoint[0], {"state":"Activable", "counter" : 0})
            
    def addPlayers(self, team1, team2):
        self.all_players = []
        for i in range(len(team1)):
            self.all_players.append(team1[i])
            self.all_players.append(team2[i])
    

    def isPositionInField(self, pos):
        """
        returns: True if pos is in the field, False otherwise.
        """        
        if pos[0] >= 0 and pos[0] < DT.width:
            if pos[1] >= 0 and pos[1] < DT.height:
                return True
        return False
        
    def getNumberOfHumans(self):
        """
        Number of humans in the field
        As long as this number is > 0, the game continues
        """
        number = 0
        for player in self.all_players:
            if player.kind == "Human":
                number += 1
        return number
        
    def updateStatusOfPlayers(self):
        for player in self.all_players:
            player.updateStatus()
            
        self.updateCheckpoints()

                        
    def movePlayers(self, i):
                    
        for player in self.all_players:
            if not (player.kind == "Zombie" and i < DT.zombie_stop * DT.resolution):
                player.selectTarget()
                player.updatePosition()
        
        
    def playersInteractions(self):
        for player1 in self.all_players:
            if player1.kind == "Doctor" and not player1.disabled:
                for player2 in self.all_players:
                    if player2.kind == "Zombie" and player2.team != player1.team and not player2.disabled and (player1.calculateDistance(player2) < DT.effect_distance):
                        if random.random() < 0.5:
                            player1.disabled = True
                            break
                        else:
                            player2.disabled = True
                        
                        
                        
        for player in self.all_players:
            if player.kind == "Human":
                player.interactions()
        


    def activateCheckpoint(self, checkpoint):
        for chck in self.all_checkpoints:
            if checkpoint == chck[0]:
                if chck[1]["state"] == "Activable":
                    chck[1]["state"] = "Active"


    def updateCheckpoints(self):
        for chck in self.all_checkpoints:
            if chck[1]["state"] == "Active":
                chck[1]["counter"] += 1
                if chck[1]["counter"] == DT.cool_period[0] * DT.resolution or DT.cool_period[0] == 0:
                    chck[1]["state"] = "Disabled"
                    chck[1]["counter"] = 0
                    self.checkpoints.remove(chck[0])
                    
            elif chck[1]["state"] == "Disabled":
                chck[1]["counter"] += 1
                if chck[1]["counter"] == DT.cool_period[1] * DT.resolution or DT.cool_period[1] == 0:
                    chck[1]["state"] = "Activable"
                    chck[1]["counter"] = 0
                    self.checkpoints.append(chck[0])
                            

                
        
        