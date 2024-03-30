import serial
arduino =serial.Serial('COM7',9600)
import smtplib
from email.message import EmailMessage
from datetime import datetime
now=datetime.now()
current_time=now.strftime("%H:%M:%S")
server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('coderinfo123@gmail.com','replace yours')
msg=EmailMessage()
usub="low quantity of stock"
vsub = "orders placed by user"
vendor='coderinfo123@gmail.com'
user='mohannekkanti101@gmail.com'
def sendmail(content,emailreciver,subject,emailsender):
 msg = EmailMessage()
 msg.set_content(content)
 msg["To"]=emailreciver
 msg['from']=emailsender
 msg['Subject']=subject
 server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
 server.login('coderinfo123@gmail.com', 'bnnbtzjuznnmpyvq')
 server.send_message(msg)
while True:
    height=abs(float(arduino.readline().decode().strip()))
    mass =height
    print(height)
    ucontent = "sugar is low quantity\n Reaming quantity:-" + str(mass)+"grams\nRequired quantity:-"+str(1000)+'grams\nOrder placed to vendor'
    vcontent ="Stockname:-sugar\nRequired quantity:-"+str(1000)+'grams\nOrder placed at '+current_time+""
    print(ucontent,vcontent)
    if height<=59:
        sendmail(ucontent,user,usub,vendor)
        sendmail(vcontent,vendor,vsub, vendor)

    quit()




