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

# Читаем файл со списком номеров задач
with open('tasks.txt', 'r') as f:
    tasks = f.read()

tasks_list = tasks.split()
# Получаем пароль к Jire от пользователя
pass_key = getpass.getpass('\nПароль пользователя Jira: ')

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
    for i in tasks_list:
        try:
            print(str(i))
            wd.get("https://jira.absolutins.ru/browse/"+str(i))
            type_task = "   Тип: " + \
                wd.find_element(By.XPATH, "//span[@id='type-val']").text
            status_task = "   Статус: " + \
                wd.find_element(By.XPATH, "//span[@id='status-val']").text
            executor_task = "   Исполнитель: " + \
                wd.find_element(
                    By.XPATH, "//span[@id='assignee-val']").text
            author_task = "   Автор: " + \
                wd.find_element(
                    By.XPATH, "//span[@id='reporter-val']").text
            tester_task = "   Тестировщик: " + \
                wd.find_element(
                    By.XPATH, "//span[@id='customfield_11200-val']").text
            # Разблокировать, если надо записывать в файл
            # with open('result.txt', 'a', encoding="utf-8") as f:
            # f.write(str(i) + "\n" + status_task + "\n" +
            # executor_task + "\n" + author_task + "\n")
            print(type_task + "\n" + status_task + "\n" + executor_task + "\n" +
                  author_task + "\n" + tester_task + "\n")
        except NoSuchElementException as e:
            s = str(e)
            if "type-val" in s:
                status_task = '    Тип: -----'
            elif "status-val" in s:
                status_task = '    Статус: -----'
            elif "assignee-val" in s:
                executor_task = '    Исполнитель: -----'
            elif "reporter-val" in s:
                author_task = '    Автор: -----'
            elif "customfield_11200-val" in s:
                tester_task = '   Тестировщик: -----'
            else:
                print('Ни один из запрошенных элементов не найден !!!')
            print(type_task + "\n" + status_task + "\n" + executor_task + "\n" +
                  author_task + "\n" + tester_task + "\n")
    print("-"*10)
# except:
#    print("Error")
finally:
    wd.quit()
