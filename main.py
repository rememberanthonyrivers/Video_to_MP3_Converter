from selenium  import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

path_to_driver = ("/Users/tony/Desktop/code_folder/linkedin_bot/ChromeDriver/chromedriver.exe")

s = Service(path_to_driver)

driver = webdriver.Chrome(service=s)

url = 'https://ytmp3.nu/9/youtube-to-mp3'

while True:
    print('\n\t*** Lets begin ! ***')
    driver.get(url)
    mp4_to_mp3_url_field = driver.find_element(By.ID, "url")
    url_for_extraction = input('\n\tEnter the videos url for conversion to mp3 : ')
    mp4_to_mp3_url_field.send_keys(url_for_extraction)
    mp4_to_mp3_url_field.send_keys(Keys.ENTER)
    time.sleep(8)
    download_btn = driver.find_element(By.LINK_TEXT, 'Download').click()
    time.sleep(6)
    print('\n\t*** Thank you come again ! ***\n')
    break