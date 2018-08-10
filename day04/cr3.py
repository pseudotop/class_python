from selenium import webdriver

url = 'http://www.naver.com'
driver = webdriver.Chrome('c:\\chromedriver.exe')
driver.get(url)
#driver.save_screenshot('naver.png')

login_btn = driver.find_element_by_css_selector('i.ico_local_login')
print(login_btn.text)
login_btn.click()
id = driver.find_element_by_css_selector('input#id.int')
pw = driver.find_element_by_css_selector('input#pw.int')
print('id:',id.send_keys('lsupertopl'),'pw:',pw.send_keys('1111'))
