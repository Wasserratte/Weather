
from flask import Flask
from flask import render_template
import smbus
import time
from humidityhelper import Humidity
from mplhelper import MPL
from wetterhelper import Unterfranken

app = Flask(__name__)

wet = Humidity()

air = MPL()

news = Unterfranken()


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


    lion = news.get_Weather()


    bayern = {'Mittelfranken': lion[0], 'Oberbayern': lion[1], 'Niederbayern': lion[2], 'Oberfranken': lion[3],
        'Schwaben': lion[4], 'Oberpfalz': lion[5], 'Unterfranken': lion[6]}



    return render_template("home.html", data=weather_data, main=bayern)




if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
