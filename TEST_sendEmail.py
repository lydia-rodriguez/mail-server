import smtplib

FROMADDR1 = "lydiaTEST@fsgi.com"
TOADDRS1  = ["lydia.rodriguez@fsgi.com"]
SUBJECT1  = "More Testing"

LOGIN    = FROMADDR1
PASSWORD = ""

msg1 = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR1, ", ".join(TOADDRS1), SUBJECT1) )
msg1 += "test text\r\n"


FROMADDR2 = "alarms@spectracell.com"
TOADDRS2  = ["lydia.rodriguez@fsgi.com"]
SUBJECT2  = "More Testing"

LOGIN    = FROMADDR2
PASSWORD = ""

msg2 = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR2, ", ".join(TOADDRS2), SUBJECT2) )
msg2 += "test text\r\n"


FROMADDR3 = "test@gmail.com"
TOADDRS3  = ["lydia.rodriguez@fsgi.com"]

SUBJECT3  = "More Testing"
LOGIN    = FROMADDR3
PASSWORD = ""

msg3 = ("From: %s\r\nTo: %s\r\nSubject: %s\r\n\r\n"
       % (FROMADDR3, ", ".join(TOADDRS3), SUBJECT3) )
msg3 += "test text\r\n"



server = smtplib.SMTP('130.211.148.85', 8888)
server.set_debuglevel(1)
server.ehlo()
# server.starttls()
# server.login(LOGIN, PASSWORD)
server.sendmail(FROMADDR1, TOADDRS1, msg1)
server.sendmail(FROMADDR2, TOADDRS2, msg2)
server.sendmail(FROMADDR3, TOADDRS3, msg3)
server.quit()
