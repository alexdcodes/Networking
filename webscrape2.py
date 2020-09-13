from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

import pandas as pd
import re
import itertools

driver = webdriver.Chrome("C:/Python37_64/chromedriver.exe")


file_name = "C:/Users/alexdcodes/PycharmProjects//List.xlsx"

book = pd.read_excel(file_name, sheet_name = 'Good List-892')

store_list = book['S N'].tolist()

address_list = book['Address'].tolist()

enp_addresses = book['SA '].tolist()

device_list = book['Meh Number'].tolist()



total = len(store_list)

for x in range(total):
    value = str(store_list[x])
    if value[0] == '0':
        if value[1] != '0':
            store_list[x] = int(value[1:5])
        elif value[2] != '0':
            store_list[x] = int(value[2:5])
        elif value[3] != '0':
            store_list[x] = int(value[3:5])
        else:
            store_list[x] = int(value[4])
    elif 48 <= ord(value[0]) <= 57:
        store_list[x] = int(value[0:4])

    if len(str(address_list[x])) < 3:
        address_list[x] = enp_addresses[x]



time.sleep(4)

usernameBox = driver.find_element_by_id('login').find_element_by_id('usr_name')

passwordBox = driver.find_element_by_id('login').find_element_by_id('usr_password')

loginButton = driver.find_element_by_id('login').find_element_by_tag_name('button')

usernameBox.send_keys("nagararjan.k@eportal")

passwordBox.send_keys("Cisco#12")

loginButton.click()


time.sleep(10)

driver.switch_to.frame(driver.find_elements_by_name("leftnav")[1])

web_text = driver.page_source

time.sleep(2)

driver.find_element_by_link_text('Reporting').click()

time.sleep(7)

driver.switch_to.parent_frame()

driver.switch_to.frame('contentpage')

driver.find_element_by_link_text('Upgraded Network Performance Reporting').click()

driver.switch_to.window(driver.window_handles[1])


time.sleep(15)

ce_filter = driver.find_element_by_class_name("IvTableFilterBar").find_element_by_tag_name('span').find_element_by_tag_name('input')

ce_name = []
ip_address = []
connected_port = []

for x in range(81, 91):
    ce_filter.send_keys(device_list[x])

    time.sleep(1)

    try:
        span_list = driver.find_element_by_id('iv_table_TablePane_1-0').find_elements_by_tag_name('span')
    except:
        connected_port.append("ERR")
        ce_name.append("ERR")
        ip_address.append("ERR")
        print("Issue at store" + str(store_list[x]))
        ce_filter.clear()
        continue

    try:
        connected_port.append(span_list[0].text.split()[1])
    except:
        connected_port.append(span_list[0].text)

    ce_name.append(span_list[5].text)

    if ce_name != device_list[x]:
        print("Issue at store" + str(store_list[x]))

    ip_address.append(span_list[9].text)
    ce_filter.clear()


