from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://paginas.seccionamarilla.com.mx/antigua-taqueria-la-oriental/tacos-arabes-a-domicilio/puebla/puebla/-/bella-vista/")
# assert "Python" in driver.title
elem = driver.find_element_by_id("")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

