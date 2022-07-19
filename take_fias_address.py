from os import path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

driver_path = r'C:\Users\p.kalinchuk\python\work\drivers\geckodriver.exe'

options = Options()
options.headless = True
path = Service(driver_path)
wd = webdriver.Firefox(service=path, options=options)
wd.implicitly_wait(30)

s = []
fias_code = input("\nКод-фиас: ")

try:
    wd.get("https://xn--80ap2aj.xn--80asehdb/" + fias_code)
    fias_address = wd.find_elements(
        By.XPATH, "//li[contains(@class,'breadcrumb-item')]")
    for i in fias_address:
        s.append(i.text)
    s.remove('ФИАС онлайн')
    print("\n")
    print(s)
    print("\n")
finally:
    wd.quit()
