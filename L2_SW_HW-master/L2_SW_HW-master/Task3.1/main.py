

#!/usr/bin/env python
# importation des bibliothèques
import RPi.GPIO as GPIO
import time


# Initialisation des broches du  GPIO et temporisation
GPIO.setmode(GPIO.BOARD)

LED_list = (7,11,12,13,15,16,18,22)
LED_list2= (22,18,16,15,13,12,11,7)

GPIO.setup(LED_list, GPIO.OUT, initial=GPIO.LOW)

duree = 0.5




# chenillard
for i in range(1):
    # definir pour chaque LED de la liste son état : HIGH (allumée), LOW (éteinte)
    # commande équivalente à 3 instructions
    # GPIO.output(rouge,GPIO.HIGH)
    # GPIO.output(vert,GPIO.LOW)
    # GPIO.output(orange,GPIO.LOW)
    GPIO.output(LED_list, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
    time.sleep(duree)

    for i in range(1):
        # definir pour chaque LED de la liste son état : HIGH (allumée), LOW (éteinte)
        # commande équivalente à 3 instructions
        # GPIO.output(rouge,GPIO.HIGH)
        # GPIO.output(vert,GPIO.LOW)
        # GPIO.output(orange,GPIO.LOW)
        GPIO.output(LED_list2, (GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
        time.sleep(duree)
        GPIO.output(LED_list2, (GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
        time.sleep(duree)
        GPIO.output(LED_list2, (GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
        time.sleep(duree)
        GPIO.output(LED_list2, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
        time.sleep(duree)
        GPIO.output(LED_list2, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
        time.sleep(duree)
        GPIO.output(LED_list2, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH, GPIO.HIGH))
        time.sleep(duree)
        GPIO.output(LED_list2, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.HIGH))
        time.sleep(duree)
        GPIO.output(LED_list2, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.LOW))
        time.sleep(duree)


    GPIO.cleanup()