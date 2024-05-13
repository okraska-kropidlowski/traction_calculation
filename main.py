from time import sleep
import math

#LOCOMOTIVE PARAMETERS
tractive_force_max = 340 #[kN]
power_max = 6400 #[kW]
wheel_diameter = 1250 #[mm]
gear_ratio = 5.261

time = 0
speed = 0
distance = 0

acceleration = float(input("Provide the vehicle acceleration [m/s²]: "))
time_step = float(input("Provide the calculation time step [s]: "))
overall_time = float(input("Provide the total calculation time [s]: "))

while time < overall_time:

    #CALCULATIONS
    time = time + time_step
    speed = speed + (acceleration * time_step)
    distance = distance + (speed * time_step)
    #ROTATIONAL SPEED OF THE TRACTION MOTOR [rpm]
    rotational_speed = (speed * 60) / (2 * math.pi * (wheel_diameter / 1000))
    rotational_speed_motor = rotational_speed * gear_ratio

    #FORMATTING
    speed_kmh = speed * 3.6
    time_0f = ("{:.0f}".format(time))
    speed_2f = ("{:.2f}".format(speed_kmh))
    distance_2f = ("{:.2f}".format(distance))
    rotational_speed_motor_2f = ("{:.2f}".format(rotational_speed_motor))

    #DISPLAYING
    print("Time point: " + str(time_0f) + " s")
    print("Current speed: " + str(speed_2f) + " km/h")
    print("Travelled distance: " + str(distance_2f) + " m")
    print("Motor rotational speed: " + str(rotational_speed_motor_2f) + " rpm")
    sleep(0.5)
