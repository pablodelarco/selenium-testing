import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_browser = webdriver.Chrome()
chrome_browser.maximize_window()
chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title
show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")

assert "Show Message" in chrome_browser.page_source

user_message = chrome_browser.find_element(By.ID, "user-message")
# chrome_browser.find_element(By.CLASS_NAME, "btn-default")
time.sleep(2)
user_message.clear()
user_message.send_keys("THIS IS THE TEXT")
time.sleep(2)
show_message_button.click()  # this is the button that says "Show Message"
output_message = chrome_browser.find_element(By.ID, "display")

assert "THIS IS THE TEXT" in output_message.text


chrome_browser.implicitly_wait(5)
popup = chrome_browser.find_element(By.ID, "at-cv-lightbox-close")
popup.click()
