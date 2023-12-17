import time

import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])

# def test_step1():
#     x_selector1 = """//*[@id="login"]/div[1]/label/input"""
#     input1 = site.find_element("xpath", x_selector1)
#     input1.send_keys("1234")
#     x_selector2 = """//*[@id="login"]/div[2]/label/input"""
#     input2 = site.find_element("xpath", x_selector2)
#     input2.send_keys("1234")
#     btn_selector = "button"
#     btn = site.find_element("css", btn_selector)
#     btn.click()
#     x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
#     err_label = site.find_element("xpath", x_selector3)
#     assert err_label.text == "401"

def test_step2():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys("Alena808")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys("gi89mjb90f")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    # x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    # err_label = site.find_element("xpath", x_selector3)
    # assert err_label.text == "401"
    time.sleep(3)

    x_selector1 = """//*[@id="create-btn"]"""
    input1 = site.find_element("xpath", x_selector1)
    input1.click()
    time.sleep(3)

    x_selector1 = """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("OneMoreTestFromPython")
    x_selector2 = """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("DescriptionFromPython")
    x_selector3 = """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
    input3 = site.find_element("xpath", x_selector3)
    input3.send_keys("contentNEWpython")
    time.sleep(3)

    x_selector4 = """//*[@id="create-item"]/div/div/div[7]/div/button/span"""
    input4 = site.find_element("xpath", x_selector4)
    input4.click()
    time.sleep(3)


    x_selector_x = """//*[@id="app"]/main/div/div[1]/h1"""
    text_label = site.find_element("xpath", x_selector_x)
    assert text_label.text == 'OneMoreTestFromPython'
