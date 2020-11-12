from selenium import webdriver
from selenium.webdriver.common.by import By 
import pytest
import time
import math

@pytest.fixture(scope="function")
def browser():
	browser = webdriver.Chrome()
	browser.implicitly_wait(10)
	yield browser
	time.sleep(2)
	browser.quit()

@pytest.mark.parametrize('id_lesson', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_feedback(browser, id_lesson):
	link = f"https://stepik.org/lesson/{id_lesson}/step/1"
	browser.get(link)
	answer_field = browser.find_element(By.CLASS_NAME, "textarea")
	answer = math.log(int(time.time()))
	answer_field.send_keys(str(answer))
	button = browser.find_element(By.CLASS_NAME, "submit-submission")
	button.click()
	feedback = browser.find_element(By.CLASS_NAME, "smart-hints__hint")
	text_feedback = feedback.text
	assert text_feedback == "Correct!", "Text of feedback differents on text default"