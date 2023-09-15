import email.contentmanager
import smtplib
from string import Template
from pathlib import Path
from email.message import EmailMessage

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Vishal V Bangrae'
email['to'] = 'ushahpv@gmail.com'
email['subject'] = 'HIHI'

email.set_content(html.substitute({'name': 'Usha'}), 'html')

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.login('vishalvbangrae@gmail.com', 'zwyfwojytxzifofs')
    smtp.send_message(email)
    print('done')