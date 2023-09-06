# water_pump.py

class WaterPump:
    def __init__(self):
        self.status = False

    def turn_on(self):
        # Code to turn on the water pump
        self.status = True

    def turn_off(self):
        # Code to turn off the water pump
        self.status = False

if __name__ == "__main__":
    water_pump = WaterPump()
    water_pump.turn_on()
