import get_number_agk_on_bb
import get_bb_number
import get_voltage_on_bb
import get_region_on_bb

result_info = []

for x in get_bb_number.number_bb_get():
    result_info_tmp = []
    try:
        if float(get_voltage_on_bb.voltage_get(str(x))) < 11.70: #если есть значение напряжения, то сравниваем с 11,7 В
            result_info_tmp.append(get_region_on_bb.find_region(str(x))) #добавляем район
            result_info_tmp.append(get_number_agk_on_bb.number_agk_get(str(x))) #добавляем номер АГК
            result_info_tmp.append(get_voltage_on_bb.voltage_get(str(x))) #добавляем напряжение
            result_info_tmp.append(get_voltage_on_bb.date_voltage(str(x))[0]) #добаляем дату измерения
            result_info_tmp.append(get_voltage_on_bb.date_voltage(str(x))[1]) #добавляем время измерения
            result_info.append(result_info_tmp) # добавляем список [Район, Номер АГК, Напряжение, дата, время] в результирующий список
        else:
            continue
    except:
        result_info_tmp.append(get_region_on_bb.find_region(str(x)))  # добавляем район
        result_info_tmp.append(get_number_agk_on_bb.number_agk_get(str(x)))  # добавляем номер АГК
        result_info_tmp.append(get_voltage_on_bb.voltage_get(str(x)))  # добавляем напряжение
        result_info_tmp.append(get_voltage_on_bb.date_voltage(str(x))[0])  # добаляем дату измерения
        result_info_tmp.append(get_voltage_on_bb.date_voltage(str(x))[1])  # добавляем время измерения
        result_info.append(result_info_tmp)  # добавляем список [Район, Номер АГК, Напряжение, дата, время] в результирующий список

result_info.sort()
temp = ''
for x in result_info:
    if str(x[0]) != "Неизвестно":
        temp +=  '<tr><td>' + str(x[0]) + '</td><td>' + str(x[1]) + '</td><td>' + str(x[2]) + '</td><td>' + str(x[3]) + '</td><td>' + str(x[4]) + '</td></tr>'




html_data = """
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
<table>
<tr>
  <th>Район</th>
  <th>Номер АГК</th>
  <th>Напряжение</th>
  <th>Дата измерения</th>
  <th>Время измерения</th>
  </tr>
"""
html_data += temp + "</table></body></html>"

d = open('1.txt', 'w', encoding='utf-8')
d.write(html_data)
d.close()
