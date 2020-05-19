import os
import smtplib

def sent_gmail(user, password, send_to, subject=None, body=None):
   if isinstance(send_to, list):
      send_to = ', '.join(send_to)
   email_text = f'From: {user}\nTo: {send_to}\nSubject: {subject}\n\n{body}'

   try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      server.login(user, password)
      server.sendmail(user, send_to, email_text)
      server.close()
      return True, 'Success'
   except Exception as e:
      return False, str(e)

if __name__ == "__main__":
   user = os.environ['USER']
   password = os.environ['PASS']
   to = 'penut85420@gmail.com'
   result, reason = sent_gmail(user, password, to)

   print(result, reason)
