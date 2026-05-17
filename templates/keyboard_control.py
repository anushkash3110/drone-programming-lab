from pysimverse import Drone
import keyboard
import time


SPEED = 50


def get_keyboard_input():

    left_right = 0
    forward_backward = 0
    up_down = 0
    yaw = 0

    if keyboard.is_pressed("w") or keyboard.is_pressed("up"):
        forward_backward = SPEED

    if keyboard.is_pressed("s") or keyboard.is_pressed("down"):
        forward_backward = -SPEED

    if keyboard.is_pressed("a") or keyboard.is_pressed("left"):
        left_right = -SPEED

    if keyboard.is_pressed("d") or keyboard.is_pressed("right"):
        left_right = SPEED

    if keyboard.is_pressed("r"):
        up_down = SPEED

    if keyboard.is_pressed("f"):
        up_down = -SPEED

    if keyboard.is_pressed("q"):
        yaw = -SPEED

    if keyboard.is_pressed("e"):
        yaw = SPEED

    return [
        left_right,
        forward_backward,
        up_down,
        yaw
    ]


def main():

    drone = Drone()

    drone.connect()

    print("Response: Connected")

    drone.take_off()

    print("Drone has taken off.")

    while True:

        if keyboard.is_pressed("x"):
            break

        values = get_keyboard_input()

        drone.send_rc_control(
            values[0],
            values[1],
            values[2],
            values[3]
        )

        print(
            f"RC Data -> "
            f"LR:{values[0]} "
            f"FB:{values[1]} "
            f"UD:{values[2]} "
            f"YAW:{values[3]}"
        )

        time.sleep(0.05)

    drone.land()

    print("Drone landed.")

    time.sleep(1)


if __name__ == "__main__":
    main()