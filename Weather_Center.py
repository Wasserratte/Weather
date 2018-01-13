
from flask import Flask
from flask import render_template
import smbus
import time
import Adafruit_MCP3008


app = Flask(__name__)

CLK=18
MISO=23
MOSI=24
CS=25

mcp=Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


@app.route("/")
def HonigWetter():


    bus = smbus.SMBus(1)


    bus.write_byte_data(0x60, 0x26, 0xB9)


    bus.write_byte_data(0x60, 0x13, 0x07)


    bus.write_byte_data(0x60, 0x26, 0xB9)

    time.sleep(1)



    data = bus.read_i2c_block_data(0x60, 0x00, 6)



    tHeight = ((data[1] * 65536) + (data[2] *256) + (data[3] & 0xF0)) / 16

    temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16

    altitude = tHeight / 16.0

    cTemp = temp / 16.0

    fTemp = cTemp * 1.8 + 32


    bus.write_byte_data(0x60, 0x26, 0x39)

    time.sleep(1)


    data = bus.read_i2c_block_data(0x60, 0x00, 4)



    pres = ((data[1] + 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16

    pressure = (pres / 4.0) / 1000.0







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


    humidity = Humidity

    weather_data = {'pressure': pressure, 'altitude': altitude, 'cTemp': cTemp, 'fTemp': fTemp, 'humidity': humidity}

    return render_template("home.html", data=weather_data)





if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
