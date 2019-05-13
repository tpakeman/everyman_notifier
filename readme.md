## Summary
#### This contains a script that scrapes the everyman cinema website for film listings and emails recipients with a neat HTML list of the showings and times
* everyman.py contains the functions to scrape the site and return data and html to use in an email
    * _NB currently the function returns the data and the formatted html together - in the future these will be separated_
* mail.py contains a function to send an html formatted email from gmail or hotmail
* main.py contains the main script to combine and run the functions
* config.json contains a configuration file in json with:
    * Venues to scrape
        * This should be an array of venues in lowercase and hyphen separated
            * e.g. ['maida-vale', 'kings-cross']
    * An array of email recipients to receive the email
    * Desired days and times
        * Format is {day_of_week: times, day_of_week: times...}
        * Write days in full e.g. "Monday" - "Sunday"
        * Use strings in format "0000-2359" for start-end
        * e.g. {"Monday": "1800-2200"} would mean show Monday films starting between 6 and 10pm
    * Credentials of an email account (gmail or hotmail) to use
        * Credentials should be inside a dictionary called 'email' with keys gmail_user and gmail_password or hotmail_user and hotmail_password
* _NB a demo_config.json is included in the right format, but the actual config.json has been added to .gitignore for security_


## How to run
* Create the config file with the recipients, venues, email recipients and desired times (optional)
* Amend main.py if desired to adjust location of config file, any email parameters and location of python installation on first line
* Make the script executable using `chmod +x 'path/to/file'`
* Add to crontab using `crontab -e` to trigger on a regular basis

## Requirements
* Python 3.6+
* requests, beautiful soup (bs4) with lxml parser, smtp and email libraries 


## TO DO 
* Fix issue of no matching times on a given day
* Separate scraping and html / text formatting functions
* Rotten tomatoes API to show user and critic scores
* Improve email formatting, e.g. multiple columns
* Make configuration easier - add argparser to make it CLI compatible
* Parse and clean venue input - remove spaces and lower case
    * Write a venue lookup function
* NICE TO HAVE
    * Authenticate and book within the email!