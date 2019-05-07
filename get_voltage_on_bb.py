#Данная программа предназначена для получения последнего имеющегося значения напряжения и его даи и времени
import re
import requests
from datetime import datetime as dt
from datetime import timedelta
def voltage_get (bb):
    #делаем запрос лога
    agk = requests.get('http://emercit.com/tech3/log.php?bb=' + str(bb))
    last_voltage = '--.--'
    #проходим циклом по всем строкам полученного лога
    temp_info = re.findall(r'time\(\d\d\.\d\d\.\d\d\d\d \d\d:\d\d:\d\d\) volt\(main=\d\d\.\d\d;rl=\d\d\.\d\d\)', agk.text)
    last_time = dt.strptime(r'01.01.2019 00:00:00', r'%d.%m.%Y %H:%M:%S')
    for x in temp_info:
        date_tmp = dt.strptime(re.findall(r'\d\d\.\d\d\.\d\d\d\d', x)[0] + " " + re.findall(r'\d\d:\d\d:\d\d', x)[0], r'%d.%m.%Y %H:%M:%S')
        if date_tmp > last_time:
            last_time = date_tmp
            last_voltage = re.findall(r'\d\d\.\d\d', re.findall(r'main=\d\d\.\d\d', re.findall(r'volt\(main=\d\d\.\d\d;rl=\d\d\.\d\d', x)[0])[0])[0]


    return last_voltage

def date_voltage(bb):
    #делаем запрос лога
    agk = requests.get('http://emercit.com/tech3/log.php?bb=' + str(bb))
    date = 'no_data'
    time_volt = 'no_data'
    #проходим циклом по всем строкам полученного лога
    temp_info = re.findall(r'time\(\d\d\.\d\d\.\d\d\d\d \d\d:\d\d:\d\d\) volt\(main=\d\d\.\d\d;rl=\d\d\.\d\d\)',
                           agk.text)
    last_time = dt.strptime(r'01.01.2019 00:00:00', r'%d.%m.%Y %H:%M:%S')
    for x in temp_info:
        date_tmp = dt.strptime(re.findall(r'\d\d\.\d\d\.\d\d\d\d', x)[0] + " " + re.findall(r'\d\d:\d\d:\d\d', x)[0],
                               r'%d.%m.%Y %H:%M:%S')
        if date_tmp > last_time:
            last_time = date_tmp
    last_time += timedelta(hours=3)
    return last_time

