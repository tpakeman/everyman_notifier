#!/usr/local/bin/python3.6
from mail import send_html_mail
from everyman import scrape_everyman
import json


if __name__ == '__main__':
    CONFIG = 'demo_config.json'
    with open(CONFIG, 'r', encoding='UTF-8') as f:
        config = json.loads(f.read())
    venues = config['venues']
    recipients = config['recipients']
    creds = config['email']
    times = config['times']
    html, data, text = scrape_everyman(venues, times)
    send_html_mail(text,
                   html,
                   'Cinema times this week',
                   recipients,
                   'Python Mail',
                   'gmail',
                   creds)
