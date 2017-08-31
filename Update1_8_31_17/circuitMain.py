#Author Chris George

'''
pygamegame.py
layout created by Lukas Peraza
for 15-112 F15 Pygame Optional Lecture, 11/11/15
'''



import pygame
import os
import random
import math

from circuitPlayNew import BasicCircuit
from circuitResistorPlay import BasicResistorCircuit

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.display.init()
titleFont = pygame.font.SysFont("Impact", 60)
subTitleFont = pygame.font.SysFont("Impact", 30)


###############################################################################
#intializeing class

class PygameGame(object):
    def init(self): 
        self.mode = 'home'
        self.prevMode = 'home'
        self.homeFunctions = {'keyPressed':self.homeKeyPressed,
                            'keyReleased':self.homeKeyReleased,
                            'mousePressed':self.homeMousePressed,
                            'mousePosition':self.homeMousePosition,
                            'redrawAll':self.homeRedrawAll,
                            'timerFired':self.homeTimerFired
                            }
        self.pausedFunctions = {'keyPressed':self.pausedKeyPressed,
                            'keyReleased':self.pausedKeyReleased,
                            'mousePressed':self.pausedMousePressed,
                            'mousePosition':self.pausedMousePosition,
                            'redrawAll':self.pausedRedrawAll,
                            'timerFired':self.pausedTimerFired
                            }
        self.playBasicCircuitFunctions = {'keyPressed':self.playBasicCircuitKeyPressed,
                                        'keyReleased':self.playBasicCircuitKeyReleased,
                                        'mousePressed':self.playBasicCircuitMousePressed,
                                        'mousePosition':self.playBasicCircuitMousePosition,
                                        'redrawAll':self.playBasicCircuitRedrawAll,
                                        'timerFired':self.playBasicCircuitTimerFired
                                        }
        self.playBasicResistorCircuitFunctions = {'keyPressed':self.playBasicResistorCircuitKeyPressed,
                                        'keyReleased':self.playBasicResistorCircuitKeyReleased,
                                        'mousePressed':self.playBasicResistorCircuitMousePressed,
                                        'mousePosition':self.playBasicResistorCircuitMousePosition,
                                        'redrawAll':self.playBasicResistorCircuitRedrawAll,
                                        'timerFired':self.playBasicResistorCircuitTimerFired
                                        }
        self.instructionFunctions = {'keyPressed':self.instructKeyPressed,
                                    'keyReleased':self.instructKeyReleased,
                                    'mousePressed':self.instructMousePressed,
                                    'mousePosition':self.instructMousePosition,
                                    'redrawAll':self.instructRedrawAll,
                                    'timerFired':self.instructTimerFired
                                    }
        self.gameOverFunctions = {'keyPressed':self.gameOverKeyPressed,
                                    'keyReleased':self.gameOverKeyReleased,
                                    'mousePressed':self.gameOverMousePressed,
                                    'mousePosition':self.gameOverMousePosition,
                                    'redrawAll':self.gameOverRedrawAll,
                                    'timerFired':self.gameOverTimerFired
                                    }

        self.circuitPlayBasicCircuit = BasicCircuit(self)
        self.circuitPlayBasicResistorCircuit = BasicResistorCircuit(self)

        
