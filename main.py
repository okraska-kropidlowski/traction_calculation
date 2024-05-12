from time import sleep

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

    #FORMATTING
    speed_kmh = speed * 3.6
    time_0f = ("{:.0f}".format(time))
    speed_2f = ("{:.2f}".format(speed_kmh))

    #DISPLAYING
    print("Time point: " + str(time_0f) + " s")
    print("Current speed: " + str(speed_2f) + " km/h")
    sleep(0.5)