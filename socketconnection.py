import smtplib
from email.message import EmailMessage
from datetime import datetime
import socket

# Email configuration
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login('coderinfo123@gmail.com', 'replace yours')
vendor_email = 'coderinfo123@gmail.com'
user_email = 'mohannekkanti101@gmail.com'

# Email message setup
usubject = "Low Quantity of Stock - Sugar"
vsubject = "New Order Placed - Sugar"
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def send_email(content, email_receiver, subject):
    msg = EmailMessage()
    msg.set_content(content)
    msg['To'] = email_receiver
    msg['From'] = 'coderinfo123@gmail.com'
    msg['Subject'] = subject
    server.send_message(msg)

# Configure NodeMCU's Wi-Fi connection
NODEMCU_IP = '192.168.1.10'  # Adjust with your NodeMCU's IP address
NODEMCU_PORT = 12345  # Choose a suitable port

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the NodeMCU's IP and port
sock.bind((NODEMCU_IP, NODEMCU_PORT))

# Listen for incoming connections
sock.listen(1)

# Accept connection from NodeMCU
client_socket, client_address = sock.accept()
print("NodeMCU connected:", client_address)

while True:
    # Receive data from NodeMCU
    data = client_socket.recv(1024).decode().strip()
    height = abs(float(data))
    mass = height
    print("Current Stock Quantity:", height)

    # Compose email content
    user_content = f"Sugar is low in quantity.\nRemaining quantity: {mass} grams\nRequired quantity: 1000 grams\nOrder placed to vendor."
    vendor_content = f"Stock Name: Sugar\nRequired quantity: 1000 grams\nOrder placed at {current_time}."

    # Send email notifications if stock quantity is low
    if height <= 59:
        send_email(user_content, user_email, usubject)
        send_email(vendor_content, vendor_email, vsubject)

# Close the socket connection and server connection
client_socket.close()
server.quit()
