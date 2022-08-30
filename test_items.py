from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_exist_button_buy(browser):
    browser.get(link)
    assert browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    time.sleep(30)
