
from flask import Flask
from flask import render_template
import smbus
import time
from humidityhelper import Humidity
from mplhelper import MPL

app = Flask(__name__)

wet = Humidity()

air = MPL()


@app.route("/")
def HonigWetter():


    sun = air.Value()


    pressure = sun['pressure']
    cTemp = sun['cTemp']
    fTemp = sun['fTemp']
    altitude = sun['altitude']


    value = wet.Value()


    humidity = value





    weather_data = {'pressure': pressure, 'altitude': altitude, 'cTemp': cTemp, 'fTemp': fTemp, 'humidity': humidity}

    return render_template("home.html", data=weather_data)





if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
