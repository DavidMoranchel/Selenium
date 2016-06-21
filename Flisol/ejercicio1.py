from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://paginas.seccionamarilla.com.mx/antigua-taqueria-la-oriental/tacos-arabes-a-domicilio/puebla/puebla/-/bella-vista/")
elem = driver.find_element_by_xpath('//*[@id="id_email"]')
elem.send_keys("David Cermeño Moranchel")
elem = driver.find_element_by_xpath('//*[@id="id_phone"]')
elem.send_keys("david.arcshtag@gmail.com")
elem = driver.find_element_by_xpath('//*[@id="id_name"]')
elem.send_keys("5561167626")
elem = driver.find_element_by_xpath('//*[@id="id_message"]')
elem.send_keys("Quiero unos tacos pa' la cruda ")

