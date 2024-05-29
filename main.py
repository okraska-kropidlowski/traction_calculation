#IMPORTS
import math
import scipy.constants
import parameters

tractive_effort = float(input("Provide the tractive effort [kN]: "))    #TO MA BYC LICZONE, MASA POCIAGU ITP.
tractive_force_percentage = float(input("Tractive force usage [%]: "))/100
gradient = math.radians(float(input("Provide track gradient [°]: ")))
acceleration_force = (parameters.tractive_force * tractive_force_percentage) - tractive_effort + (parameters.mass * scipy.constants.g * math.sin(gradient))
if acceleration_force <= 0:
    max_speed = 0
else:
    max_speed = min(parameters.speed_max, ((parameters.power_max / acceleration_force) * 3.6))
print("Speed limit: " + str(max_speed) + "km/h")

with open(forces.py, "w") as forces:
    forces.tractive_effort = tractive_effort
    forces.acceleration_force = acceleration_force
    forces.gradient = gradient
    forces.max_speed = max_speed