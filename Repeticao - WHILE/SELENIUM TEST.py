import os
import selenium.webdriver as webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

firefox = webdriver.Firefox(executable_path=r"C:\Users\theus\Downloads\GECKODRIVER")
firefox.get('https://google.com.br')



