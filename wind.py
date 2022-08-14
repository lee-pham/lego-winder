#!/usr/bin/env python3

from ev3dev2.motor import MediumMotor, OUTPUT_B, SpeedPercent

motor = MediumMotor(OUTPUT_B)
motor.on_for_rotations(SpeedPercent(10), 5)
