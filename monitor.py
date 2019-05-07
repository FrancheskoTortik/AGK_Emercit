import time
import requests
import re
from datetime import  datetime as dt
import get_number_agk_on_bb
import get_region_on_bb
import get_bb_number
import get_voltage_on_bb
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

temp = ''
chek = 0
url = 'http://tech.emercit.com/state.html'
r = requests.get(url)
filter_agk = re.findall(r'АГК-\d\d\d\d', requests.get(url).text)[:-15] + ['ЭМЕРСИТ-0228']

def check_registration(bb_number):
    flag = False
    url = 'http://tech.emercit.com/state.html'
    info = requests.get(url).text.split('onclick')
    for x in info:
        if bb_number in x:
            time_reg = dt.strptime(re.findall(r'\d\d\.\d\d\.\d\d\d\d \d\d:\d\d:\d\d',x)[0], r'%d.%m.%Y %H:%M:%S')
    now = dt.now()
    delta = now - time_reg
    if delta.seconds//3600 < 2:
        flag = True
    return flag

def time_registration(bb_number):

    url = 'http://tech.emercit.com/state.html'
    info = requests.get(url).text.split('onclick')
    for x in info:
        if bb_number in x:
            time_reg = dt.strptime(re.findall(r'\d\d\.\d\d\.\d\d\d\d \d\d:\d\d:\d\d',x)[0], r'%d.%m.%Y %H:%M:%S')

    return time_reg

def info_reg():
    temp = ''
    for x in get_bb_number.number_bb_get():
        if check_registration(x):
            continue
        else:
            if get_number_agk_on_bb.number_agk_get(x) in filter_agk:
                temp+= '<tr><td>' + str(get_number_agk_on_bb.number_agk_get(x))+ '</td><td>' + dt.strftime(time_registration(x), r'%d.%m.%Y %H:%M:%S') + '</td><td>' +  dt.strftime(get_voltage_on_bb.date_voltage(x), r'%d.%m.%Y %H:%M:%S') + '</td><td>' +  str(get_voltage_on_bb.voltage_get(x))+ '</td></tr>'


    return temp




html_data_monitor = """
<!DOCTYPE HTML>
<html>
<style>
  table{
    margin: 50px 0;
    text-align: left;
    border-collapse: separate;
    border: 1px solid #ddd;
    border-spacing: 10px;
    border-radius: 3px;
    background: #fdfdfd;
    font-size: 14px;
    width: auto;
  }
  td,th{
    border: 1px solid #ddd;
    padding: 5px;
    border-radius: 3px;
  }
  th{
    background: #E4E4E4;
  }
  caption{
    font-style: italic;
    text-align: right;
    color: #547901;
  }
</style>
<body>
<h3>Добрый день! Информация по регистрации АГК на сервере tech.emercit.com.""" + dt.strftime(dt.now(), r'%d.%m.%Y %H:%M:%S') +"</h3><table><tr>  <th>Часов не выходил на связь</th>  <th>Номер АГК</th>  <th>Район</th><th>Дата последнего выхода</th></tr>"

html_data_monitor += temp + "</table></body></html>"

#d = open('1.txt', 'w', encoding='utf-8')
#d.write(html_data)
#d.close()
i=1
while True:
    info_reg()
    print(temp)
    html_data_monitor1= """
    <!DOCTYPE HTML>
    <html>
    <style>
      table{
        margin: 50px 0;
        text-align: left;
        border-collapse: separate;
        border: 1px solid #ddd;
        border-spacing: 10px;
        border-radius: 3px;
        background: #fdfdfd;
        font-size: 14px;
        width: auto;
      }
      td,th{
        border: 1px solid #ddd;
        padding: 5px;
        border-radius: 3px;
      }
      th{
        background: #E4E4E4;
      }
      caption{
        font-style: italic;
        text-align: right;
        color: #547901;
      }
    </style>
    <body>
    <h3>Добрый день! Информация по регистрации АГК на сервере tech.emercit.com. по состоянию на 
     """
    html_data_monitor2 = dt.strftime(dt.now(),r'%d.%m.%Y %H:%M:%S')
    html_data_monitor3 = """</h3><table><tr><th>Номер АГК</th><th>дата последнего выхода</th><th>Дата последнего измерения напряжения</th><th>Последнее измеренное напряжение</th></tr>"""


    html_data_monitor = html_data_monitor1 + html_data_monitor2 + html_data_monitor3 + info_reg() + "</table></body></html>"

    info_reg()

    email_list = ['4008@emercit.ru']
    for x in email_list:
        msg = MIMEMultipart()
        addr_from = '8600999@gmail.com'
       # addr_to = email_list
        password = 'qwerty8600999'
        msg['From'] = addr_from
        msg['To'] = x
        msg['Subject'] = 'Напряжение АКБ'
        #body ='Добрый день!  \nВремя указано в GMT нужно прибавить 3 часа.'
        #msg.attach(MIMEText(body,'plain'))
        html = html_data_monitor
        msg.attach(MIMEText(html,'html'))
        smpt_obj = smtplib.SMTP('smtp.gmail.com', 587)
        #smpt_obj.set_debuglevel(True)
        smpt_obj.ehlo()
        smpt_obj.starttls()
        smpt_obj.login('8600999@gmail.com', password)
        smpt_obj.send_message(msg)
        smpt_obj.quit()
    print('Сессия №{} закончена'.format(i))
    i += 1
    time.sleep(3600)