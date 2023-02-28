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
#sleep for 2 seconds
time.sleep(2)
#scroll up to the top of the page
driver.execute_script("window.scrollTo(0, 0);")
#sleep for 2 seconds
time.sleep(2)
#click Sort by dropdown and select "Price: High to Low"
driver.find_element(By.ID, "a-autoid-0-announce").click()
driver.find_element(By.ID, "s-result-sort-select_2").click()
time.sleep(2)
#click Eligible for Free Shipping checkbox
driver.find_element(By.ID, "p_76/2661625011").click()
time.sleep(5)
#click the first product
driver.find_element(By.CSS_SELECTOR, ".a-link-normal.a-text-normal").click()
#sleep for 2 seconds
time.sleep(2)
#click Add to Cart button
driver.find_element(By.ID, "add-to-cart-button").click()
#sleep for 2 seconds
time.sleep(2)