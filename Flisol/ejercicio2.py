from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def Write(text):
	return elem.send_keys(text)

def Clear():
	return elem.clear()

driver = webdriver.Firefox()
driver.get("https://www.google.com.mx/#q=traductor")
elem = driver.find_element_by_id('tw-source-text-ta')
cont = 1
while cont == 1:
	Write(text=input())
	cont = int(input('Press 1 to continue translate or 2 exit: '))
	if cont == 1:
		Clear()
	else:
		print('Bye')
		driver.close()