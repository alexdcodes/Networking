from selenium import webdriver
import os
import telnetlib
import time

os.system("PATH")

chromedriver = "PATH"
driver = webdriver.Chrome(chromedriver)


ups = open("hosts", "r")
password = "password"


def config_old_card_smtp(t):
    # t = telnetlib.Telnet(hostname)
    # t.read_until(b"Enter Password: ", 5)
    t.write(password.encode('ascii'))
    print("Configuring SMTP server...")
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'1')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'9')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'4')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'1')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'4')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'email')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'2')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'1')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'2')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'\r\n')
    print("Configured SMTP, configuring NTP shortly...")
    time.sleep(2)
    t.write(b'0')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'1')
    t.write(b'\r\n')
    t.write(b'XXXXXXXXXXXX')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'0')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'0')
    t.write(b'\r\n')
    time.sleep(2)


def config_old_card_ntp(t):
    print("Configuring NTP server...")
    t.write(b'1')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'5')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'3')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'XXXXXXXXXXXXXXX')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'7')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'1')
    t.write(b'\r\n')
    time.sleep(2)
    t.write(b'0')
    print("Configured NTP server, exiting shortly...")
    t.close()


def config_email_notifs():
    driver.get("http://username:password@" + host + "/ups_noti.htm")
    element = driver.find_element_by_name('RecipientList')
    for option in element.find_elements_by_tag_name('option'):
        if option.text == 'recipient4@domain.com':
            option.click()
            break

    email_box = driver.find_element_by_name('Receipt')
    email_box.clear()
    email_box.send_keys("email")
    el = driver.find_element_by_name('select1')

    for option in el.find_elements_by_tag_name('option'):
        if option.text == 'Enabled':
            option.click()
            break

    enotify_box = driver.find_element_by_name('enotify')
    enotify_box.click()

    ups_on_battery = driver.find_element_by_name('Evt1')
    ups_on_battery.click()
    ups_ac = driver.find_element_by_name('Evt2')
    ups_ac.click()
    ups_low_battery = driver.find_element_by_name('Evt3')
    ups_low_battery.click()
    battery_faults = driver.find_element_by_name('Evt4')
    battery_faults.click()
    battery_ok = driver.find_element_by_name('Evt5')
    battery_ok.click()
    ups_overload = driver.find_element_by_name('Evt6')
    ups_overload.click()
    ups_return_normal = driver.find_element_by_name('Evt7')
    ups_return_normal.click()
    ups_ok = driver.find_element_by_name('Evt9')
    ups_ok.click()
    ups_comm_failed = driver.find_element_by_name('Evt10')
    ups_comm_failed.click()
    ups_comm = driver.find_element_by_name('Evt11')
    ups_comm.click()

    submit_box = driver.find_element_by_name('Submit')
    submit_box.click()
    driver.switch_to.alert.accept()


def config_smtp_server():
    driver.get("http://username:password@" + host + "/set_net.htm")
    smtp = driver.find_element_by_name('SMTPserver')
    smtp.clear()
    smtp.send_keys('10.62.188.30')
    submit_box = driver.find_element_by_name('Submit')
    submit_box.click()
    driver.switch_to.alert.accept()


def config_ntp():
    driver.get("http://username:password@" + host + "/set_time.htm")
    driver.find_element_by_css_selector("input[type='radio'][VALUE='3']").click()
    ntp = driver.find_element_by_name('IpAddress')
    ntp.clear()
    ntp.send_keys('162.53.5.166')
    element = driver.find_element_by_name('TimeZone')
    for option in element.find_elements_by_tag_name('option'):
        if option.text == '(GMT-05:00) Bogota, Lima, Quito, Eastern TIME (US & Canada)':
            option.click()
            break
    submit_button = driver.find_element_by_name('Submit')
    submit_button.click()
    driver.switch_to.alert.accept()


def select_card(hostname):
    driver.get("http://username:password@" + hostname)
    meta_tag = driver.find_element_by_tag_name('meta').get_attribute('content')
    print("Connecting to host @ " + hostname)
    compare = meta_tag.split()
    compare2 = compare[1]
    if "utf-8" in compare2:
        print("New firmware found, running necessary configuration")
        config_email_notifs()
        config_smtp_server()
        config_ntp()
    elif "next.htm" in compare2:
        print("Old firmware found, running necessary configuration")
        t = telnetlib.Telnet(hostname)
        config_old_card_smtp(t)
        config_old_card_ntp(t)


def reboot_new_card():
    driver.get("http://username:password@" + host + "/set_sys.htm")
    driver.find_element_by_css_selector("input[type='SUBMIT'][VALUE='Reset Communication']").click()
    driver.switch_to.alert.accept()


for line in ups:
    host = line.strip()
    select_card(host)