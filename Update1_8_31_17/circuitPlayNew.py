import pygame
import random
import math
import string
import copy
import ast



pygame.init()
pygame.display.init()
titleFont = pygame.font.SysFont("Impact", 60)
subTitleFont = pygame.font.SysFont("Impact", 30)
subSubTitleFont = pygame.font.SysFont("Impact", 20)


class BasicCircuit(object):
    def __init__(self, other):
        self.width = other.width
        self.height = other.height

        self.status = 'Resistor'
        self.resistorCircuit = ''
        self.batteryVoltage = ''
        self.currentAmps = ''
        
        self.miniFontSize = 20
      
        self.statuses = ['Resistor', 'Battery', 'Current', 'Redo Something']
        self.screenLabels = ['Resistor Circuit', 'hit enter when done | press r to restart', 
                              'Total Resistance of', 'Battery Voltage',
                              'Press Enter to Calculate Current', 
                              'Current Amps', "Complete"]

                        #done x, y , width, height
        self.doneButton = [-2, self.height-80, self.width+10, 90]
        self.doneButtonColor = (175,175,175)
                    #resistors, batteries, current

        self.totalResistance = None
        self.totalVoltage = None
        self.totalCurrent = None

        self.complete = False


#===========================================================================#


    def playMousePressed(self, mouseX, mouseY):
        pass
            

    def playMousePosition(self, mouseX, mouseY):
        pass


##############################################################################

    def parAdd(self, numbers):
        total = 0
        for i in numbers:
            total += 1/i
        return total**-1 if total != 0 else 0

    def solveResistorCircuit(self, infiniteList, series = True):
        currentAddition = []
        for elements in infiniteList:
            if not isinstance(elements, list):
                currentAddition.append(elements)
            else:
                series = not series
                currentAddition.append(self.solveResistorCircuit(elements, series))
                series = not series
        if series:
            return sum(currentAddition)
        else:
            return self.parAdd(currentAddition)



############################ KEY PRESSED #######################################
#Resistor KeyPressed
    def isValidResistorKey(self, keyCode):
        if (keyCode == pygame.K_LEFTBRACKET or keyCode == pygame.K_RIGHTBRACKET
            or keyCode == pygame.K_COMMA or chr(keyCode).isdigit()):
            return True
        elif (keyCode == pygame.K_BACKSPACE):
            self.resistorCircuit = self.resistorCircuit[:-1]
        else:
            return False

    def resistorKeyPressed(self, keyCode):
        if self.isValidResistorKey(keyCode):
            #Currently assuming that this makes a solvable circuit, 
            #later introduce way of inputting a wrong circuit and the program noticing
            self.resistorCircuit += chr(keyCode)
        if keyCode == pygame.K_RETURN:
            if len(self.resistorCircuit) == 0:
                self.totalResistance = '?'
            else:
                allResistors = '[' + self.resistorCircuit + ']'
                resistorList = ast.literal_eval(allResistors)
                self.totalResistance = round(self.solveResistorCircuit(resistorList), 2)
            if self.totalVoltage == None:
                self.status = 'Battery'
            else:
                self.checkCompleteness()

####################
#Battery KeyPressed
    def isValidBatteryKey(self, keyCode):
        if chr(keyCode).isdigit(): 
            return True
        elif (keyCode == pygame.K_BACKSPACE):
            self.batteryVoltage = self.batteryVoltage[:-1]
        else: return False


    def batteryKeyPressed(self, keyCode):
        if self.isValidBatteryKey(keyCode):
            self.batteryVoltage += chr(keyCode)
        if keyCode == pygame.K_RETURN:
            if len(self.batteryVoltage) == 0:
                self.totalVoltage = '?'
            else:
                self.totalVoltage = self.batteryVoltage
            if self.totalCurrent == None:
                self.status = 'Current'
            else:
                self.checkCompleteness()


################
#Current Key Pressed
    def isValidCurrentKey(self, keyCode):
        if chr(keyCode).isdigit(): 
            return True
        elif (keyCode == pygame.K_BACKSPACE):
            self.currentAmps = self.currentAmps[:-1]
        else: return False

    def currentKeyPressed(self, keyCode):
        if self.isValidCurrentKey(keyCode): 
            self.currentAmps += chr(keyCode)
        if keyCode == pygame.K_RETURN:
            if len(self.currentAmps) == 0:
                if self.totalVoltage != '?' and self.totalResistance != '?':
                    self.totalCurrent = round(float(self.totalVoltage)/float(self.totalResistance), 3)
                    self.checkCompleteness()
            else:
                self.totalCurrent = self.currentAmps
                self.checkCompleteness()


