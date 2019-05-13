#!/usr/local/bin/python3.6
import requests
from bs4 import BeautifulSoup
from modules.film_template import templates


def scrape_everyman(venues: list, timeconfig: dict=None):
    """
    INPUT: venues: list, timeconfig: dict
    ----------------------------------------------------------------------
    ----------------------------------------------------------------------
    venues     |  An array of everyman venues to scrape film times
    timeconfig |  A dict containing days of week with times in string format
               |  '0000-2359' to check against. If a day is missing this will
               |  return data for all times.


    OUTPUT: data -> dict
    ----------------------------------------------------------------------
    ----------------------------------------------------------------------
    data       |  A json representation of the film data

    """
    base = "https://www.everymancinema.com"
    data = {}
    for venue in venues:
        data[venue] = {}
        soup = BeautifulSoup(requests.get(f"{base}/{venue}").content, 'lxml')
        films = soup.find_all("li", {"class": "gridRow filmItem"})
        for f in films:
            title = f.find('a', {"class": "filmItemTitleLink"}).text
            link = "{}{}".format(base, f.find('a', {'data-book-button': True})['href'])
            data[venue][title] = {"title": title, "link": link, "times": {}}
            dates = f.find_all(attrs={"data-film-session": True})
            for date in dates:
                day = date.find(attrs={"class": "filmItemDate"}).text
                target_times = timeconfig.get(day.split(' ')[0].strip().title(), None)
                if target_times:
                    stime, etime = [int(i) for i in target_times.split('-')]
                data[venue][title]["times"][day] = []
                times = date.find_all("a", {"class": "filmTimeItem"})
                for t in times:
                    screen = t['data-screen']
                    booking_link = f"{base}{t['href']}"
                    time = t.text
                    itime = int(time.replace(':', ''))
                    if not target_times or (itime >= stime and itime <= etime):
                        data[venue][title]["times"][day].append({"screen": screen, "time": time, "booking_link": booking_link})
    return data


def generate_html(film_data: dict):
    """
    INPUT: film_data: dict
    ----------------------------------------------------------------------
    ----------------------------------------------------------------------
    film_data  |  A json / dict containing the everyman film data as
                  returned by the scrape_everman function

    OUTPUT: html -> str, data -> dict, plaintext -> str
    ----------------------------------------------------------------------
    ----------------------------------------------------------------------
    html       |  A string containing HTML data to use in an email
    plaintext  |  A plaintext version of the HTML to use in an email

    """
    html = templates['title']
    plaintext = ''
    for venue, movies in film_data.items():
        html += templates['venue'].format(' '.join([v.title() for v in venue.split('-')]))
        plaintext += ' '.join([v.title() for v in venue.split('-')])
        for title, info in movies.items():
            html += templates['film_info'].format(title, info['link'])
            plaintext += f"\n{title}\t{info['link']}"
            for date, times in info['times'].items():
                html += templates['date'].format(date)
                plaintext += f"\n{date}"
                for time in times:
                    html += templates['film_times'].format(time['booking_link'], time['time'], time['screen'])
                    plaintext += f"\n{time['time']} @ {time['screen']}:\t{time['booking_link']}"
                html += templates['end_times']
                plaintext += f"\n"
    return html, plaintext
