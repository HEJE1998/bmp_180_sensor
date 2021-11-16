#Jeldrik Hemme
#ETS 2021
#16.11.2021

#Hardware: ESP32 und den Sensor BMP180 angeschlossen 

#Version: 0.1

#Importieren der Klassen 
from bmp180 import BMP180
from machine import I2C, Pin

#Konfigurationene
bus = I2C(scl=Pin(22), sda=Pin(21), freq=100000)
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325

temperatur = bmp180.temperature
ausgabewert_temperatur = round(temperatur)

#Auslesen der Werte und berechnen der Ausgabewerte 
druck = bmp180.pressure
druck_1 = druck / 100
ausgabewert_druck = round(druck_1, 2)

#Ausgabebefehle
print('Temperatur in Grad Celsius: {0}'.format(ausgabewert_temperatur))
print('Luftdruck in Pascal: {0}'.format(ausgabewert_druck))

