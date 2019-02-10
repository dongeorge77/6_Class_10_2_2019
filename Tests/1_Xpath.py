from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/ADMIN/PycharmProjects/S_Class/drivers/chromedriver.exe")
driver.get("http://www.facebook.com")
driver.maximize_window()
driver.find_element_by_xpath("//input[@data-testid='royal_email']").send_keys("Test")
driver.find_element_by_xpath("//input[@data-testid='royal_pass']").send_keys("12345")
driver.find_element_by_xpath("//a[text()='Forgotten account?']").click()