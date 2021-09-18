# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

# Start the browser and login with standard_user
def login (driver, user, password):
    print ('Starting the browser...')
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'
    print('Login succeeded')

def add_items (driver):
    names = []
    print('Adding items...')
    items = driver.find_elements_by_class_name('inventory_item')
    for item in items:
        name = item.find_element_by_class_name('inventory_item_name').text
        names.append(name)
        item.find_element_by_class_name('btn_inventory').click()
        print('Added item to cart: {}'.format(name))

    cart_badge = driver.find_element_by_class_name('shopping_cart_badge')
    assert len(items) == int(cart_badge.text)

    driver.find_element_by_class_name('shopping_cart_link').click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    cart_items = driver.find_elements_by_class_name('inventory_item_name')
    for item in cart_items:
        assert item.text in names
    print('Adding items succeeded')

def remove_items (driver):
    print('Removing items...')
    driver.find_element_by_class_name('shopping_cart_link').click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'
    cart_items = driver.find_elements_by_class_name('cart_item')
    for item in cart_items:
        name = item.find_element_by_class_name('inventory_item_name').text
        print('Removing item: {}'.format(name))
        item.find_element_by_class_name('cart_button').click()

    num_items = len(driver.find_elements_by_class_name('cart_item'))
    assert num_items == 0
    cart_badge = driver.find_elements_by_class_name('shopping_cart_badge')
    assert len(cart_badge) == 0
    print('Removing items succeeded')

# driver = webdriver.Chrome()
# --uncomment when running in Azure DevOps.
options = ChromeOptions()
options.add_argument("--headless") 
driver = webdriver.Chrome(options=options)

login(driver, 'standard_user', 'secret_sauce')
add_items(driver)
remove_items(driver)

print('Tests complete')
driver.quit()
