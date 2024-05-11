from time import sleep

time = 0
speed = 0

acceleration = float(input("Provide the vehicle acceleration [m/s²]: "))
time_step = float(input("Provide the calculation time step [s]: "))
overall_time = float(input("Provide the total calculation time [s]: "))

while time < overall_time:
    speed = speed + (acceleration * time_step)
    speed_2f = ("{:.2f}".format(speed))
    print("Current speed: " + str(speed_2f) + " m/s²")
    time = time + time_step
    sleep(0.1)