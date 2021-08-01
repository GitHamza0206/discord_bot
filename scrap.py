from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.lichess.org")
button = driver.find_element_by_class('button button-metal config_friend active')
print(elem.get_attribute("class"))
driver.close()