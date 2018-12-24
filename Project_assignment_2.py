# coding=utf-8

import time
#allow using sleep commands


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="/Users/yarzi01/Documents/DevOps/chromedriver")
driver.get("http://localhost:5000/")              #open the webpage
# driver.fullscreen_window()
time.sleep(5)

my_txt=driver.find_element_by_css_selector("body").text
print(smart_text(my_txt))

driver.close()
driver.quit()

#end of program

