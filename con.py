import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import util


def Istp():
	chrome_options = Options()
	chrome_options.add_argument('headless')
	chrome_options.add_argument('start-maximized')
	

	driver = webdriver.Chrome(chrome_options=chrome_options)
	usernameStr = 'your username'
	passwordStr = 'your password'

	driver.maximize_window()
	driver.get('https://accounts.google.com/signin/v2/identifier?service=cl&passive=1209600&osid=1&continue=https%3A%2F%2Fcalendar.google.com%2Fcalendar%2Frender&followup=https%3A%2F%2Fcalendar.google.com%2Fcalendar&scc=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin');

	username = driver.find_element_by_id('identifierId')
	username.send_keys(usernameStr)

	nextButton = driver.find_element_by_id('identifierNext')
	nextButton.click()

	password = WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((By.NAME, "password")))

	password.send_keys(passwordStr)

	signInButton = driver.find_element_by_id('passwordNext')
	signInButton.click()

	time.sleep(2)
	

	### make changes so that the the current and future events are always visible
	IIdp(driver)
	driver.quit()
def IIdp(driver):
	x = WebDriverWait(driver, 10).until(
	    EC.presence_of_element_located((By.ID, "mainbody")))
	util.fullpage_screenshot(driver, "test.png")
	time.sleep(2)
	import PIL
	from PIL import Image

	img = Image.open('test.png')
	
	hsize = 768
	img = img.resize((1366,hsize), PIL.Image.ANTIALIAS)
	img.save('test.png') 

	time.sleep(2)

	os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /ImagePath/test.png")

# FUnction call	
Istp()




