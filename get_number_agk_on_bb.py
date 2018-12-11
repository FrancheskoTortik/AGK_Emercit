import re
import requests


def number_agk_get(bb):
    # получаем файл с данными

    agk_list = requests.get('http://tech.emercit.com/state.html')

    # берем только строку, содержащуюю ББ
    for i in agk_list.text.split('onclick'):

        if re.findall(str(bb), i) != []: #находим строку. в которой есть номер ББ
            if re.findall('АГК',i):
                agk_number = re.findall(r'АГК-\d+', i) #присваиваем название в формате "АГК-...."
            elif re.findall('ЭМЕРСИТ', i):
                agk_number = re.findall(r'ЭМЕРСИТ-\d+\w*', i)
    return agk_number[0] #возвращаем строку - номер АГК
