from os import path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import getpass
# import datetime
# import time
# import json

driver_path = r'C:\Users\p.kalinchuk\python\work\drivers\geckodriver.exe'

options = Options()
options.headless = True
path = Service(driver_path)
wd = webdriver.Firefox(service=path, options=options)
wd.implicitly_wait(30)

# Получаем пароль к Jire от пользователя
pass_key = getpass.getpass('\nПароль пользователя Jira: ')
#pass_key = input("\nПароль пользователя Jira: ")

try:
    wd.get("https://jira.absolutins.ru/login.jsp?os_destination=%2Flogin.jsp")
    wd.find_element(
        By.XPATH, "//input[@id='login-form-username']").click()
    wd.find_element(
        By.XPATH, "//input[@id='login-form-username']").clear()
    wd.find_element(
        By.XPATH, "//input[@id='login-form-username']").send_keys('p.kalinchuk')
    wd.find_element(
        By.XPATH, "//input[@id='login-form-password']").click()
    wd.find_element(
        By.XPATH, "//input[@id='login-form-password']").clear()
    wd.find_element(
        By.XPATH, "//input[@id='login-form-password']").send_keys(pass_key)
    wd.find_element(
        By.XPATH, "//input[@id='login-form-submit']").click()
    print("-"*10 + "\n")
    wd.get("https://jira.absolutins.ru/issues/?filter=12451")
    try:
        a = wd.find_elements(
            By.XPATH, '//td[@class="issuekey"]')
#        a = wd.find_element(
#            By.XPATH, '//td[@class="issuekey"]').text
#        print(a)
#        a = wd.find_elements(
#            By.XPATH, "//*[contains(@id, 'issuerow')]")
        for i in a:
            print(i.text)
    except:
        b = 'test'
except:
    print("Что-то пошло не так :-(\n")
finally:
    wd.quit()
