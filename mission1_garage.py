from pysimverse import Drone
import time

drone = Drone()
drone.connect()
drone.take_off()
drone.set_speed(500)

drone.rotate(-40)
drone.move_forward(450)
drone.rotate(155)
time.sleep(2)
drone.move_down(80)
drone.move_forward(600)
# drone.rotate(30)
# drone.move_forward(280)
# drone.rotate(-130)


drone.land()
time.sleep(1)