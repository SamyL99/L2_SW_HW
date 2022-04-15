

#!/usr/bin/env python
import RPi.GPIO as GPIO  # Gestion des GPIO
from time import sleep   # Gestion du temps

GPIO.setmode(GPIO.BOARD)   # La numerotation choisie
GPIO.setup(11, GPIO.OUT) # Une sortie : la LED
GPIO.setup(12, GPIO.IN)  # Une entree : le poussoir

def my_callback(channel):
  if GPIO.input(channel):
    print('GPIO %s 0->1' %channel)
    GPIO.output(11, GPIO.LOW)
  else:
    print('GPIO %s 1->0' %channel)
    GPIO.output(11, GPIO.HIGH)

print("Le programme prendra fin dans 30s.")
print("Vous pouvez aussi terminer avec CTRL+C \n")

GPIO.add_event_detect(12, GPIO.BOTH, callback=my_callback)
print("Maintenant, le programme surveille les actions sur le poussoir\n")

try:
  sleep(30)

except KeyboardInterrupt:
  print("\nInterruption par clavier.")

finally:
  print("On arrete et nettoie les broches pour les liberer")
  print("en vue d'une prochaine utilisation.")
  GPIO.cleanup()

