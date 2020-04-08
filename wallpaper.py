import schedule
import os
import time
import datetime

def job(t):
    os.system("`gsettings set org.gnome.desktop.background picture-uri 'file:///home/dell/project/wallpapers/images/team{}.jpg'`".format(t))



x = datetime.datetime.now()
y=x.strftime("%d")
schedule.every().day.at("22:08").do(job,y)
while True:
    schedule.run_pending()
    time.sleep(10) 