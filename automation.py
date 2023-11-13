import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def run_selenium_demo():
    try:
        # Initialize Chrome browser
        chrome_browser = webdriver.Chrome()
        chrome_browser.maximize_window()

        # Navigate to the Selenium Easy Demo page
        chrome_browser.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")

        # Enter a user message and click "Show Message" button
        user_message = chrome_browser.find_element(By.ID, "user-message")
        time.sleep(2)
        user_message.clear()
        user_message.send_keys("THIS IS THE TEXT")

        time.sleep(2)

        show_message_button = chrome_browser.find_element(By.CLASS_NAME, "btn-primary")
        show_message_button.click()

        # Verify the displayed output
        output_message = chrome_browser.find_element(By.ID, "display")
        assert "THIS IS THE TEXT" in output_message.text

        # Close popup if present
        chrome_browser.implicitly_wait(5)
        popup = chrome_browser.find_element(By.ID, "at-cv-lightbox-close")
        popup.click()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        chrome_browser.quit()


if __name__ == "__main__":
    run_selenium_demo()
