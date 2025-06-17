import smtplib

hostname = "testdom"
from_addr = "some_addr@ukr.net"
to_addr = "student@testdom.my"
message = "smtp message"

server = smtplib.SMTP('192.168.0.76')
#print server.elho(hostname)
try:
    server.verify(to_addr)
    server.sendmail(from_addr, to_addr, message)
    print "Message is sent"
    server.quit()
except smtplib.SMTPRecipientsRefused:
    print 'Address of the destination is Not valid'