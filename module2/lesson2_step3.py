from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
from selenium.webdriver.support.ui import Select 

try:
	
	link = "http://suninjuly.github.io/selects1.html"
	browser = webdriver.Chrome()
	browser.get(link)

	elem_1 = browser.find_element(By.ID, "num1")
	num_1 = int(elem_1.text)

	elem_2 = browser.find_element(By.ID, "num2")
	num_2 = int(elem_2.text)

	answer_sum = num_1 + num_2

	select = Select(browser.find_element(By.TAG_NAME, "select"))
	select.select_by_value(str(answer_sum))

	button = browser.find_element(By.TAG_NAME, "button")
	button.click()

finally:

	time.sleep(10)

	browser.quit()
