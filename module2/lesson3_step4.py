from selenium import webdriver
from selenium.webdriver.common.by import By 
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	button_1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
	button_1.click()

	confirm = browser.switch_to.alert
	confirm.accept()

	x = browser.find_element(By.ID, "input_value")
	value_x = x.text

	ans = browser.find_element(By.ID, "answer")
	ans.send_keys(calc(value_x))

	button_2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
	button_2.click()

finally:

	time.sleep(20)

	browser.quit()


