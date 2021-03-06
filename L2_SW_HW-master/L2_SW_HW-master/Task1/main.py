#!/usr/bin/env python3


import RPi.GPIO as GPIO #Importe la bibliotheque pour controler les GPIOs

GPIO.setmode(GPIO.BOARD) #defnit le mode de numeration (board)
led=11 #definit le numero du port GPIO qui alimente la led
GPIO.setup(led,GPIO.OUT) #active le controle du GPIO
state=GPIO.input(led)  #lit l'etat actuel du GPIO , vrai si allumé , faux si eteint

if (state) : #Si GPIO allumé state est à l'etat 1
    GPIO.output(led , GPIO.LOW) #On l'éteint
else : #sinon
    GPIO.output(led , GPIO.HIGH) #On l'allume

def destroy(): # pour securité
    GPIO.cleanup()

    #ensuite il suffit de lancer la commande chmode +x /-----> vers le fichier ou se trouve notre programme python
    #et enfin on change l'etat de la diode en executant le code a chaque fois ça va passer de 1 vers 0 , de 0 vers 1




