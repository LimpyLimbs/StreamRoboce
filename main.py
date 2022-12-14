from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import environ

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
URL = "https://www.twitch.tv/pest"
driver = webdriver.Chrome(options=chrome_options)

driver.get(environ.get('URL'))

exit_script = False

while not exit_script:
    None

'''
Notes:
learn how to orchestrate containers
'''
