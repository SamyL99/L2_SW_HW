#!/usr/bin/env python3


import RPi.GPIO as GPIO #Importe la bibliotheque pour controler les GPIOs

GPIO.setmode(GPIO.BOARD) #defnit le mode de numeration (board)
#definition des variables
led=11
bouton=12
#definit le numero du port GPIO qui alimente la led
GPIO.setup(led,GPIO.OUT) #active le controle du GPIO

#initialisation d'etat de la led
GPIO.setup(bouton, GPIO.IN , pull_up_down=GPIO.PUD_UP)



print('Execution du programme')
print('Appuyer sur le bouton poussoirpour allumer la led')
try:
    while 1:
        #le programme tourne en boucle dans l'attente d'evenement sur le poussoir
        if(GPIO.input(bouton)==0):
            GPIO.output(led,1)

        else :
            GPIO.output(led,0)

except :
    GPIO.cleanup()




