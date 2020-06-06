import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import html5lib

browser = webdriver.Chrome()
browser.get("https://www.worldometers.info/coronavirus/")
coronatable = browser.find_element_by_xpath("//*[@id=\"nav-today\"]/div")
time.sleep(10)
source_code = coronatable.get_attribute('innerHTML')


coronaDataframe = pd.read_html(source_code,skiprows=[1])

browser.quit()
coronaDataframe = coronaDataframe[0]