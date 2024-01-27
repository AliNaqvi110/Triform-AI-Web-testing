import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

class TestManageAccountSettings(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('start-maximized')
        chrome_options.add_argument('disable-infobars')
        chrome_options.add_argument('--disable-browser-side-navigation')
        # Use ChromeDriverManager to get the Chrome WebDriver
        self.driver = webdriver.Chrome()

    def test_manage_account_settings(self):
        # Load environment variables
        load_dotenv()
        github_username = os.getenv('GITHUB_USERNAME')
        github_password = os.getenv('GITHUB_PASSWORD')

        driver = self.driver

        # Navigate to the login page
        driver.get('https://triform.movs.ai/login')  # Replace with the actual URL

        # Locate the "Get Early Bird Access" button using a CSS selector
        early_bird_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'p.font-mono.font-bold.text-white'))
              )
         # Click the button
        early_bird_button.click()
        
        # Wait for GitHub login page to appear within the same window
        WebDriverWait(driver, 10).until(EC.url_contains("github.com/login"))  # Or a more specific condition
        # Fill in GitHub credentials (replace with your credentials)
        username_field = driver.find_element(By.ID, 'login_field')
        username_field.send_keys(github_username)
        
        password_field = driver.find_element(By.ID, 'password')
        password_field.send_keys(github_password)
        # Submit the login form
        password_field.send_keys(Keys.ENTER)

        # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])

        # Navigate to the profile 
        driver.get('https://triform.movs.ai/user/profile')  # Replace with the actual URL

        user_name = 'Ali Naqvi'
        email = 'jesuisetudaint110@gmail.com'
        # Fill in the User Name
        uname_field = driver.find_element(By.ID, 'name')
        uname_field.send_keys(user_name)
        uemail_field  = driver.find_element(By.ID, 'email')
        uemail_field.send_keys(email)

        # Save changes
        driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/div[1]/div[2]/form/div[2]/button').click()

        
        # Wait for the API token dialog box to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "px-6.py-4")))  # Adjusted based on class

        # Verify the API token is displayed in the input field
        api_token_text = driver.find_element(By.CSS_SELECTOR, "input.border-gray-700[type='text']").get_attribute("value")
        assert api_token_text != "", "API token is not displayed in the dialog box"


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
