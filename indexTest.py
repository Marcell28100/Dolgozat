# imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
# set driver
driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5500/index.html")
# functions

# test1: dupla kattintás után szerepel-e az "animation" class
def test1():
    time.sleep(1)
    elementOne = driver.find_element(By.ID, value = "element-one")
    webdriver.ActionChains(driver).double_click(elementOne).perform()
    assert "animation" in elementOne.get_attribute("class")
    
driver.save_screenshot("test1.png")
test1()

# ha rámegy az egér, utána létezik-e box-shadow
def test2():
    time.sleep(1)
    elementTwo = driver.find_element(By.ID, value = "element-two")
    webdriver.ActionChains(driver).move_to_element(elementTwo).perform()
    assert "box-shadow" in elementTwo.get_attribute("style")

driver.save_screenshot("test2.png")
test2()

# kattintás után eltűnik-e
def test3():
    time.sleep(1)
    elementThree = driver.find_element(By.ID, value = "element-three")
    elementThree.click()
    assert "hidden" in elementThree.get_attribute("class")

driver.save_screenshot("test3.png")
test3()

# kattintás után a háttere zöld lesz-e
def test4():
    time.sleep(1)
    elementFour = driver.find_element(By.ID, value = "element-four")
    elementFour.click()
    assert "green" in elementFour.get_attribute("style")

driver.save_screenshot("test4.png")
test4()

# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)
def test5():
    time.sleep(1)
    elementFour = driver.find_element(By.ID, value = "element-four")

driver.save_screenshot("test5.png")
test5()