from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import os

try:

	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)

	first_name = browser.find_element(By.NAME, "firstname")
	first_name.send_keys("Ivan")

	last_name = browser.find_element(By.NAME, "lastname")
	last_name.send_keys("Ivanov")

	email = browser.find_element(By.NAME, "email")
	email.send_keys("test@test.ru")

	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')

	file = browser.find_element(By.ID, "file")
	file.send_keys(file_path)

	button = browser.find_element(By.CLASS_NAME, "btn")
	button.click()

finally:

	time.sleep(20)

	browser.quit()


