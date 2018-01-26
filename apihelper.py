#Import Libraries
import json
import urllib2
import urllib

#API-URL
api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8b55a9ee343dcbbe22412e4aef9c9a12'


class API_Weather():



    def get_weather(self,query):

        query = urllib.quote(query)
        url = api_url.format(query)
        data = urllib2.urlopen(url).read()
        parsed = json.loads(data)


        if parsed.get("weather"):

            weather = {"description": parsed["weather"][0]["description"],
                "temperature": parsed["main"]["temp"],
                "city": parsed["name"]
                }

        return weather


#celcius = API_Weather()

#sw = celcius.get_weather('London')

#print sw


