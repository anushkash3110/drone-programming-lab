from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off()
drone.set_speed(100)



drone.land()
time.sleep(1)