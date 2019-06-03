import requests
import re
from datetime import datetime as dt
from datetime import date
import get_bb_number
import get_number_agk_on_bb



bb_list = get_bb_number.number_bb_get()

def door_control(date, bb_number):
    """
    Функция принимает на вход дату и номер биглбона и возвращает количество срабатываний по дверям
    """
    #Начальные данные
    url = 'http://emercit.com/tech3/log.php?bb=' + bb_number
    data = requests.get(url).text.split('\n') #скачиваем ЛОГ и записываем его в список, где каждая строка - строка ЛОГа
    alert_count = 0
    date_control = dt.strftime(date, "%d.%m.%Y")
    
    #определяем текущий статус дверцы и записываем его в переменную door_status
    for x in data:
        if re.findall(date_control, x) != [] and re.findall(r'door1',x) != []:
            door_staus = x.split('door1=')[1].split(';')[0]
            
            break
            
    for x in data:
        
        if re.findall(date_control, x) != [] and re.findall(r'door1',x) != []:
            #print(x)
            door_check = x.split('door1=')[1].split(';')[0]
            if door_check != door_staus:
                alert_count +=1 
                door_staus = door_check
            
    try:
        if alert_count != 0:
            str_report = "{} За {} произошло {} срабатываний по дверям! Текущий статус двери: {}".format(get_number_agk_on_bb.number_agk_get(bb_number), date_control, alert_count, door_staus)
            print(str_report)
    except:
        print('{} Что то пошло не так'.format(get_number_agk_on_bb.number_agk_get(bb_number)))
today = dt.now().date()   
yesterday = date(2019,6,1)



def door_control_lite(bb_number):
    url = 'http://emercit.com/tech3/log.php?bb=' + bb_number
    data = requests.get(url).text.split('\n')  # скачиваем ЛОГ и записываем его в список, где каждая строка - строка ЛОГа
    alert_count = 0

    # определяем текущий статус дверцы и записываем его в переменную door_status
    for x in data:
        if re.findall(r'door1', x) != []:
            door_staus = x.split('door1=')[1].split(';')[0]
            break
    for x in data:

        if re.findall(r'door1', x) != []:
            # print(x)
            door_check = x.split('door1=')[1].split(';')[0]
            if door_check != door_staus:
                alert_count += 1
                door_staus = door_check
    try:
        if alert_count != 0:
            str_report = "{} произошло {} срабатываний по дверям! Текущий статус двери: {}".format(get_number_agk_on_bb.number_agk_get(bb_number),alert_count, door_staus)
            print(str_report)
    except:
        print('{} Что то пошло не так'.format(get_number_agk_on_bb.number_agk_get(bb_number)))

for x in bb_list:
    door_control_lite(x)
