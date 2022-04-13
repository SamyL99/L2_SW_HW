

#!/usr/bin/env python
# importation des bibliothèques
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) #choisir le mode   BOARD
GPIO.setup(11,GPIO.OUT)  #declarer la broche et specifier
p=GPIO.PWM(11,200)    #creation de PWM instance
p.start(0)     #initialiser a 0
while True :  #boucle de parcours
    for duty in range(0,101,1):  #boucle pour augmenter la luminosité
        p.ChangeDutyCycle(duty)  #changer le rapport cyclique
        time.sleep(0.01) #mettre en attente pour quelques secondes
    time.sleep(0.5)

    for duty in range(100,-1,-1): #boucle pour diminuer la luminosité
        p.ChangeDutyCycle(duty)
        time.sleep(0.01)
    time.sleep(0.5)

    GPIO.cleanup() #pour securité


