import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import html5lib

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options = chrome_options)
browser.get("https://www.worldometers.info/coronavirus/")
coronatable = browser.find_element_by_xpath("//*[@id=\"nav-today\"]/div")
time.sleep(10)
source_code = coronatable.get_attribute('innerHTML')


coronaDataframe = pd.read_html(source_code,skiprows=[1])

browser.quit()

coronaDataframe = coronaDataframe[0]
print(coronaDataframe.shape[0])
coronaDataframe.head()