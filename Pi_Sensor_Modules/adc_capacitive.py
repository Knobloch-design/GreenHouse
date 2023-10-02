import spidev
import time

# Create an SPI interface
spi = spidev.SpiDev()
spi.open(0, 0)  # (bus, device)

def read_adc(channel):
    # MCP3008 provides 10 bits of resolution, so we read two bytes (16 bits).
    # The first 3 bits are the control bits, and the remaining 13 bits are the ADC result.
    # We shift the result right by 3 bits to get the 10-bit value.
    adc = spi.xfer2([1, 8 + channel << 4, 0])
    return ((adc[1] & 3) << 8) + adc[2]

try:
    while True:
        moisture_value = read_adc(0)  # Read from CH0 (or the channel your sensor is connected to)

        # You may need to calibrate the threshold values based on your sensor.
        if moisture_value < 300:
            print("Very Wet")
        elif 300 <= moisture_value < 600:
            print("Wet")
        else:
            print("Dry")

        time.sleep(2)  # Adjust the delay time as needed

except KeyboardInterrupt:
    pass

finally:
    spi.close()
