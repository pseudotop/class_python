from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

url = 'http://www.letskorail.com'
driver = webdriver.Chrome('c:\\chromedriver.exe')
driver.get(url)
handles = driver.window_handles
size = len(handles)
#print(size)
main = driver.current_window_handle
for handle in handles:
    if handle != main :
        driver.switch_to.window(handle)
        driver.close()
driver.switch_to.window(main)
#booking = driver.find_element_by_css_selector('img[src*="/images/btn_reserve.gif"]')
booking = driver.find_element_by_css_selector('p.btn_res > a')
booking.click()

# 페이지가 바뀔 때 1초 waiting
driver.implicitly_wait(1)

start = driver.find_element_by_css_selector('#start')
# print(start.get_attribute('value'))
start.clear()
start.send_keys('용산')

get = driver.find_element_by_css_selector('#get')
# print(start.get_attribute('value'))
get.clear()
get.send_keys('부산')

s_year = driver.find_element_by_css_selector('#s_year > option[value="2018"]')
s_year.click()

s_month = driver.find_element_by_css_selector('#s_month > option[value="08"]')
s_month.click()

s_day = driver.find_element_by_css_selector('#s_day > option[value="10"]')
s_day.click()

s_hour = driver.find_element_by_css_selector('#s_hour > option[value="19"]')
s_hour.click()

while True:
    search = driver.find_element_by_css_selector('p.btn_inq > a')
    search.click()

    driver.implicitly_wait(1)

    reservation = driver.find_elements_by_css_selector('img[name="btnRsv2_0"]')
    # print(reservation[0])
    if len(reservation) > 0:
        reservation[0].click()
        break
driver.implicitly_wait(1)

id = '123412345'
pwd = '123415143'

txtMember = driver.find_element_by_css_selector('#txtMember')
txtMember.clear()
txtMember.send_keys(id)

txtPwd = driver.find_element_by_css_selector('#txtPwd')
txtPwd.clear()
txtPwd.send_keys(pwd)

login = driver.find_element_by_css_selector('img[src*="/images/btn_login.gif"]')
login.click()

while True:
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                       'Timed out waiting for PA creation ' +
                                       'confirmation popup to appear.')

        alert = driver.switch_to.alert
        alert.accept()
        print("alert accepted")
    except TimeoutException:
        break