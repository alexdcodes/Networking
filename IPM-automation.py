from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver


import time
import re
import supporting_css


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-ssl-errors=yes')
chrome_options.add_argument('--ignore-certificate-errors')


driver = supporting_css.reload(chrome_options)

action = ActionChains(driver)


time.sleep(10)


discovery_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="ext-gen32"]/div/li[4]/ul/li[1]/div/a/span')
discovery_button.click()

input_bar = supporting_css.exp_wait(driver, By.CLASS_NAME, 'x-form-element').find_element_by_tag_name('input')
input_bar.clear()

address_scan = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/div/div/ul/li[3]/a')
address_scan.click()


time.sleep(3)

input_bar.send_keys("0.0.0.0.0")
input_bar = None


submit_button = driver.find_element_by_xpath('/html/body/div[14]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
submit_button.click()
submit_button = None

time.sleep(10)

\node_list_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="ext-gen32"]/div/li[1]/ul/li[1]/div/a/span')
node_list_button.click()

time.sleep(3)

action.context_click(node_list_button).perform()

create_sub_view = driver.find_element_by_link_text("Create a sub view")
create_sub_view.click()

time.sleep(3)

\input_bar = supporting_css.exp_wait(driver, By.CLASS_NAME, 'x-form-element').find_element_by_tag_name('input')
input_bar.clear()

time.sleep(3)

\input_bar.send_keys("meh " + "245")

input_bar = None

