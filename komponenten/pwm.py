# pwm.py
# Author: Dennis Gieger

# Bibliotheken import
from __future__ import division

# Basis Klasse
class BasisPWM:
    programm_laeuft = True
    beschleuniging = 0
    lenkung = 0

	# Methode für die ein und ausgabe 
    def ausfuehren_parallel(self, beschleuniging, lenkung):
        self.beschleuniging = beschleuniging
        self.lenkung = lenkung



	# Thread beenden
    def beenden(self):
        self.programm_laeuft = False
        print('PWM beenden')
        time.sleep(.5)


# Klasse zur Regelung des Motors und Lenkservos für Raspberry Pi
class PWM(BasisPWM):
    name = "PWM"

	# PWM initialisierung
    def __init__(self,tt):
        self.client = tt.CarClient()
        self.car_controls = tt.CarControls()

	# Endlosschleife für die Regelung
    def aktualisieren(self):
        while self.programm_laeuft:
            
            #print(self.beschleuniging,self.lenkung)
            self.car_controls.throttle = self.beschleuniging
            self.car_controls.steering = self.lenkung
            self.client.setCarControls(self.car_controls)
