import buildhat
import random


WATCH_ROTATIONS_PER_HOUR = 50
MOE = .85
gear_ratio_1 = 60/36
gear_ratio_2 = 36/12
motor_rotations = WATCH_ROTATIONS_PER_HOUR * gear_ratio_1 * gear_ratio_2

motor = buildhat.Motor("C")
direction = 1 if random.random() < .5 else -1
motor.run_for_rotations(direction * motor_rotations / MOE)
