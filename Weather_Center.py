#Import der Module
from flask import Flask
from flask import render_template
from flask import request
import smbus
import time
from humidityhelper import Humidity
from mplhelper import MPL
from wetterhelper import Unterfranken
from nachrichtenhelper import News_Feed
from apihelper import API_Weather

#Flask application
app = Flask(__name__)

#Instances
wet = Humidity()

air = MPL()

news = Unterfranken()

br = News_Feed()

api = API_Weather()

#Homepage
@app.route("/")
def HonigWetter():

    #Pressure and Temperature

    sun = air.Value()


    pressure = sun['pressure']
    cTemp = sun['cTemp']
    fTemp = sun['fTemp']
    altitude = sun['altitude']


    value = wet.Value()


    humidity = value




    weather_data = {'pressure': pressure, 'altitude': altitude, 'cTemp': cTemp, 'fTemp': fTemp, 'humidity': humidity}


    #Weather-Feed

    lion = news.get_Weather()
    link = news.get_Weather_link()


    bayern = {'Mittelfranken': lion[0], 'Niederbayern': lion[1], 'Oberbayern': lion[2], 'Oberfranken': lion[3],
        'Oberpfalz': lion[4], 'Schwaben': lion[5], 'Unterfranken': lion[6]}

    wetterlink = {'Mittelfranken': link[0], 'Niederbayern': link[1], 'Oberbayern': link[2], 'Oberfranken': link[3],
        'Oberpfalz': link[4], 'Schwaben': link[5], 'Unterfranken': link[6]}


    #API-Weather

    city = request.args.get("openweather")

    if not city:
        city = "Bad Kissingen"

    api_weather = api.get_weather(city)

    return render_template("home.html", data=weather_data, main=bayern, link=wetterlink, API=api_weather)





#Nachrichten-Feed
@app.route("/Nachrichten")
def Nachrichten():

    artikel = br.get_news()

    return render_template("news.html", nachrichten=artikel)


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
