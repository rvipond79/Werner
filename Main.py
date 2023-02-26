#import selenium
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
#setup the driver
driver = webdriver.Chrome()
#open the url
driver.get("https://www.amazon.com")
#find the search box and type "socks" in the search box and hit enter
driver.find_element(By.ID, "twotabsearchtextbox").send_keys("socks")
driver.find_element(By.ID, "nav-search-submit-button").click()
#scroll down to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")










#sleep for 5 seconds
time.sleep(5)
