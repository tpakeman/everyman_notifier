import smtplib
from email.mime.text import MIMEText


def send_mail(message,
              subject,
              recipients,
              from_text,
              service, # hotmail  or gmail
              creds):
    if service == 'gmail':
        service_address = 'smtp.gmail.com:587'
    elif service == 'hotmail':
        service_address = 'smtp.live.com:587'
    else:
        raise ValueError("Only gmail or hotmail are accepted email providers.")
    with smtplib.SMTP(service_address) as server:
        if service == 'gmail':
            un = creds['gmail_user']
            pw = creds['gmail_password']
        elif service == 'hotmail':
            un = creds['hotmail_user']
            pw = creds['hotmail_password']
        server.starttls()
        server.login(un, pw)
        if not isinstance(recipients, list):
            recipients = [recipients]
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = from_text
        for r in recipients:
            msg['To'] = r
            server.sendmail(un, r, msg.as_string())
            "Successfully sent mail to {}".format(r)


def send_html_mail(message_text,
                   message_html,
                   subject,
                   recipients,
                   from_text,
                   service, # hotmail or gmail
                   creds):
    from email.mime.multipart import MIMEMultipart
    if service == 'gmail':
        service_address = 'smtp.gmail.com:587'
    elif service == 'hotmail':
        service_address = 'smtp.live.com:587'
    else:
        raise ValueError("Only gmail or hotmail are accepted email providers.")
    with smtplib.SMTP(service_address) as server:
        if service == 'gmail':
            un = creds['gmail_user']
            pw = creds['gmail_password']
        elif service == 'hotmail':
            un = creds['hotmail_user']
            pw = creds['hotmail_password']
        server.starttls()
        server.login(un, pw)
        if not isinstance(recipients, list):
            recipients = [recipients]
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = from_text
        part1 = MIMEText(message_text, 'plain')
        part2 = MIMEText(message_html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        for r in recipients:
            msg['To'] = r
            server.sendmail(un, r, msg.as_string())
            print("Successfully sent mail to {}".format(r))
