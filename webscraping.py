from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
import pandas as pd
import itertools

update_mode = False

debug_mode = True

driver = webdriver.Chrome("C:/Users//Downloads/chromedriver_win32/chromedriver.exe")

if update_mode == True:
    file_name = "Downloads\file.txt"

    book = pd.read_excel(file_name, sheet_name = 0)

    print(book.columns.tolist())
    meh_list = book['meh number'].tolist()

meh_numbers = []
s_n = []
brands = []
s_ad = []
cities = []
p_n = []
meh_connection_types = []
meh_secondary_p = []
ether0s = []
wan_ips = []
masks = []
account_names = []


for number in range(0,500):

    if update_mode == True:
        zeros = ""

        if(len(str(number)) < 5):
            for x in range(5-len(str(number))):
                zeros += "0"
                item_number = 0
    else:
        offset = int(number/10) * 10
        item_number = number % 10

    if update_mode == True:
        driver.get('http://aws.domain.com/searchin.php')
        numberBox = driver.find_element_by_name('BannerName')
        numberBox.send_keys(zeros + str(number) + Keys.RETURN)
        link = driver.find_element_by_xpath("//td[@bgcolor='#EADEA5']/font/a").click()
    else:
        driver.get('http://aws.domain.com/mehlist.php?offset=' + str(offset))
        link_list = driver.find_elements_by_xpath("//td[@bgcolor='#EADEA5']/font/a")
        link = link_list[item_number]
        
    search_list = driver.find_elements_by_xpath("//td[@bgcolor='#EADEA5']/font/b")
    banner_list = driver.find_elements_by_xpath("//td[@width='18%']/font")
    address_list = driver.find_elements_by_xpath("//td[@width='32%']/font")
    game_name_list = driver.find_elements_by_xpath("//td[@width='20%']/font")
    phone_list = driver.find_elements_by_xpath("//td[@width='15%']/font")

    s_n.append(search_list[item_number].text)
    brands.append(banner_list[item_number+1].text)
    s_ad.append(address_list[item_number+1].text)
    cities.append(game_name_list[item_number+1].text)
    p_n.append(phone_list[3+item_number*2].text)

    try:
        link.click()
    except:
        print("no value found for " + str(number))
        continue

    current_url = driver.current_url
    meh_numbers.append(current_url[-4:])

    content = driver.page_source
    soup = BeautifulSoup(content, 'html.parser')

    ftags = soup.find_all('font')

    

    meh_connection_types.append(ftags[18].text)

    meh_secondary_phones.append(ftags[20].text)

    ether0s.append(ftags[22].text)

    wan_ips.append(ftags[24].text)

    masks.append(ftags[26].text)

    account_names.append(ftags[28].text)

   
data = pd.DataFrame({'Search Number':s_n, 'Banner':brands, 'meh number':meh_numbers, 'meh add':s_ad,
'game_name':cities, 'Phone':p_n, 'Connection Type':meh_connection_types,
'Secondary': meh_secondary_phones, 'IP': ether0s, 'WAN IP': wan_ips, 'MASK':masks, 'AN':account_names})


data.to_csv(r'shakingbacon', index = False, encoding='utf-8')
