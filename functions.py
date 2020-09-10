from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException


# open the IMDb page of the random chosen movie
def locate_movie(driver, movie):
    print('Locating "{Title}"...'.format(**movie))
    movie_url = '{URL}'.format(**movie)
    driver.get(movie_url)

    # sign in, enter email & password and submit the sign in form
    print('Signing in...')
    sign_in = driver.find_element_by_xpath('//*[@id="imdbHeader"]/div[2]/div[5]/a/div')
    sign_in.click()
    sign_in_imdb = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#signin-options > div > div:nth-child(2) > a:nth-child(1)')))
    sign_in_imdb.click()

    EMAIL = input('Enter your IMDb email address: ')
    PASS = input('Enter your IMDb password: ')

    email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#ap_email')))
    email.send_keys(EMAIL)
    password = driver.find_element_by_css_selector('#ap_password')
    password.send_keys(PASS)

    sign_in_submit = driver.find_element_by_css_selector('#signInSubmit')
    sign_in_submit.click()

    print('Signed in.')


# rate the movie
def rate_movie(driver, movie):
    print('Enter the rating for "{Title}"'.format(**movie))
    rating = int(input())

    ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
    rate_this = WebDriverWait(driver, 10, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#star-rating-widget > div > button')))
    rate_this.click()

    # Rate and remove from watchlist
    if rating == 1:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(1)')
        rate_star.click()
    elif rating == 2:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(2)')
        rate_star.click()
    elif rating == 3:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(3)')
        rate_star.click()
    elif rating == 4:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(4)')
        rate_star.click()
    elif rating == 5:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(5)')
        rate_star.click()
    elif rating == 6:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(6)')
        rate_star.click()
    elif rating == 7:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(7)')
        rate_star.click()
    elif rating == 8:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(8)')
        rate_star.click()
    elif rating == 9:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(9)')
        rate_star.click()
    elif rating == 10:
        rate_star = driver.find_element_by_css_selector(
            '#star-rating-widget > div > div > span:nth-child(1) > span > a:nth-child(10)')
        rate_star.click()

    print('"{Title}" rated.'.format(**movie))


# remove the movie from the watchlist
def remove_movie(driver, movie):
    print('Removing "{Title}" from your watchlist...'.format(**movie))

    remove = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="title-overview-widget"]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div')))
    remove.click()

    print('"{Title}" removed from your watchlist.'.format(**movie))
