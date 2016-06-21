from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 


driver = webdriver.Chrome()
driver.get("https://paginas.seccionamarilla.com.mx/antigua-taqueria-la-oriental/tacos-arabes-a-domicilio/puebla/puebla/-/bella-vista/")
elem = driver.find_element_by_xpath('//*[@id="id_email"]')
elem.send_keys("David Cermeño Moranchel")
elem1 = driver.find_element_by_xpath('//*[@id="id_phone"]')
elem1.send_keys("david.arcshtag@gmail.com")
elem2 = driver.find_element_by_xpath('//*[@id="id_name"]')
elem2.send_keys("5561167626")
elem3 = driver.find_element_by_xpath('//*[@id="id_message"]')
elem3.send_keys("Quiero unos tacos pa' la cruda ")
elem4 = driver.find_element_by_xpath('//*[@id="sb-module-9067119"]/div/div/form/div/fieldset/p[5]/input')
elem4.click()


