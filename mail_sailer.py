import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import result


msg = MIMEMultipart()

addr_from = '8600999@gmail.com'
addr_to = '4008@emercit.ru'
password = 'qwerty8600999'
msg['From'] = addr_from
msg['To'] = addr_to
msg['Subject'] = 'Напряжение АКБ'
body =' \tДобрый день! Высылаю напряжение АКБ:'
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