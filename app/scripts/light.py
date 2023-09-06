# light.py

class Light:
    def __init__(self):
        self.status = False

    def turn_on(self):
        # Code to turn on the light
        self.status = True

    def turn_off(self):
        # Code to turn off the light
        self.status = False

if __name__ == "__main__":
    light = Light()
    light.turn_on()
    print(light.status)
    light.turn_off()
    print(light.status)
