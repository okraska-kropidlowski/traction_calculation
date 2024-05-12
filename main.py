from time import sleep

time = 0
speed = 0
distance = 0

acceleration = float(input("Provide the vehicle acceleration [m/s²]: "))
time_step = float(input("Provide the calculation time step [s]: "))
overall_time = float(input("Provide the total calculation time [s]: "))

while time < overall_time:
    time = time + time_step
    speed = speed + (acceleration * time_step)
    time_0f = ("{:.0f}".format(time))
    speed_2f = ("{:.2f}".format(speed))
    print("Time point: " + str(time_0f) + " s")
    print("Current speed: " + str(speed_2f) + " m/s²")
    sleep(0.5)