from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

	button = browser.find_element(By.ID, "book")

	button.click()

	x = browser.find_element(By.ID, "input_value")

	value_x = x.text

	ans = browser.find_element(By.ID, "answer")

	ans.send_keys(calc(value_x))

	button_2 = browser.find_element(By.ID, "solve")

	button_2.click()

finally:

	time.sleep(20)

	browser.quit()

