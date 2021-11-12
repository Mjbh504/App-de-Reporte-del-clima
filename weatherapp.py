import tkinter as tk
from typing import Text
import requests
import time

def getweather(canvas):
    ciudad=textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+ciudad+"&appid=5a7c7e5cfc0d9415ea07ba399ae98ac6"

    datosclima=requests.get(api).json()
    condicion=datosclima['weather'][0]['main']
    temperatura=int(datosclima['main']['temp']-273.15)
    maxtemp=int(datosclima['main']['temp_max']-273.15)
    mintemp=int(datosclima['main']['temp_min']-273.15)
    presion=datosclima['main']['pressure']
    humedad=datosclima['main']['humidity']
    viento=datosclima['wind']['speed']
    amancer=time.strftime('%I:%M:%S', time.gmtime(datosclima['sys']['sunrise']+21600))
    atardecer=time.strftime('%I:%M:%S', time.gmtime(datosclima['sys']['sunset']+21600))

    informefinal=condicion+"\n"+str(temperatura)+"°C"

    infofinal = condicion + "\n" + str(temperatura) + "°C" 
    datofinal = "\n"+ "Min Temp: " + str(mintemp) + "°C" + "\n" + "Max Temp: " + str(maxtemp) + "°C" +"\n" + "Pressure: " + str(presion) + "\n" +"Humidity: " + str(humedad) + "\n" +"Wind Speed: " + str(viento) + "\n" + "Sunrise: " + amancer + "\n" + "Sunset: " + atardecer
    lab1.config(text = infofinal)
    lab2.config(text = datofinal)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("app del clima")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield=tk.Entry(canvas, justify='center', width = 20, font = t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind('<Return>', getweather)


lab1=tk.Label(canvas, font=t)
lab1.pack()
lab2=tk.Label(canvas, font=t)
lab2.pack()
canvas.mainloop()