###############
#KeyPressed
                        
    def playKeyPressed(self, keyCode):
        if keyCode == pygame.K_r: #reset 
            self.__init__(self)

        if self.status == 'Resistor':
            self.resistorKeyPressed(keyCode)
            return

        if self.status == 'Battery':
            self.batteryKeyPressed(keyCode)
            return
            

        if self.status == 'Current':
            self.currentKeyPressed(keyCode)
            return


    def playKeyReleased(self, keyCode):
        pass


    def checkCompleteness(self):
        if self.totalResistance != None and self.totalVoltage != None and self.totalCurrent != None:
            if self.totalVoltage == '?':
                if self.totalResistance != '?':
                    if self.totalCurrent != '?':
                        self.totalVoltage = round(float(self.totalCurrent)*float(self.totalResistance), 3)
                    else:
                        self.status = 'Current'
                else:
                    self.status = 'Resistor'
                return
       

            elif self.totalResistance == '?':
                if self.totalVoltage != '?':
                    if self.totalCurrent != '?':
                        self.totalResistance = round(float(self.totalVoltage) / float(self.totalCurrent), 3)
                    else:
                        self.status = 'Current'
                else:
                    self.status = 'Voltage'
                return


            elif self.totalCurrent == '?':
                if self.totalVoltage != '?':
                    if self.totalResistance != '?':
                        self.totalCurrent = round(float(self.totalVoltage) / float(self.totalResistance), 3)
                    else:
                        self.status = 'Resistor'
                else:
                    self.status = 'Voltage'
                return

            self.complete = True


        

    def playTimerFired(self, dt):
        self.checkCompleteness()

# ================================DRAWING===================================#

    def drawBg(self, screen):
        pygame.draw.rect(screen, (50,175,255), [0,0, self.width, self.height])


    def drawMainTitle(self, screen):
        if self.complete == True:
            title = self.screenLabels[6]
            title = titleFont.render(title, False, (255,255,255))
            centered = title.get_rect(center=(self.width//2, self.height//4))
            screen.blit(title, centered) 
            return

        if self.status == 'Resistor':
            title = self.screenLabels[0]
            title = titleFont.render(title, False, (255,255,255))
            centered = title.get_rect(center=(self.width//2, self.height//4))
            screen.blit(title, centered) 

            subTitle = subTitleFont.render('['+self.resistorCircuit+']', False, (255,255,255))
            centered = subTitle.get_rect(center=(self.width//2, self.height//4+60))
            screen.blit(subTitle, centered)
            return

        if self.status == 'Battery':
            title = self.screenLabels[3]
            title = titleFont.render(title, False, (255,255,255))
            centered = title.get_rect(center=(self.width//2, self.height//4))
            screen.blit(title, centered) 

            subTitle = subTitleFont.render(str(self.batteryVoltage)+ ' V', False, (255,255,255))
            centered = subTitle.get_rect(center=(self.width//2, self.height//4+60))
            screen.blit(subTitle, centered)
            return

        if self.status == 'Current':
            if self.totalVoltage != '?' and self.totalResistance != '?':
                title = self.screenLabels[4]
                title = titleFont.render(title, False, (255,255,255))
                centered = title.get_rect(center=(self.width//2, self.height//4))
                screen.blit(title, centered) 
            else:
                title = self.screenLabels[5]
                title = titleFont.render(title, False, (255,255,255))
                centered = title.get_rect(center=(self.width//2, self.height//4))
                screen.blit(title, centered) 

                subTitle = subTitleFont.render(str(self.currentAmps)+ ' A', False, (255,255,255))
                centered = subTitle.get_rect(center=(self.width//2, self.height//4+60))
                screen.blit(subTitle, centered)
            return



    def drawDoneButton(self, screen):
        x0, y0, width, height = self.doneButton
        color = self.doneButtonColor
        pygame.draw.rect(screen, color, [x0,y0,width,height])

        doneTitle = subTitleFont.render(self.screenLabels[1], False, (255,255,255))
        centered = doneTitle.get_rect(center=(self.width//2, self.height-40))
        screen.blit(doneTitle, centered) 

    def drawTotals(self, screen):
        margin = x0 = 5
        if self.totalResistance != None:
            #draw 'Total Resistance: ' #of total re
            totalResistance = 'Total Resistance: ' + str(self.totalResistance) + ' ohms'
            totResistance = subSubTitleFont.render(totalResistance, False, (255,255,255))
            screen.blit(totResistance, (x0, x0))

        if self.totalVoltage != None:
            #draw 'Total Voltage: ' #of total re
            totalVoltage= 'Total Voltage: ' + str(self.totalVoltage) + ' V'
            totalVoltage = subSubTitleFont.render(totalVoltage, False, (255,255,255))
            screen.blit(totalVoltage, (x0, x0+self.miniFontSize+margin))

        if self.totalCurrent != None:
            #draw 'Total Current: ' #of total 
            totalCurrent = 'Total Current: ' + str(self.totalCurrent) + ' A'
            totalCurrent = subSubTitleFont.render(totalCurrent, False, (255,255,255))
            screen.blit(totalCurrent, (x0, x0+2*self.miniFontSize+2*margin))


    def playRedrawAll(self, screen):
        self.drawBg(screen)
        self.drawMainTitle(screen)
        self.drawDoneButton(screen)

        #draw basic circuit values in the top
        self.drawTotals(screen)

