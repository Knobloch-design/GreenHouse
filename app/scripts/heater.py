# heater.py

class Heater:
    def __init__(self):
        self.status = False

    def turn_on(self):
        # Code to turn on the heater
        self.status = True

    def turn_off(self):
        # Code to turn off the heater
        self.status = False

if __name__ == "__main__":
    heater = Heater()
    heater.turn_on()
    print(heater.status)
    heater.turn_off()
    print(heater.status)
