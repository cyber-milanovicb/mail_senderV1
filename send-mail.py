import os
import smtplib
import ssl

email = "milanovicful@gmail.com" #changed
password = email_password = os.environ.get("EMAIL_PASSWORD") #changed
to = "milanovicful@gmail.com"

msg = """I am sorry for sending couple of mails, I was just testing out some other details like CC/ BCC if I can
somehow implement them as well. It "gets the variable and argument" but, it doesn't work....FOr Now. :)
Please award me with your and maybe one more FOLLOW at borismilanovic.medium.com . 
    
Thanks bro for being supportative, and NOW  - take a look at the watch - I am going to rest a bit.
    
Sincerest regards to you and all 3 princesses."""



server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(email, password)

server.sendmail(email , to , msg)

server.quit()
# Create system variable with your sixteen-digit code that you get once you turn on 2-step verification
#
# This PC -> Advanced System Settings -> click on Environment Variables, click on New
# Name it EMAIL_PASSWORD and put the six character code you've got once two-step authentication is ON
# And at https://myaccount.google.com/apppasswords you have generated six character key
# email_password = os.environ.get("EMAIL_PASSWORD") - this means that newly created environment value called
# "EMAIL_PASSWORD" contains the key generated at the https://myaccount.google.com/apppasswords
# where you have generated six character key



