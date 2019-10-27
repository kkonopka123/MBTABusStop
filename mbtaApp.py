import requests
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import subprocess
import tkinter

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
window.attributes("-fullscreen", True) 

### Scheduler init
scheduler = BackgroundScheduler()


def destroyElements():
    for child in window.winfo_children():
        child.destroy()

def updateTime():
    destroyElements()
    print("Trigger Update")
    response = requests.get('https://api-v3.mbta.com/predictions?filter%5Bdirection_id%5D=1&filter%5Broute_type%5D=3&filter%5Bstop%5D=1270&filter%5Broute%5D=65').json()
    now = datetime.now()
    bus = "Bus: 65"
    nowFormated = now.strftime("Today is %A, %B %d %S")
    tkinter.Label(window, text = bus).pack()
    tkinter.Label(window, text = nowFormated).pack()
    for a in response['data']:
        arrival_time = datetime.strptime(a['attributes']['arrival_time'][:-6],"%Y-%m-%dT%H:%M:%S")
        deltaTime = str(arrival_time - now)
        leftDateTime = datetime.strptime(deltaTime,'%H:%M:%S.%f')
        leftTime = leftDateTime.strftime("%H:%M:%S")
        print("WTF" + leftTime)
        tkinter.Label(window, text = leftTime)
    

def turnOnScreen(): 
    scheduler.add_job(updateTime, "interval", minutes=1, id="refreshData")
    print("turnOnScreen")
    subprocess.call(['xset','dpms','force','on'])
    window.update()
    window.deiconify()
    ##add job
    ##open screen

def turnOffScreen():
    scheduler.remove_job('refreshData')
    print("turnOffScreen")
    subprocess.call(['xset','dpms','force','off'])
    window.withdraw()

    ##remove job
    ##remove screen
    #status = subprocess.check_output(['xset','-q']).decode('UTF-8').strip() ###allows to pull the current status of the screen
#xset dpms force off:

##initiate scheduler jobs
scheduler.add_job(turnOnScreen, "cron", day_of_week="mon-fri", hour=6, minute=30)
scheduler.add_job(turnOffScreen, "cron", day_of_week="mon-fri", hour=9, minute=0)
# scheduler.add_job(turnOnScreen, "interval", seconds=25)
# scheduler.add_job(turnOffScreen, "interval", seconds=60)
scheduler.start()




# pack is used to show the object in the window
window.mainloop()
