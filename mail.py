

import smtplib
from getpass import getpass

try:
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls()
	sender = 'k.abhinandhan15@gmail.com.com'
	reciever = 'knprajwalsai@gmail.com'
	message = "hii"
	password = getpass("enter password")
	s.login(sender, password)
	s.sendmail(sender, reciever, message)
except:
	print("some error")
else:
	print("sent succesfully")