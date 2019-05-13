## Summary
#### This contains a script that scrapes the everyman cinema website for film listings and emails recipients with a neat HTML list of the showings and times
* `main.py` contains the main script to combine and run the functions contained in `/modules`
* `/modules`:
   * `everyman.py` contains a function to scrape and return data and a function to compose html to use in an email
   * `mail.py` contains a function to send an html formatted email from gmail or hotmail
   * `film_template.py` contains strings containing html which are used in the everyman.py script to create the email body
   * `/config`:
     * _NB a demo_config.json is included in the right format, but the actual config.json has been added to .gitignore for security_
      * `config.json` should contain a configuration file in json with:
         * An array of venues to scrape in lowercase and hyphen separated
            * e.g. `['maida-vale', 'kings-cross']`
         * An array of email recipients to receive the email
            * e.g. `['me@gmail.com', 'you@hotmail.com']`
         * Desired days and times
           * Format is `{day_of_week: times, day_of_week: times...}`
         * Write days in full e.g. "Monday" - "Sunday"
           * Use strings in format "0000-2359" for start-end
           * e.g. `{"Monday": "1800-2200"}` would mean show Monday films starting between 6 and 10pm
          * Credentials of an email account (gmail or hotmail) to use
            * Credentials should be inside a dictionary called 'email' with keys `gmail_user` and `gmail_password` and/or `hotmail_user` and `hotmail_password`
   

## How to run
* Create the config file with the recipients, venues, email recipients and desired times (optional)
* Amend main.py if desired to adjust location of config file, any email parameters and location of python installation on first line
* Make the `main.py` script executable using `chmod +x 'path/to/file'`
* Add to crontab using `crontab -e` to trigger on a regular basis

## Requirements
* Python 3.6+
* requests, beautiful soup (bs4) with lxml parser, smtp and email libraries
* A gmail or hotmail email account to send mail from. 
   * _NB using gmail will require you to ['allow access to less secure apps'](https://support.google.com/accounts/answer/6010255?hl=en)_


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
