import smtplib
import getpass
to =[]
user = input("Enter your EmailAddress :")
password = getpass.getpass("Enter your password : ")
msg = input("Please Enter The Matter : ")
to.append(input("Enter To address: "))
s = smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
print("Connecting to the server.....")
try:
    s.login(user,password)
    if(s.verify(user)):
        print("Successfully connected to Server...")
        s.sendmail(user,to,msg)
        s.quit()
        print("Mail have been sent successfully.....!")
except smtplib.SMTPAuthenticationError:
    print("Can not connected to the Server...!")




