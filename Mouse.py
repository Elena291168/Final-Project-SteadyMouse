import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox(executable_path=r'C:\Users\elena\Downloads\geckodriver-v0.27.0-win64\geckodriver.exe')
driver.get("https://www.steadymouse.com/")


# verify presence of main text and its text "The SteadyMouse Project":
main_text = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(.,"The SteadyMouse Project")]')))
assert main_text.text == "The SteadyMouse Project"


# wait until "purchase" link in the left side bar is visible  verify its text and click on it:
purchase_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/purchase/#buynow")]')))
assert purchase_link.text == "Purchase"
purchase_link.click()


# wait until "buy steady mouse X" button is visible verify its text and click on it:
buy_steady_mouse_x_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(),"Buy SteadyMouse X (All Versions)")]')))
assert buy_steady_mouse_x_btn.text == "Buy SteadyMouse X (All Versions)"
buy_steady_mouse_x_btn.click()

# add the iframe switch to access the pop up window elements:
time.sleep(5)
iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//iframe[@class="gumroad-overlay-iframe"]')))
driver.switch_to.frame(iframe)

# wait until the "price tag" element is visible and verify its text:
price_tag = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="product-price-tag-container"]/h2')))
assert price_tag.text == "$127"

def changeQuantity(quantity_change_XPATH):
    quantity_change_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, quantity_change_XPATH)))
    quantity_change_button.click()

quantity_change_XPATHES = ['//a[contains(text(),"+")]', '//a[contains(text(),"-")]']
for quantity_change_XPATH in quantity_change_XPATHES:
    changeQuantity(quantity_change_XPATH)

def verifyquantity(quantity):
    new_quantity = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//strong[@data-testid="current-quantity"]')))
    assert new_quantity.text == quantity

quantities_increase = ('//a[contains(text(),"+")]', "2")
quantities_decrease = ('//a[contains(text(),"-")]', "1")

quantities = [quantities_increase, quantities_decrease]
for quantity in quantities:
    changeQuantity(quantity[0])
    verifyquantity(quantity[1])



buy_this_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//button[@class="button-primary button-block i_want_this_button"]')))
buy_this_button.click()



# wait until the checkout window pops up and click close "x" button to return to the previous pop up window:
close_button= WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="buy-form-main"]/a/i')))
close_button.click()

# wait until the rating box is visible and click to open its content:
rating_box_btn = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="product-ratings-container js-average-rating-container soft-hidden"]')))
rating_box_btn.click()

# wait until the rating box is opened and verify 5 star has 86% and 4 star has 14%:
def verifyratingtext(rating_element_xpath, rating_element_text):
    rating_element = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, rating_element_xpath)))
    assert rating_element.text == rating_element_text

five_star_rating_element = ('//li[@class="js-rating-percent-container"][1]', "5 star 86%")
four_star_rating_element = ('//li[@class="js-rating-percent-container"][2]', "4 star 14%")

rating_elements = [five_star_rating_element,four_star_rating_element]
for rating_element in rating_elements:
    verifyratingtext(rating_element[0],rating_element[1])

driver.quit()







