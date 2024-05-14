from time import sleep
import math
import parameters

time = 0
speed = 0
distance = 0
tractive_effort = 0

tractive_effort = float(input("Provide the required tractive effort [kN]: "))
acceleration = float(input("Provide the vehicle acceleration [m/s²]: "))
time_step = float(input("Provide the calculation time step [s]: "))
overall_time = float(input("Provide the total calculation time [s]: "))
max_speed = min(parameters.speed_max, ((parameters.power_max / tractive_effort) * 3.6))
print(max_speed)

while time < overall_time:

    time = time + time_step

    #CALCULATIONS
    if speed + (acceleration * time_step * 3.6) < max_speed:
        speed = speed + (acceleration * time_step * 3.6)
    else:
        speed = max_speed

    distance = distance + (speed * time_step)

    #ROTATIONAL SPEED OF THE TRACTION MOTOR [rpm]
    rotational_speed = (speed * 60) / (2 * math.pi * (parameters.wheel_diameter / 1000))
    rotational_speed_motor = rotational_speed * parameters.gear_ratio

    #FORMATTING
    time_0f = ("{:.0f}".format(time))
    speed_1f = ("{:.1f}".format(speed))
    distance_2f = ("{:.2f}".format(distance))
    rotational_speed_motor_2f = ("{:.2f}".format(rotational_speed_motor))
    
    #DISPLAYING
    print("Time point: " + str(time_0f) + " s")
    print("Current speed: " + str(speed_1f) + " km/h")
    print("Travelled distance: " + str(distance_2f) + " m")
    print("Motor rotational speed: " + str(rotational_speed_motor_2f) + " rpm")
    sleep(0.5)