\submit_button = driver.find_element_by_xpath('/html/body/div[23]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
submit_button.click()

submit_button = None

\time.sleep(5)

\driver.quit()

\driver = supporting_css.reload(chrome_options)

action = ActionChains(driver)

#
time.sleep(5)

\node_list = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/div/li[1]/ul/li[1]/ul').find_elements_by_tag_name('a')

\
for element in node_list:
    node_name = element.find_element_by_tag_name('span').text
    if node_name == ("meh " + "245"):
        print("found")
        action.context_click(element).perform()
        break

node_filter = driver.find_element_by_link_text('Edit filter view')
node_filter.click()

time.sleep(1)

add_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div[1]/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
add_button.click()

time.sleep(0.5)

input_bar = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[2]')
input_bar.click()

time.sleep(0.5)

input_bar_2 = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[2]/div')
input_bar_2.click()

input_bar = None

time.sleep(1)

input_bar = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-layer x-combo-list "]/div/div[10]')
input_bar.click()

input_bar = None

input_bar = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[3]/div/div')
input_bar.click()

input_bar_2 = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[3]/div')
input_bar_2.click()

input_bar = None

time.sleep(1)

input_bar = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-layer x-combo-list "][2]/div/div[7]')
input_bar.click()

input_bar = None

input_bar = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/table/tbody/tr/td[4]/div/div')
input_bar.click()

input_bar_2 = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[2]/div[4]/input')
input_bar_2.send_keys("0245")

submit_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
submit_button.click()


time.sleep(10)

connector_button = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[2]/div[2]/div/ul/div/li[4]/ul/li[3]/div/a/span')
connector_button.click()

time.sleep(3)

for x in range(3,5):
    add_connector = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/div/div/ul/li[1]/a')
    add_connector.click()

    time.sleep(2)

    input_bar = supporting_css.exp_wait(driver, By.CLASS_NAME, 'x-form-element').find_element_by_tag_name('input')
    input_bar.click()

    input_bar = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-layer x-combo-list "][1]/div/div[3]')
    input_bar.click()

    time.sleep(2)

    input_bar = driver.find_elements_by_class_name('x-form-element')[1].find_element_by_tag_name('input')
    input_bar.click()

    input_bar.send_keys("pe0" + "0245" + "pr0" + str(x))

    input_bar = driver.find_elements_by_class_name('x-form-element')[2].find_element_by_tag_name('input')
    input_bar.click()

    input_bar.send_keys("root")

    input_bar = driver.find_elements_by_class_name('x-form-element')[3].find_element_by_tag_name('input')
    input_bar.click()

    input_bar.send_keys("D!>!ne@889")

    submit_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window x-resizable-pinned"]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
    submit_button.click()

    time.sleep(2)


config_policy = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[2]/div[2]/div/ul/div/li[3]/ul/li[3]/div/a/span')
config_policy.click()

time.sleep(5)

policy_list = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div').find_elements_by_tag_name('span')

for element in policy_list:
    if element.text == "meh  ESXi Shutdown Policy":
        element.click()
        time.sleep(3)
        break

time.sleep(1)

copy_policy = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/ul/li[4]/a')
copy_policy.click()

time.sleep(1)

input_bar = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window"]/div[2]/div[1]/div/div/div/div/div/form/div[1]/div[1]/input')
input_bar.send_keys("meh " + " " + "ESXi Shutdown Policy")

submit_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window"]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
submit_button.click()

time.sleep(5)

driver.quit()

driver = supporting_css.reload(chrome_options)

action = ActionChains(driver)

config_policy = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[2]/div[2]/div/ul/div/li[3]/ul/li[3]/div/a/span')
config_policy.click()

time.sleep(5)

policy_list = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div').find_elements_by_tag_name('span')

for element in policy_list:
    if element.text == "meh " + "245" + " ESXi Shutdown Policy":
        element.click()
        time.sleep(3)
        break

time.sleep(1)

edit_policy = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/ul/li[2]/a')
edit_policy.click()

time.sleep(1)

button = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window"]/div[2]/div[1]/div/div/div/div/div/form/div[2]/div/div/table/tbody/tr/td[2]/em/button')
button.click()

deselect_one = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/form/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div[1]')
deselect_two = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/form/div/div[3]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[2]/div[2]')

action.key_down(Keys.SHIFT).click(deselect_one).click(deselect_two).key_up(Keys.SHIFT).perform()

deselect_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div/div/table[2]/tbody/tr/td[2]/em/button')
deselect_button.click()

time.sleep(2)
save_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
save_button.click()

time.sleep(1)

submit_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window"]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
submit_button.click()

time.sleep(5)

driver.quit()

driver = supporting_css.reload(chrome_options)

action = ActionChains(driver)

config_policy = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[2]/div[2]/div/ul/div/li[3]/ul/li[3]/div/a/span')
config_policy.click()

time.sleep(5)

policy_list = driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/div').find_elements_by_tag_name('span')

for element in policy_list:
    if element.text == "meh " + "" + " ESXi Shutdown Policy":
        element.click()
        time.sleep(3)
        break

time.sleep(1)

edit_policy = supporting_css.exp_wait(driver, By.XPATH, '/html/body/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/ul/li[2]/a')
edit_policy.click()

time.sleep(1)

button = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window"]/div[2]/div[1]/div/div/div/div/div/form/div[2]/div/div/table/tbody/tr/td[2]/em/button')
button.click()

left_panel_search = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/form/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div')

search_list = left_panel_search.find_elements_by_tag_name('div')
list_length = len(search_list)

for element in search_list:
    if element.text == ("" + "" + ""):
        action.key_down(Keys.SHIFT).click(element).key_up(Keys.SHIFT).perform()
        time.sleep(3)
        break

for element in search_list:
    if element.text == ("" + "" + ""):
        action.key_down(Keys.SHIFT).click(element).key_up(Keys.SHIFT).perform()
        time.sleep(3)
        break

select_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/form/div/div[2]/div/div/table[1]/tbody/tr/td[2]/em/button')
select_button.click()

time.sleep(2)
save_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
save_button.click()

time.sleep(1)

edit_power_source = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window"]/div[2]/div[1]/div/div/div/div/div/form/div[4]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div/div[5]/table/tbody/tr/td[4]/div/img')
edit_power_source.click()

power_source_list = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/form/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[2]/div')
search_list = power_source_list.find_elements_by_tag_name('div')

for element in search_list:
    if element.text == ("" + "" + ""):
        element.click()
        time.sleep(3)
        break

save_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@id="SelectItemsBase-window"]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
save_button.click()

submit_button = supporting_css.exp_wait(driver, By.XPATH, '//*[@class="x-window"]/div[2]/div[1]/div/div/div/div/div/div/div/div/table/tbody/tr/td[1]/table/tbody/tr/td[2]/em/button')
submit_button.click()

time.sleep(5)



