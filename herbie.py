# herbie.py
# Author: Dennis Gieger
import airsim
# Komponenten import
from fahrzeug import Herbie
from komponenten.steuerung import Logitech_F710 as Steuerung
from komponenten.kamera import USB_kamera as Kamera

#from komponenten.pilot import Fahrer
from komponenten.pwm import PWM
from komponenten.datenspeicher import Datenspeicher
#from komponenten.webserver.server import WebServer

print('Herbie startet')
client = airsim.CarClient()
client.confirmConnection()
client.enableApiControl(True)

# Instanziierung der Kopmponenten
herbie = Herbie()
steuerung = Steuerung()
kamera = Kamera(airsim)

#fahrer = Fahrer()
pwm = PWM(airsim)
datenspeicher = Datenspeicher()
#server = WebServer()

print('Komponenten laden...')

"""
Komponenten werden nach dem fogendem Schema angelegt:
	herbie.hinzufuegen(komponente, eingang=['eingang_name',...], ausgang=['ausgang_name',...], ausfuehren_parallel = True or False)
"""

# Hinzufügen der Komponenten
herbie.hinzufuegen(steuerung, ausgang=['beschleunigung','lenkung','aufnahme','modus','speichern','programm_ende'], ausfuehren_parallel=True)
herbie.hinzufuegen(kamera, ausgang=['kamera'], ausfuehren_parallel=True)


#herbie.hinzufuegen(fahrer, eingang=['kamera','beschleunigung','lenkung','modus'], ausgang=['lenkung','beschleunigung'], ausfuehren_parallel=True)

herbie.hinzufuegen(pwm, eingang=['beschleunigung','lenkung'], ausfuehren_parallel=True)
herbie.hinzufuegen(datenspeicher, eingang=['kamera','beschleunigung','lenkung','aufnahme','speichern','besch_x','besch_y','besch_z','gyro_x','gyro_y','gyro_z'], ausfuehren_parallel=True)
#herbie.hinzufuegen(server, eingang=['kamera','beschleunigung','lenkung'],ausfuehren_parallel=True)

# Hauptschleife starten
herbie.starten()