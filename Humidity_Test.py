import time
import Adafruit_MCP3008

#Software SPI configuration

CLK=18
MISO=23
MOSI=24
CS=25

mcp=Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


#Read data

value = mcp.read_adc(0)
voltage = value * (3300.00/1024.00)	#Millivolt
voltage2 = voltage / 1000.00	#Volt


if voltage2 < 1.03:
    print "20%"

elif voltage2 < 1.35:
    print "30%"

elif voltage2 < 1.67:
    print "40%"

elif voltage2 < 1.98:
    print "50%"

elif voltage2 < 2.26:
    print "60%"

elif voltage2 < 2.50:
    print "70%"

elif voltage2 < 2.70:
    print "80%"

else:
    print "90%"

 


