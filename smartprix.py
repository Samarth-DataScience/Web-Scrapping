# Import necessary modules and classes from the Selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Set up the ChromeDriver service using the Service class
s = Service('C:/Users/Test User/Desktop/chromedriver.exe')

# Create a Chrome WebDriver instance and associate it with the ChromeDriver service
driver = webdriver.Chrome(service=s)

# Maximize the browser window
driver.maximize_window()

# Navigate to the specified URL
driver.get('https://www.smartprix.com/mobiles')

# Find the "Load More" element on the webpage using XPath
load_more = driver.find_element(by=By.XPATH, value= '//*[@id="app"]/main/div[1]/div[3]/div[3]')

# Click the "Load More" button to load additional content
load_more.click()

# (Optional) Introduce a delay of 2 seconds to allow the page to load (for demonstration purposes)
time.sleep(2)
