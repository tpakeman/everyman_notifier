#!/usr/local/bin/python3.6
from modules.mail import send_html_mail
from modules import everyman
import json
from os import path


if __name__ == '__main__':
    CONFIG = path.join('config', 'config.json')
    with open(CONFIG, 'r', encoding='UTF-8') as f:
        config = json.loads(f.read())
    venues = config['venues']
    recipients = config['recipients']
    creds = config['email']
    times = config['times']
    data = everyman.scrape_everyman(venues, times)
    html, text = everyman.generate_html(data)
    send_html_mail(text,
                   html,
                   'Cinema times this week',
                   recipients,
                   'Python Mail',
                   'gmail',
                   creds)
