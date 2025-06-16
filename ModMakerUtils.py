import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver


moddingAuthor = "NotchArrow"
moddingPackage = "com.notcharrow"

def getVersionInfo(modVersion):
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--headless")
	driver = webdriver.Chrome(options=chrome_options)
	driver.get("https://fabricmc.net/develop/")

	time.sleep(3)

	dropdown = Select(driver.find_element(By.XPATH, "/html/body/main/div/div[2]/p[2]/select"))
	dropdown.select_by_visible_text(modVersion)

	time.sleep(1)

	versionInfo = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/div/pre/code").text.split("\n")
	return versionInfo