from selenium import webdriver

driver = webdriver.Chrome(r'H:\chromedriver.exe')
driver.maximize_window()
driver.get("http://www.seleniumeasy.com/test/basic-first-form-demo.html")
assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title

eleUserMessage = driver.find_element_by_id("user-message")
eleUserMessage.clear()
eleUserMessage.send_keys("Nigger")

eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
eleShowMsgBtn.click()

eleUserMessage = driver.find_element_by_id("sum1")
eleUserMessage.clear()
eleUserMessage.send_keys(15)

eleUserMessage = driver.find_element_by_id("sum2")
eleUserMessage.clear()
eleUserMessage.send_keys(20)

eleShowMsgBtn=driver.find_element_by_css_selector('#gettotal > .btn')
eleShowMsgBtn.click()

eleYourMsg=driver.find_element_by_id("display")
assert "Nigger" in eleYourMsg.text
#driver.close()