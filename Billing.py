from selenium import webdriver
import time

driver = webdriver.Chrome(r'H:\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.saintalfred.com/collections/brands/products/raceway-snapback-cap-ss20")
assert "RACEWAY SNAPBACK CAP SU20" in driver.title


eleShowMsgBtn=driver.find_element_by_class_name('add-to-cart')
eleShowMsgBtn.click()
time.sleep(2)
driver.get("https://www.saintalfred.com/cart")

eleShowMsgBtn=driver.find_element_by_id('shipping-warning')
eleShowMsgBtn.click()

driver.get("https://www.saintalfred.com/checkout")


with open(r'C:\Users\anees\Desktop\DoogBot\Billing Profile.txt', 'r') as reader:
    email = reader.readline(25)
    nameF = reader.readline(15)
    nameL = reader.readline(15)
    addy = reader.readline(50)
    city = reader.readline(20)
    zip = reader.readline(5)
    CCnumber = reader.readline(16)
    CCname = reader.readline(50)
    exp = reader.readline(4)
    cvv = reader.readline(4)

    reader.close()

    eleUserMessage = driver.find_element_by_id("checkout_email")
    eleUserMessage.send_keys(email.rstrip())
    time.sleep(1)

    eleShowMsgBtn = driver.find_element_by_id('checkout_buyer_accepts_marketing')
    eleShowMsgBtn.click()
    time.sleep(1)

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_first_name")
    eleUserMessage.send_keys(nameF.rstrip())
    time.sleep(1)

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_last_name")
    eleUserMessage.send_keys(nameL.rstrip())
    time.sleep(1)

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_address1")
    eleUserMessage.send_keys(addy.rstrip())
    time.sleep(1)

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_city")
    eleUserMessage.send_keys(city.rstrip())
    time.sleep(1)

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_zip")
    eleUserMessage.send_keys(zip.rstrip())
    time.sleep(1)

eleShowMsgBtn = driver.find_element_by_id('continue_button')
eleShowMsgBtn.click()

time.sleep(10)

pageRN = driver.current_url
nextStep = pageRN[0:93]
payment = nextStep + "shipping_method&step=payment_method"
driver.get(payment)
time.sleep(2)

eleUserMessage = driver.find_element_by_xpath("//html/body/form/input[1]")
eleUserMessage.send_keys(CCnumber.rstrip())
time.sleep(1)

eleUserMessage = driver.find_element_by_id('name')
eleUserMessage.send_keys(CCname.rstrip())
time.sleep(1)

eleUserMessage = driver.find_element_by_id("expiry")
eleUserMessage.send_keys(exp.rstrip())
time.sleep(1)

eleUserMessage = driver.find_element_by_id('verification_value')
eleUserMessage.send_keys(cvv.rstrip())
time.sleep(1)