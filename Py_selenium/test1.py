# verify that the title name is correct or not

import time

from selenium import webdriver
from typing_extensions import assert_type

def test_page_title():
    driver= webdriver.Chrome()
    driver.get("https://jpetstore.aspectran.com/")

    assert(driver.title == "JPetStore Demo")
    print(driver.title)
    time.sleep(3)

def test_title():
    driver = webdriver.Chrome()
    driver.get("https://jpetstore.aspectran.com/")
    elem_title = driver.find_element("xpath","/html/body/section/div[1]/div[1]/div/div/header/h1")
    assert (elem_title.text == "JPetStore Demo")
    time.sleep(3)
