import requests
from tkinter import *
from tkinter import messagebox

#get API key from text file
api_key = open('WeatherApp Project/api_key.txt', 'r').read()
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

#Create a function to get the weather for a given city
def getweather(city):
    result = requests.get(url.format(city, api_key))
    print(result)

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        kelvin = json['main']['temp']
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        weather = json['weather'][0]['main']
        full_weather = [city, country, kelvin, 
                        celsius, fahrenheit, weather]
        
        return full_weather
    
    else:
        print("Weather not found")

#Create function to search for a city's weather information
def search():
    city = city_text.get()
    weather = getweather(city)

    if weather:
        location['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_celsius['text'] = str(float("%.2f"%weather[3]))+" Degrees Celsius"
        temperature_fahrenheit['text'] = str(float("%.2f"%weather[4]))+" Degrees Fahrenheit"
        weather_lbl['text'] = weather[5]

    else:
        messagebox.showerror('Error', "Can't find weather {}".format(city))


#creating the tkinter object
app = Tk()

#add the title
app.title("Sathya's Weather App")

#alter window size
app.geometry("750x750")

#add text
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

#create search button
search_button = Button(app, text="search for weather", width=12, command=search)
search_button.pack()

#create labels
location = Label(app, text="Location", font={'bold', 20})
location.pack()

temperature_celsius = Label(app, text="Temperature in Celsius")
temperature_fahrenheit = Label(app, text="Temperature in Fahrenheit")
temperature_celsius.pack()
temperature_fahrenheit.pack()

weather_lbl = Label(app, text="Weather")
weather_lbl.pack()

app.mainloop()