import buildhat
import random


WATCH_ROTATIONS_PER_HOUR = 50
MOE = .85
gear_ratio = 60/36
motor_rotations = WATCH_ROTATIONS_PER_HOUR * gear_ratio

motor = buildhat.Motor("C")
direction = 1 if random.random() < .5 else -1
motor.run_for_rotations(direction * motor_rotations / MOE)