##############################################################################
## home

    def homeMousePressed(self, x, y):
        self.mode = 'play'

    def homeMousePosition(self, x, y):
        pass

    def homeKeyPressed(self, keyCode):
        if keyCode == pygame.K_b:
            self.mode = 'playBasicCircuit'
        if keyCode == pygame.K_r:
            self.mode = 'playBasicResistorCircuit'

    def homeKeyReleased(self, keyCode):
        pass

    def homeTimerFired(self, dt):
        pass

    def homeRedrawAll(self, screen):
        pygame.draw.rect(screen, (50,75,255), [0,0, self.width, self.height])
        title = titleFont.render('Circuitos', False, (255,255,255))
        centered = title.get_rect(center=(self.width//2, self.height//2))
        screen.blit(title, centered) 
        
        subTitle = subTitleFont.render('Click or Press to Play!', False, (255,255,255))
        centered = subTitle.get_rect(center=(self.width//2, self.height//2+60))
        screen.blit(subTitle, centered) 


###############################################################################      
#play basic circuit

    def playBasicCircuitMousePressed(self, mouseX, mouseY):
        self.circuitPlayBasicCircuit.playMousePressed(mouseX, mouseY)

    def playBasicCircuitMousePosition(self, mouseX, mouseY):
        self.circuitPlayBasicCircuit.playMousePosition(mouseX, mouseY)

    def playBasicCircuitKeyPressed(self, keyCode):
        self.circuitPlayBasicCircuit.playKeyPressed(keyCode)

    def playBasicCircuitKeyReleased(self, keyCode):
        self.circuitPlayBasicCircuit.playKeyReleased(keyCode)

    def playBasicCircuitTimerFired(self, dt):
        self.circuitPlayBasicCircuit.playTimerFired(dt)

    def playBasicCircuitRedrawAll(self, screen):
        self.circuitPlayBasicCircuit.playRedrawAll(screen)

###############################################################################      
#play basic resistor circuit

    def playBasicResistorCircuitMousePressed(self, mouseX, mouseY):
        self.circuitPlayBasicResistorCircuit.playMousePressed(mouseX, mouseY)

    def playBasicResistorCircuitMousePosition(self, mouseX, mouseY):
        self.circuitPlayBasicResistorCircuit.playMousePosition(mouseX, mouseY)

    def playBasicResistorCircuitKeyPressed(self, keyCode):
        self.circuitPlayBasicResistorCircuit.playKeyPressed(keyCode)

    def playBasicResistorCircuitKeyReleased(self, keyCode):
        pass

    def playBasicResistorCircuitTimerFired(self, dt):
        self.circuitPlayBasicResistorCircuit.playTimerFired(dt)

    def playBasicResistorCircuitRedrawAll(self, screen):
        self.circuitPlayBasicResistorCircuit.playRedrawAll(screen)


##############################################################################
#paused 

    def pausedMousePressed(self, x, y):
        pass

    def pausedMousePosition(self, x, y):
        pass

    def pausedKeyPressed(self, keyCode):
        pass

    def pausedKeyReleased(self, keyCode):
        pass

    def pausedTimerFired(self, dt):
        pass

    def pausedRedrawAll(self, screen):
        pass


###############################################################################
#Instructions

    def instructMousePressed(self, x, y):
        pass

    def instructMousePosition(self, x, y):
        pass

    def instructKeyPressed(self, keyCode):
        pass

    def instructKeyReleased(self, keyCode):
        pass

    def instructTimerFired(self, dt):
        pass

    def instructRedrawAll(self, screen):
        pass       

    ##############################################################################
#gameOver

    def gameOverMousePressed(self, x, y):
        pass

    def gameOverMousePosition(self, x, y):
        pass

    def gameOverKeyPressed(self, keyCode):
        pass

    def gameOverKeyReleased(self, keyCode):
        pass

    def gameOverTimerFired(self, dt):
        pass

    def gameOverRedrawAll(self, screen):
        pass
     

################################################################################
#big stuff below

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=900, height=500, fps=100, title="Circuitos"):
        self.width = 1000
        self.height = 600
        self.fps = fps
        self.title = title
        self.bgColor = (255, 255, 255)
        pygame.init()
        
    def doLoop(self,func,time,screen):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                func['mousePressed'](*(event.pos))
            
            elif (event.type == pygame.MOUSEMOTION and
                    event.buttons == (0, 0, 0)):
                func['mousePosition'](*(event.pos))
        
            elif event.type == pygame.KEYDOWN:
                self._keys[event.key] = True
                func['keyPressed'](event.key)

            elif event.type == pygame.KEYUP:
                self._keys[event.key] = False
                func['keyReleased'](event.key)
                
            elif event.type == pygame.QUIT:
                self.playing = False
        func['timerFired'](time)
        func['redrawAll'](screen)

##################################################################
    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        self.playing = True
        while self.playing:
            screen.fill(self.bgColor)
            time = clock.tick(self.fps)
            # the 'name' functions are dictionaries that hold the key, mouse and draw func for a mode
            if self.mode == 'home':
                self.doLoop(self.homeFunctions,time,screen)
            elif self.mode == 'paused':
                self.doLoop(self.pausedFunctions,time,screen)
            elif self.mode == 'playBasicCircuit':
                self.doLoop(self.playBasicCircuitFunctions,time,screen)
            elif self.mode == 'playBasicResistorCircuit':
                self.doLoop(self.playBasicResistorCircuitFunctions,time,screen)
            elif self.mode == 'instructions':
                self.doLoop(self.instructionFunctions,time,screen)
            elif self.mode == 'gameOver':
                self.doLoop(self.gameOverFunctions,time,screen)
            pygame.display.update()
            
        pygame.quit()

def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()