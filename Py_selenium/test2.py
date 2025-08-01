import time

from selenium import webdriver
from typing_extensions import assert_type

def test_search():
    driver = webdriver.Chrome()
    driver.get("https://jpetstore.aspectran.com/")
    elem_search_box = driver.find_element("xpath" , "/html/body/section/div[2]/div[1]/div[2]/div/form/div/input")
    elem_search_box.click()

    elem_search_box.send_keys("dog")
    elem_search_btn = driver.find_element("xpath" , "/html/body/section/div[2]/div[1]/div[2]/div/form/div/div/button")
    elem_search_btn.click()

    driver.execute_script("window.scrollBy(0,500);")

    elem_search_res = driver.find_element("xpath" , "/html/body/section/div[2]/div[2]/div[2]/table/tbody/tr[2]/td[2]")
    assert (elem_search_res.text == "Bulldog")
    time.sleep(5)

