# -*- coding: UTF-8 -*-
import better_exceptions

from WeatherAPI import yahoo_weather
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

import better_exceptions
import Sendmail
from Sendmail import Gmail

#####################################

loca = 'Paris'
nbr_days = 5
mail_subject = loca+' weather forecast in the next '+str(nbr_days)+' days.'
mail_body = yahoo_weather(loca, nbr_days)

# Send weather information by gamil
gmail_sender ='zhaolu.715@gmail.com'
gmail_passwd ='vklu51it'
mail_to = ['azhaoalu@hotmail.com', 'laila@berberos.com ']
# Send mail during the work days and the time
wk_days = '1-5'
time_h = '10'
time_m = '05'


def job():
    try:
        gm = Gmail(gmail_sender, gmail_passwd)
        gm.send_message(mail_to, mail_subject, mail_body)
        print('sucesseful')
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) 
    except:
       print('failed')
# Using APScheduler module
# BlockingScheduler
scheduler = BlockingScheduler()
scheduler.add_job(job, 'cron', day_of_week=wk_days, hour=time_h, minute=time_m)
scheduler.start()