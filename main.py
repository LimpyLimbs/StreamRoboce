from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox") # linux only
# PATH = r"C:\Users\Eddie\Documents\chromedriver.exe"
URL = "https://www.twitch.tv/limpylimbs"
driver = webdriver.Chrome(options=chrome_options)

driver.get(URL)

quit = False

while not quit:
     None

'''
Notes:
learn how to create a Dockerfile in windows
learn how to do headless browsing
import chrome, webdriver,
Build the image
__version__ = "4.7.2"
python is a debian-based OS
'''