from flask import Flask,request,render_template
import requests
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()

app=Flask(__name__,template_folder='template')
API_KEY=os.environ.get('API_KEY')

@app.route('/', methods=["GET","POST"])
def show_weather():
    today_date=date.today().strftime("%a,%d %B")
    Weather_data = ''
    Error = 0
    City_name = ''
    weather=''
    tempreture=''
    feels_like=''
    if request.method=="POST":
        City_name=request.form.get("City_name")
        if City_name:
            API_Key=API_KEY
            City_name=request.form.get('City_name')
            url='https://api.openweathermap.org/data/2.5/weather?q='+City_name+'&APPID='+ API_Key
            data=requests.get(url)
            Weather_data=data.json()
            list_weather= Weather_data['weather']
            for i in list_weather:
                  for j,k in i.items():
                   if j=='description':
                     weather=k
            tempreture=round((Weather_data['main']['temp']- 273.15))
            feels_like=round((Weather_data['main']['feels_like']- 273.15))
        else:
            Error=1   
    return render_template('weather.html',today_date=today_date,data=Weather_data,City_name=City_name,Error=Error,weather=weather,tempreture=tempreture,feels_like=feels_like)
    

if __name__ =='__main__':
    app.run(debug=True)

