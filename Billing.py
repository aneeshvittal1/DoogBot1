from selenium import webdriver

driver = webdriver.Chrome(r'H:\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.saintalfred.com/collections/brands/products/raceway-snapback-cap-ss20")
assert "RACEWAY SNAPBACK CAP SU20" in driver.title


eleShowMsgBtn=driver.find_element_by_class_name('add-to-cart')
eleShowMsgBtn.click()
driver.implicitly_wait(500)
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

    eleUserMessage = driver.find_element_by_id("checkout_email")
    eleUserMessage.clear()
    eleUserMessage.send_keys(email)

    eleShowMsgBtn = driver.find_element_by_id('checkout_buyer_accepts_marketing')
    eleShowMsgBtn.click()

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_first_name")
    eleUserMessage.clear()
    eleUserMessage.send_keys(nameF)

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_last_name")
    eleUserMessage.clear()
    eleUserMessage.send_keys(nameL)

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_address1")
    eleUserMessage.clear()
    eleUserMessage.send_keys(addy)

    eleUserMessage = driver.find_element_by_id("checkout_shipping_address_city")
    eleUserMessage.clear()
    eleUserMessage.send_keys(city)

    eleUserMessage = driver.find_element_by_class_name('field__input field__input--zip')
    eleUserMessage.clear()
    eleUserMessage.send_keys(zip)
