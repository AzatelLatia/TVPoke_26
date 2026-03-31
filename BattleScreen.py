# from BaseClasses import *
from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 255))
    
        self.state={
            'AlmightyPlaceholder':'First Time?'
        }
    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = [
           StupidMOVEONEButtton(10, 10, self.trainers[0].pokemon[0].moves[0]),
            StupidMOVEONEButtton(10, 25, self.trainers[0].pokemon[0].moves[1]),
             StupidMOVEONEButtton(30, 10, self.trainers[0].pokemon[0].moves[2]),
             StupidMOVEONEButtton(30, 25, self.trainers[0].pokemon[0].moves[3]),
             Label((15,30),25,15,str(self.trainers[0].pokemon[0].hp),15,(0,0,0),False),
             Label((90,95),25,15,str(self.trainers[1].pokemon[0].hp),15,(0,0,0),False),             
             Label((15,40),25,15,str(self.trainers[0].pokemon[0].name),15,(0,0,0),False),
             Label((90,90),25,15,str(self.trainers[1].pokemon[0].name),15,(0,0,0),False),
             
        ]

        if self.state['AlmightyPlaceholder']=='here we go again' or self.state['AlmightyPlaceholder']=='First Time?':
            #First trainer
            #SOMETHING HERE IS BROKEN AND I DONT KNWO WHAt
            self.elements.append(Image((20,50),25,25, self.trainers[0].pokemon[0].img))
            #second trainer ig?
            self.elements.append(Image((75,90),25,25, self.trainers[1].pokemon[0].img))

class StupidMOVEONEButtton(Button):
    def __init__(self, x, y, move):
        self.move = move
        super().__init__((x, y), 20, 20, move.name, (0,0,0),(25, 255, 255))

    def onClick(self, screen):
        screen.trainers[1].pokemon[0].takeDamage(self.move)
        screen.trainers.reverse()
        screen.state['AlmightyPlaceholder']=' here we go again'
        # y = 0
        # #two rows of three
        # for trainer in self.trainers:
        #     x = 0
        #     y += 100/3
        #     for poke in trainer.pokemon:
        #         x += 100/4
        #         self.elements.append(Image((x, y), 20, 20,p oke.img))
        #         self.elements.append(Label((x, y + 10), 20, 10, poke.name))
                




