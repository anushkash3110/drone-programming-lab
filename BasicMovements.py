from djitellopy import Tello
from time import sleep

me = Tello()
me.connect()
print(me.get_battery())