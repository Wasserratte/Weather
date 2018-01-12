
from flask import Flask
from flask import render_template
import smbus
import time



app = Flask(__name__)


@app.route("/")
def MPL3115A2():


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


#Output data to screen

    
    weather_data = {'pressure': pressure, 'altitude': altitude, 'cTemp': cTemp, 'fTemp': fTemp}


    return render_template("home.html", data=weather_data)

    #print weather_data['cTemp']



if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
