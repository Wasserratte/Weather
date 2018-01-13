import Adafruit_MCP3008

CLK=18
MISO=23
MOSI=24
CS=25

mcp=Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


class Humidity():

    def __init__(self):
        self.humidity = 0

    def Value(self):

        value = mcp.read_adc(0)
        voltage = value * (3300.00/1024.00)     #Millivolt
        voltage2 = voltage / 1000.00    #Volt



        if voltage2 < 1.03:
            Humidity = 20

        elif voltage2 < 1.35:
            Humidity = 30

        elif voltage2 < 1.67:
            Humidity = 40

        elif voltage2 < 1.98:
            Humidity = 50

        elif voltage2 < 2.26:
            Humidity = 60

        elif voltage2 < 2.50:
           Humidity = 70

        elif voltage2 < 2.70:
            Humidity = 80

        else:
            Humidity = 90

        self.humidity = Humidity

        return self.humidity

    def get_value():
        return self.humidity
