import requests
from flask import render_template
from datetime import datetime
from app import app

@app.route('/')
def index():
    response = requests.get('https://api-v3.mbta.com/predictions?filter%5Bdirection_id%5D=1&filter%5Broute_type%5D=3&filter%5Bstop%5D=1270&filter%5Broute%5D=65').json()
    print(response)
    arrivals = []
    now = datetime.now()
    bus = "65"
    nowFormated = now.strftime("Today is %A, %B %d")
    for a in response['data']:
        arrival_time = datetime.strptime(a['attributes']['arrival_time'][:-6],"%Y-%m-%dT%H:%M:%S")
        deltaTime = str(arrival_time - now)
        leftDateTime = datetime.strptime(deltaTime,'%H:%M:%S.%f')
        arrivals.append(leftDateTime.strftime("%H:%M:%S"))
    
    return render_template("index.html",arrivals=arrivals, bus=bus, date=nowFormated)