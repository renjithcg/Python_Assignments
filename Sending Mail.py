import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.login("username","password")
msg = "Hello This is a test message"
s.sendmail("fromaddress","toaddress",msg)
