import random
import csv
import subprocess
import sys
import os

try:
    import selenium
    from selenium import webdriver
except ImportError:
    subprocess.call([sys.executable, '-m', 'pip', 'install', selenium])

from functions import *

# =================================
# CHOOSE A RANDOM MOVIE
# =================================

# Open the watchlist .csv file and choose a random movie
try:
    with open('WATCHLIST.csv') as f:
        rows = csv.DictReader(f, delimiter=',', quotechar='"')
        movies = [row for row in rows if row['Title Type'] == 'movie']

    movie = random.choice(movies)
    text = """There are {num} feature films in your watchlist.

    I have chosen the following movie for you:

    ===========================================

        {Title} ({Year})

        IMDb Rating:    {IMDb Rating}
        Genres:         {Genres}
        Runtime:        {Runtime (mins)}min
        Link:           {URL}

    ===========================================

    You have two options:
    1 - Rate "{Title}" (also removes it from the watchlist)
    2 - Remove "{Title}" from your watchlist
    """
    print(text.format(num=len(movies), **movie))
except FileNotFoundError:
    print('WATCHLIST.csv not found.')


def main():
    while True:
        try:
            # Choose between 2 options (rate & remove the movie from the watchlist)
            choice = int(input('Choose an option: '))

            try:
                # try with chrome web driver
                options = webdriver.ChromeOptions()
                options.headless = True
                options.add_experimental_option('excludeSwitches', ['enable-logging'])
                driver = webdriver.Chrome(options=options, service_log_path='nul')
            except:
                # if that doesn't work try firefox
                options = webdriver.FirefoxOptions()
                options.headless = True
                options.set_preference('devtools.jsonview.enabled', False)
                driver = webdriver.Firefox(options=options, service_log_path='nul')

            if choice == 1:  # rate the movie on IMDb
                print('You chose to rate "{Title}".'.format(**movie))
                locate_movie(driver, movie)
                rate_movie(driver, movie)
                remove_movie(driver, movie)
                print('Goodbye.')
                driver.quit()
                break
            elif choice == 2:  # remove the movie from IMDb watchlist
                print('You chose to remove "{Title}" from your watchlist.'.format(**movie))
                locate_movie(driver, movie)
                remove_movie(driver, movie)
                print('Goodbye.')
                driver.quit()
                break
        except:
            print('Invalid input.')


if __name__ == '__main__':
    main()
    os.system('pause')
