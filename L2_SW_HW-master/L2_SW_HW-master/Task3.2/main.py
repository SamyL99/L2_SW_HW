#!/usr/bin/env python
# importation des bibliothèques
import RPi.GPIO as GPIO  # Gestion des GPIO
from time import sleep   # Gestion du temps

GPIO.setmode(GPIO.BOARD)   # La numerotation choisie
GPIO.setup(32, GPIO.IN)  # Une entree : le poussoir
LED_list = (7,11,12,13,15,16,18,22)


GPIO.setup(LED_list, GPIO.OUT, initial=GPIO.LOW)

duree = 0.5

def my_callback(channel):
  if GPIO.input(channel):
    print('GPIO %s 0->1' %channel)
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
  else:
    print('GPIO %s 1->0' %channel)
    for i in range(1):
    # definir pour chaque LED de la liste son état : HIGH (allumée), LOW (éteinte)
    # commande équivalente à 3 instructions
    # GPIO.output(rouge,GPIO.HIGH)
    # GPIO.output(vert,GPIO.LOW)
    # GPIO.output(orange,GPIO.LOW)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)
    GPIO.output(LED_list, (GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH))
    time.sleep(duree)

print("Le programme prendra fin dans 60s.")
print("Vous pouvez aussi terminer avec CTRL+C \n")

GPIO.add_event_detect(32, GPIO.BOTH, callback=my_callback)
print("Maintenant, le programme surveille les actions sur le poussoir\n")

try:
  sleep(60)

except KeyboardInterrupt:
  print("\nInterruption par clavier.")

finally:
  print("On arrete et nettoie les broches pour les liberer")
  print("en vue d'une prochaine utilisation.")
  GPIO.cleanup()

