from selenium import webdriver
from selenium.common.exceptions import NoSuchFrameException
import sys
import time
from datetime import date
from datetime import datetime


PATH = "chromedriver.exe"
options = webdriver.ChromeOptions()



def main():
    options.add_argument(r'--user-data-dir=')
    driver = webdriver.Chrome(PATH, options= options)
    driver.get("https://web.whatsapp.com/")
    time.sleep(15)



if __name__ == '__main__':
    main()

