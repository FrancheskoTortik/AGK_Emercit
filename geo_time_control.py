import re
import requests
import get_bb_number
import get_number_agk_on_bb

test_bbb = '3012BB000190'

def geo_time_control(bb_number):
    """
    Функция принимает на вход номер ББ и проверяет, есть ли в Логах недостоверные данные
     или время.
    """
    url = 'http://emercit.com/tech3/log.php?bb=' + bb_number
    data = requests.get(url).text.split('\n')
    not_rell_count = 0
    for x in data:
        if 'not rel' in x and 'level' in x:
            not_rell_count +=1


    report = "{} Недостоверные координаты {} раз за последний ЛОГ".format(get_number_agk_on_bb.number_agk_get(bb_number), not_rell_count)
    if not_rell_count !=0:
        print(report)


for x in get_bb_number.number_bb_get():
    geo_time_control(x)