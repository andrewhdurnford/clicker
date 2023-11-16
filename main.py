from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import datetime
import secret
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import pytesseract
import urllib.request 
import cv2
import os
import openai

driver = webdriver.Chrome()
driver.get("https://join.iclicker.com")
time.sleep(1)
join_code = driver.find_element(By.ID, "joinCode")
join_code.send_keys("cwly")
enter = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-student/div[1]/div/button")
enter.click()
time.sleep(1)
sign_in = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-student/non-fsso/div[1]/div/div[2]/button[1]")
sign_in.click()
time.sleep(1)
username = driver.find_element(By.XPATH, "//*[@id=\"userEmail\"]")
username.send_keys(secret.username)
password = driver.find_element(By.XPATH, "//*[@id=\"userPassword\"]")
password.send_keys(secret.password)
log_in = driver.find_element(By.XPATH, "//*[@id=\"sign-in-button\"]")
log_in.click()
# Make sure the website loads instead of using time.sleep
time.sleep(2)

wait = WebDriverWait(driver, timeout=100000000000000000000000000000000)
newJoin = wait.until(EC.element_to_be_clickable(driver.find_element(By.XPATH, "//*[@id=\"btnJoin\"]")))
newJoin.click()
time.sleep(1000000)

