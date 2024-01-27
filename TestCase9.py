import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv


class TestEnvironmentVariables(unittest.TestCase):

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--disable-browser-side-navigation')
        # Use ChromeDriverManager to get the Chrome WebDriver
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_environment_variables(self):
        # Load environment variables
        load_dotenv()
        github_username = os.getenv('GITHUB_USERNAME')
        github_password = os.getenv('GITHUB_PASSWORD')

        driver = self.driver

        # Navigate to the signup page
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
        driver.find_element(By.NAME, 'commit').click()
        
        

        
        # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])

        # Move to environment page
        driver.get('https://triform.movs.ai/environment')

        # Click Add button
        driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/div/div/div/div[1]/div[2]/button').click()

        # # Wait for the new window to appear
        # WebDriverWait(driver, 10).until(
        #     EC.number_of_windows_to_be(2) # Check for 2 windows (original + new)
        # )

        # Switch to the new window
        new_window_handle = driver.window_handles[-1]  # Access the last opened window
        driver.switch_to.window(new_window_handle)

        # get name field of  variable and fill that
        name = "OOPENAI_KEY"
        name_field = driver.find_element(By.ID, 'name')
        name_field.send_keys(name)
        # get value field of the variable in fill taht also
        value = "fkljdfiosdofnrjorjhngnioxc"
        value_field = driver.find_element(By.ID, 'value')
        value_field.send_keys(value)
        # Fill Description field as well
        descript = "An API key for the Open AI to acces Various Models such as GPT3, GPT3.5, GPT4 etc"
        des_field = driver.find_element(By.ID, 'description')
        des_field.send_keys(descript)
        # Add All and Save changes
        driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/form/div[4]/button[2]').click()



    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
