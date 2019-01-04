# -*- coding: UTF-8 -*-

from weather import Weather, Unit
# Lookup WOEID via http://weather.yahoo.com.
# get weather information
def yahoo_weather(loca, nb_days):
    weather = Weather(unit=Unit.CELSIUS)
    # Lookup via location name.
    location = weather.lookup_by_location(loca)
    condition = location.condition()
    # print(condition.text())

    # Get weather forecasts for the upcoming days.

    forecasts = location.forecast()
    forecastdays = nb_days

    SUBJECT = loca+' weather forecast in the next '+str(forecastdays-1)+' days.'

    msg = [str] * forecastdays
    for i in range(forecastdays):
        if i>0:
            condit = forecasts[i].text()
            dateN = forecasts[i].date()
            Th = forecasts[i].high()
            Tl = forecasts[i].low()
            test = (
            '<h2>'+dateN+' is '+ condit+'</h2>'
            '<p> High temperature: '+Th+' &deg; C </p>'
            '<p> Low temperature: '+Tl+' &deg; C </p>'
                )
            msg[i-1] = test
            # print(test)
    msg = str(msg)
    msg = msg[2:len(msg)-1]
    TEXT = msg.replace("', '", "\n\r")
    body = TEXT[:len(TEXT)-16]
    return body


