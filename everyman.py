#!/usr/local/bin/python3.6
import requests
from bs4 import BeautifulSoup
from film_template import templates
from mail import send_html_mail
import json


def scrape_everyman(venues: list, timeconfig: dict=None):
    """
    INPUT: venues: list, timeconfig: dict
    ----------------------------------------------------------------------
    ----------------------------------------------------------------------
    venues     |  An array of everyman venues to scrape film times
    timeconfig |  A dict containing days of week with times in string format
               |  '0000-2359' to check against. If a day is missing this will
               |  return data for all times.


    OUTPUT: html -> str, data -> dict, plaintext -> str
    ----------------------------------------------------------------------
    ----------------------------------------------------------------------
    html       |  A string containing HTML data to use in an email
    data       |  A json representation of the film data
    plaintext  |  A plaintext version of the HTML to use in an email

    """
    base = "https://www.everymancinema.com"
    data = {}
    html = templates['title']
    plaintext = ''
    for venue in venues:
        data[venue] = {}
        html += templates['venue'].format(' '.join([v.title() for v in venue.split('-')]))
        plaintext += ' '.join([v.title() for v in venue.split('-')])
        soup = BeautifulSoup(requests.get(f"{base}/{venue}").content, 'lxml')
        films = soup.find_all("li", {"class": "gridRow filmItem"})
        for f in films:
            title = f.find('a', {"class": "filmItemTitleLink"}).text
            link = "{}{}".format(base, f.find('a', {'data-book-button': True})['href'])
            html += templates['film_info'].format(title, link)
            plaintext += f"\n{title}\t{link}"
            data[venue][title] = {"title": title, "link": link, "times": {}}
            dates = f.find_all(attrs={"data-film-session": True})
            for date in dates:
                day = date.find(attrs={"class": "filmItemDate"}).text
                target_times = timeconfig.get(day.split(' ')[0].strip().title(), None)
                if target_times:
                    stime, etime = [int(i) for i in target_times.split('-')]
                html += templates['date'].format(day)
                plaintext += f"\n{day}"
                data[venue][title]["times"][day] = []
                times = date.find_all("a", {"class": "filmTimeItem"})
                for t in times:
                    screen = t['data-screen']
                    booking_link = f"{base}{t['href']}"
                    time = t.text
                    itime = int(time.replace(':', ''))
                    if not target_times or (itime >= stime and itime <= etime):
                        html += templates['film_times'].format(booking_link, time, screen)
                        html == f"{time} @ {screen}:\t{booking_link}"
                        data[venue][title]["times"][day].append({"screen": screen, "time": time, "booking_link": booking_link})
                html += templates['end_times']
                plaintext += f"\n"
    return html, data, plaintext


if __name__ == '__main__':
    CONFIG = 'config.json'
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
