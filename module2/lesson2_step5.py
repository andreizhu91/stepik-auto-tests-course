from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

	link = "http://suninjuly.github.io/execute_script.html"
	browser = webdriver.Chrome()
	browser.get(link)

	x_element = browser.find_element(By.ID, "input_value")
	x = x_element.text
	y = calc(x)

	answer = browser.find_element(By.ID, "answer")
	answer.send_keys(y)

	checkbox_robot = browser.find_element(By.ID, "robotCheckbox")
	checkbox_robot.click()

	radio_robots_rule = browser.find_element(By.ID, "robotsRule")
	browser.execute_script("return arguments[0].scrollIntoView(true);", radio_robots_rule)
	radio_robots_rule.click()

	button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
	browser.execute_script("return arguments[0].scrollIntoView(true);", button)
	button.click()

finally:
	
	time.sleep(20)
	browser.quit()
