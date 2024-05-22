#IMPORTS
from time import sleep
import math
import scipy.constants
import parameters
from pprint import pprint
import csv

time = 0
speed = 0
distance = 0
tractive_effort = 0

tractive_effort = float(input("Provide the tractive effort [kN]: "))    #TO MA BYC LICZONE, MASA POCIAGu ITP.
gradient = float(input("Provide track gradient [°]: "))
time_step = float(input("Provide the calculation time step [s]: "))
overall_time = float(input("Provide the total calculation time [s]: "))
acceleration_force = (parameters.tractive_force - tractive_effort + ((parameters.mass * 1000) * scipy.constants.g * math.sin(gradient)))
max_speed = min(parameters.speed_max, ((parameters.power_max / acceleration_force) * 3.6))
print("Speed limit: " + str(max_speed) + "km/h")

#DICTIONARY OF CALCULATED PARAMETERS
travel_record = {}
with open('test.csv','w') as file:
    writer = csv.writer(file, delimiter='\t',lineterminator='\n',)
    row_content = ["Time [s]", "Speed [km/s]", "Travelled distance [km]", "Motor rotational speed [rpm]", "Power at wheel [kW]", "Line power drawn [kW]"]
    writer.writerow(row_content)

while time < overall_time:

    if time + time_step < overall_time:
        time = time + time_step
    else:
        time = overall_time

    #CALCULATIONS:
    #ACCELERATION [m/s²] AND SPEED [km/h]
    acceleration = (parameters.tractive_force - tractive_effort + (parameters.mass * scipy.constants.g * math.sin(gradient))) / (parameters.mass + (parameters.axle_count * 4)) #wspolczynnik mas wirujacych: ~4 t

    if speed + (acceleration * time_step * 3.6) < max_speed:
        speed = speed + (acceleration * time_step * 3.6)
    else:
        speed = max_speed

    distance = distance + (speed * time_step)

    #ROTATIONAL SPEED OF THE TRACTION MOTOR [rpm]
    rotational_speed = (speed * 60) / (2 * math.pi * (parameters.wheel_diameter / 1000))
    rotational_speed_motor = rotational_speed * parameters.gear_ratio

    #POWER AT WHEEL/LINE POWER [kW]
    power_at_wheel = tractive_effort * (speed / 3.6)
    line_power = power_at_wheel / parameters.traction_chain_efficiency

    #FORMATTING
    time_0f = ("{:.0f}".format(time))
    acceleration_2f = ("{:.2f}".format(acceleration))
    speed_1f = ("{:.1f}".format(speed))
    distance_2f = ("{:.2f}".format(distance))
    distance_2f_km = ("{:.2f}".format(distance / 1000))
    rotational_speed_motor_2f = ("{:.2f}".format(rotational_speed_motor))
    power_at_wheel_0f = ("{:.0f}".format(power_at_wheel))
    line_power_0f = ("{:.0f}".format(line_power))
    
    #ADD PARAMETERS TO TRAVEL RECORD
    parameters_in_point = {}
    parameters_in_point["acceleration"] = acceleration
    parameters_in_point["speed"] = speed
    parameters_in_point["distance"] = distance
    parameters_in_point["rotational_speed_motor"] = rotational_speed_motor
    parameters_in_point["power_at_wheel"] = power_at_wheel
    parameters_in_point["line_power"] = line_power
    travel_record[time] = parameters_in_point

    with open('test.csv','a') as file:
        writer = csv.writer(file, delimiter='\t',lineterminator='\n',)
        row_content = [time, speed_1f, distance_2f_km, rotational_speed_motor_2f, power_at_wheel_0f, line_power_0f]
        writer.writerow(row_content)

    #DISPLAYING
    print("Time point: " + str(time_0f) + " s")
    print("Current acceleration: " + str(acceleration_2f) + " m/s²")    
    print("Current speed: " + str(speed_1f) + " km/h")
    if distance < 1000:
        print("Travelled distance: " + str(distance_2f) + " m")
    else:
        print("Travelled distance: " + str(distance_2f_km) + " km")
    print("Motor rotational speed: " + str(rotational_speed_motor_2f) + " rpm")
    print("Power at wheel: " + str(power_at_wheel_0f) + " kW")
    print("Line power: " + str(line_power_0f) + " kW")
    sleep(0.5)

pprint(travel_record)