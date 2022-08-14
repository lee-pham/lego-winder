#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, OUTPUT_B, SpeedPercent
from random import random


WATCH_ROTATIONS_PER_HOUR = 50
gear_ratio = 56/40
motor_rotations = WATCH_ROTATIONS_PER_HOUR * gear_ratio

motor = MediumMotor(OUTPUT_B)
direction = 1 if random() < .5 else -1
motor.on_for_rotations(SpeedPercent(15 * direction), motor_rotations, brake=False)
