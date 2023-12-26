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
for i in range(55):
    load_more.click()
    print('step no. :', i+1)
    time.sleep(2)

# Get the HTML source code of the current webpage
html = driver.page_source

# Open a file named 'smartprix_mobiles' in write mode with UTF-8 encoding
with open('smartprix_mobiles', 'w', encoding='utf-8') as f:
    # Write the captured HTML source code to the file
    f.write(html)

