import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'typenamewhomfrom(noemailneeded)'
email['to'] = 'heretypeemailto '
email['subject'] = 'Kszybar'

email.set_content(html.substitute({'name': 'nameofperson'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('youremail', 'password')
	smtp.send_message(email)
	print('all good boss!')