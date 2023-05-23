from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

url = "https://tinder.com/app/recs"


# Skipping Tinder login steps


driver.get(url=url)

like_button = driver.find_element(By.XPATH, '//*[@id="u-1779218560"]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button')

for i in range(101):
    time.sleep(2)
    like_button.click()