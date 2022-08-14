#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, OUTPUT_B, SpeedPercent

WATCH_ROTATIONS_PER_HOUR = 50
gear_ratio = 56/40
motor_rotations = WATCH_ROTATIONS_PER_HOUR * gear_ratio

motor = MediumMotor(OUTPUT_B)
motor.on_for_rotations(SpeedPercent(10), motor_rotations)
