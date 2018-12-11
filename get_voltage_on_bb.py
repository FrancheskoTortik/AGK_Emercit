#Данная программа предназначена для получения последнего имеющегося значения напряжения и его даи и времени
import re
import requests

def voltage_get (bb):
    #делаем запрос лога
    agk = requests.get('http://emercit.com/tech3/log.php?bb=' + str(bb))
    voltage = '--.--'
    #проходим циклом по всем строкам полученного лога
    for i in agk.text.split('geo'):
        #print(i)
        #выбираем только строки, содержащие значение напряжения
        voltage_level_str = re.findall(r'volt', i)
        if voltage_level_str != []:

            volt = re.findall(r'main=\d+\.\d+', i)
            volt_tmp = volt[0].split('=')[1]
            voltage = str(volt_tmp)
    return voltage

def date_voltage(bb):
    #делаем запрос лога
    agk = requests.get('http://emercit.com/tech3/log.php?bb=' + str(bb))
    date = 'no_data'
    time_volt = 'no_data'
    #проходим циклом по всем строкам полученного лога
    for i in agk.text.split('geo'):

        #выбираем только строки, содержащие значение напряжения
        voltage_level_str = re.findall(r'volt', i)
        if voltage_level_str != []:

            date_tmp = re.findall(r'time\(\d\d\.\d\d\.\d\d\d\d\s\d\d:\d\d:\d\d', i)
            date_tmp2 = date_tmp[0].split('(')
            date = date_tmp2[1].split()[0]
            time_volt = date_tmp2[1].split()[1]# date_voltage(bb)[0] - дата измерения, date_voltage(bb)[1] - время измерения
    return date, time_volt
