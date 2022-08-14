#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank

motor = MediumMotor(OUTPUT_B)
motor.on_for_rotations(SpeedPercent(75), 5)
