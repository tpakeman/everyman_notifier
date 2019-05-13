#### Summary
This contains a script that scrapes the everyman cinema website for film listings and emails recipients with a neat HTML list of the showings and times


#### Requirements
* Python 3.6+ with requests, beautiful soup (bs4), smtp and email libraries
* A configuration file in json with:
    * Venues to scrape
        * This should be an array of venues in lowercase and hyphen separated
            * e.g. ['maida-vale', 'kings-cross']
    * An array of email recipients 
    * Desired days and times
        * Format is {day_of_week: times, day_of_week: times...}
        * Write days in full e.g. "Monday" - "Sunday"
        * Use strings in format "0000-2359" for start-end
        * e.g. {"Monday": "1800-2200"} would mean show Monday films starting between 6 and 10pm
    * Credentials of an email account (gmail or hotmail) to use
        * Credentials should be inside a dictionary called 'email' with keys gmail_user and gmail_password or hotmail_user and hotmail_password


#### TO DO 
# Rotten tomatoes API to show user and critic scores
# Format the email in multiple columns
# Only show when movie is weekend or evening of a weekday
# Parse and clean venue input - remove spaces and lower case
    # Write a venue lookup function
# NICE TO HAVE
    # Authenticate and book within the email!