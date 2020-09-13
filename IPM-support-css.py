import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.common.action_chains import ActionChains

def reload(chrome_options):
    driver = webdriver.Chrome("C:/Users/winbluz/Downloads/chromedriver_win32/chromedriver.exe", options = chrome_options)

    driver.implicitly_wait(10)

    driver.get("")


    time.sleep(1)

    login_username = driver.find_element_by_name('l')
    login_username.send_keys("")

    login_password = driver.find_element_by_name('p')
    login_password.send_keys("")

    tag_button = driver.find_element_by_class_name('x-btn-center').find_element_by_tag_name('em')

    login_button = driver.find_element_by_class_name('x-btn-text')
    login_button.click()

    time.sleep(20)
    return driver

def remove_unselectables(driver, arg_location, element):
    driver.execute_script("arguments[" + str(arg_location) + "].setAttribute('unselectable', 'off')", element)

def exp_wait(driver, by_type, element):
    return WebDriverWait(driver, 20).until(EC.presence_of_element_located((by_type, element)))

def wait_click(driver, by_type, element):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by_type, element)))
