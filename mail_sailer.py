import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import result



email_list = ['4008@emercit.ru', 'd.shpak-dolzenko@emercit.ru', 'm.ovsienko@emercit.ru', 'adsd78@gmail.com', 'm.velichko@emercit.ru']

for x in email_list:
    msg = MIMEMultipart()
    addr_from = '8600999@gmail.com'
   # addr_to = email_list
    password = 'qwerty8600999'
    msg['From'] = addr_from
    msg['To'] = x
    msg['Subject'] = 'Напряжение АКБ'
    body ='Добрый день! Высылаю напряжение АКБ ниже 11,7В. \nВремя указано в GMT нужно прибавить 3 часа.'
    msg.attach(MIMEText(body,'plain'))
    html = result.html_data
    msg.attach(MIMEText(html,'html'))
    smpt_obj = smtplib.SMTP('smtp.gmail.com', 587)
    #smpt_obj.set_debuglevel(True)
    smpt_obj.ehlo()
    smpt_obj.starttls()
    smpt_obj.login('8600999@gmail.com', password)
    smpt_obj.send_message(msg)
    smpt_obj.quit()