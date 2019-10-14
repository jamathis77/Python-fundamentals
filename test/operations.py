
def traffic_light_choice(car, light):
    car_command = ""
    if car == "moving":
        if light == "red":
            car_command = "stop"
    return car_command
