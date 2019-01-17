from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
import time
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
driver.get('http://www.wandoujia.com/top/app')
loadMoreBtn = driver.find_element_by_id("j-refresh-btn")
#print loadMoreBtn.get_attribute("class")
initialAppCount=24
pressBtnCount=50
for num in range(0,pressBtnCount):
	print num
	time.sleep(1)
	loadMoreBtn.click()
	initialAppCount=initialAppCount+12
	#print initialAppCount
	wait =WebDriverWait(driver, 20);
	wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='j-top-list' and count(li) >="+str(initialAppCount)+"]")));


liElements=driver.find_elements_by_xpath("//*[@id='j-top-list']//li[@class='card']")
print len(liElements)
f_handler=open('xx.txt', 'w')
sys.stdout=f_handler
print driver.page_source.encode('utf-8')

#print driver.title