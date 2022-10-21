from selenium import webdriver
import chromedriver_binary
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import re


def parse_hh(job_title):
    browser = webdriver.Chrome()  # launch browser
    browser.get("http://hh.ru")  # open hh.ru

    ok_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="region-clarification-confirm"]')
    ok_button.click()

    search_input = browser.find_element(By.ID, "a11y-search-input")  # search input
    search_input.send_keys(job_title)  # Text input

    search_button = browser.find_element(By.CSS_SELECTOR, '[data-qa="search-button"]')


    search_button.click()

    try:
        job_count = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-search-header"] h1')  # number of vacancies
    except NoSuchElementException:
        job_count = browser.find_element(By.CSS_SELECTOR, '[data-qa="vacancies-total-found"]')  # 2'nd variant

    # re.sub - change
    # \D symbols - not numbers
    count = re.sub(r"\D", "", job_count.text)

    browser.close()  # close browser
    return count
