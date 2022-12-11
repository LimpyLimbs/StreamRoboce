from selenium import webdriver

PATH = r"C:\Users\Eddie\Documents\chromedriver.exe"
driver = webdriver.chrome

driver.get("https://techwithtim.net")
print(driver.title)
driver.quit

