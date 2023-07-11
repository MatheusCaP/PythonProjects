from selenium import webdriver

driver = webdriver.Chrome(executable_path="~/usr/local/bin$ ")
driver.get("http://www.google.com.br")
driver.find_element_by_name("q").send_keys("´Matheus cardoso")
  