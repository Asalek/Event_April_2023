#Asalek123%%
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE
from email import encoders

# SMTP server details
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "asalekasalek8599@gmail.com"
smtp_password = "owduivkmwrktfusy"

# Email details
reciever = input("Enter reciever Email : ")
to = [reciever]
from_addr = smtp_username
subject = "Email with attachment"
body = "Please find attached the requested document."
file_path = "./file.txt"

# Create a multipart message object and add email contents
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = COMMASPACE.join(to)
msg['Subject'] = subject
msg.attach(MIMEText(body, 'plain'))

# Add attachment to the email
with open(file_path, "rb") as attachment:
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {file_path}")
    msg.attach(part)

# Connect to SMTP server and send email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.sendmail(from_addr, to, msg.as_string())
