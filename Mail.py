import smtplib
s= smtplib.SMTP("smtp.gmail.com",587)
s.ehlo()
s.starttls()
s.login(input("Enter The UserName : "),input("Enter The Password : "))
msg = input("Enter The Matter ; ")
s.sendmail(input("Enter the From Address : "),input("Enter The To Address : "),msg)
