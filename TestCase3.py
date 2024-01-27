import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

class TestTriformDashboardNavigation(unittest.TestCase):

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

    def test_navigate_dashboard_sections(self):
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
        password_field.send_keys(Keys.RETURN)

        # Switch back to the main window
        driver.switch_to.window(driver.window_handles[0])


        # Navigate to the dashboard (assuming already logged in from Test Case 2)
        driver.get('https://triform.movs.ai/dashboard')  # Replace with the actual URL


        # Assert the main dashboard title (updated for XPath)
        welcome_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/h1"))
        )
        self.assertEqual(welcome_title.text, "🚀 Welcome to Movs.ai! 🌟")  # Include emojis in assertion


        # Locate and verify the module request section (using XPath)
        module_request_section = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div/div/div[1]/h2"))
        )
        self.assertEqual(module_request_section.text, "Module requests")


        
    def tearDown(self):
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
