# -------------------------------------------------------------------------- #
# -------------------------------------------------------------------------- #
#### This contains a simple HTML template to format the listings data for ####
#### use in an email. Each component is a string which takes arguments.   ####
#### Each component is saved into a dictionary for importing into the     ####
#### scraping script.                                                     ####
# -------------------------------------------------------------------------- #
# -------------------------------------------------------------------------- #

# The title. One per email, doesn't change
title = """<h1><strong>Everyman Cinema</strong></h1>
<h3><span style="font-weight: 400;">Showtimes this week</span></h3>"""

# The venue name, one per venue
venue = """<p>&nbsp;</p>
<hr />
<h2><span style="color: #333399;"><strong>{}</strong></span></h2>"""

# The film title and booking_link, one per film per venue
film_info = """<h3><strong>{0}</strong></h3>
<p>| <a href="{1}"><span style="font-weight: 400;">Film info</span></a>
<span style="font-weight: 400;"> | </span>
<a href="https://www.google.com/search?q=rottentomatoes.com+{0}&amp;btnI">
<span style="font-weight: 400;">Rotten tomatoes</span></a>&nbsp;|</p>"""

# A date, one per day per film per venue
date = """<h4><em><span style="font-weight: 400;">{}</span></em></h4>
<ul>"""

# A list of film times for a given day, plus screen info and booking links
# Many per day per film per venue 
film_times = """
<li><a href="{}"><span style="font-weight: 400;">{} - {}</span></a></li>
"""
# Call this once after each day to close the list of film times
end_times = """
</ul>"""

# A dictionary for convenient importing
templates = {"title": title,
             "venue": venue,
             "film_info": film_info,
             "date": date,
             "film_times": film_times,
             "end_times": end_times}
