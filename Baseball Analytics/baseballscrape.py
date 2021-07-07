from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time as t

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

browser = webdriver.Chrome(executable_path="chromedrivers/chromedriver.exe", chrome_options=options)
browser.get("https://www.baseball-reference.com/boxes/ATL/ATL202106300.shtml")

table = browser.find_element_by_xpath('//*[@id="play_by_play"]')
rows = table.find_elements_by_xpath('//tbody/tr')
for row in rows:
    head = row.find_element_by_xpath("//th").text
    items = [item.text for item in row.find_elements_by_xpath("//td")]
    print([head] + items)
    break
print("YEEEEEEEEEEEEEEEEEEE")
