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
data_path = r'C:\Users\p.kalinchuk\python\work\data\tasks.txt'
result_path = r'C:\Users\p.kalinchuk\python\work\results\tasks_results.txt'

options = Options()
# Для  скрытия браузера передаём параметр "-headless"
options.add_argument("-headless")
path = Service(driver_path)
wd = webdriver.Firefox(service=path, options=options)
wd.implicitly_wait(30)

# Читаем файл со списком номеров задач
with open(data_path, 'r') as f:
    tasks = f.read()

tasks_list = tasks.split()
# Получаем пароль к Jire от пользователя
pass_key = getpass.getpass('\nПароль пользователя Jira: ')
# pass_key = input("\nПароль пользователя Jira: ")

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
        By.XPATH, "//*[@id='login-form-submit']").click()
    print("-"*10 + "\n")
    for i in tasks_list:
        link = ("https://jira.absolutins.ru/browse/"+str(i))
        wd.get(link)
        try:
            type_task = "   Тип: " + \
                wd.find_element(By.XPATH, "//span[@id='type-val']").text
        except NoSuchElementException as e:
            s = str(e)
            if "type-val" in s:
                type_task = '    Тип: -----'
        try:
            status_task = "   Статус: " + \
                wd.find_element(
                    By.XPATH, "//*[@id='opsbar-transitions_more']/span[@class='dropdown-text']").text
        except NoSuchElementException as e:
            s = str(e)
            if "status-val" in s:
                status_task = '    Статус: -----'
        try:
            executor_task = "   Исполнитель: " + \
                wd.find_element(
                    By.XPATH, "//span[@id='assignee-val']").text
        except NoSuchElementException as e:
            s = str(e)
            if "assignee-val" in s:
                executor_task = '    Исполнитель: -----'
        try:
            author_task = "   Автор: " + \
                wd.find_element(
                    By.XPATH, "//span[@id='reporter-val']").text
        except NoSuchElementException as e:
            s = str(e)
            if "reporter-val" in s:
                author_task = '    Автор: -----'
        try:
            tester_task = "   Тестировщик: " + \
                wd.find_element(
                    By.XPATH, "//span[@id='customfield_11200-val']").text
        except NoSuchElementException as e:
            s = str(e)
            if "customfield_11200-val" in s:
                tester_task = '   Тестировщик: -----'
        try:
            title_task = "   Заголовок: " + \
                wd.find_element(
                    By.XPATH, "//h1[@id='summary-val']").text
        except NoSuchElementException as e:
            s = str(e)
            if "summary-val" in s:
                title_task = '    Заголовок: -----'
        try:
            time_task = "   Предварительная оценка: " + \
                wd.find_element(
                    By.XPATH, "//dd[@id='tt_single_values_orig']").get_attribute("innerText")
        except NoSuchElementException as e:
            s = str(e)
            if "tt_single_values_orig" in s:
                title_task = '    Предварительная оценка: -----'
        try:
            time_task_fact = "   Затраченное время: " + \
                wd.find_element(
                    By.XPATH, "//dd[@id='tt_single_values_spent']").get_attribute("innerText")
        except NoSuchElementException as e:
            s = str(e)
            if "tt_single_values_orig" in s:
                title_task = '    Затраченное время: -----'
        try:
            sprint_task = "   В спринте: " + \
                wd.find_element(
                    By.XPATH, "//dd/a[@class='issueaction-greenhopper-rapidboard-operation js-find-on-board-sprint']").get_attribute("innerText")
        except NoSuchElementException as e:
            s = str(e)
            if "issueaction-greenhopper-rapidboard-operation js-find-on-board-sprint" in s:
                sprint_task = '    В спринте: -----'
#      Разблокировать, если надо записывать в файл
        with open(result_path, 'a', encoding="utf-8") as f:
            f.write("\n" + str(i) + "\n" + type_task + "\n" + status_task + "\n" + executor_task + "\n" + author_task +
                    "\n" + tester_task + "\n" + title_task + "\n" + time_task + "\n" + time_task_fact + "\n" + sprint_task + "\n" + link + "\n")
#            print(str(i) + ':    Тестировщик проставлен')
        # Вывод результата в терминал
        # print(str(i) + "\n" + type_task + "\n" + status_task + "\n" + executor_task + "\n" +
        #       author_task + "\n" + tester_task + "\n" + title_task + "\n" + time_task + "\n" + sprint_task + "\n" + link + "\n")
        # print(link + time_task)
    print("-"*10)
except:
    print("Что-то пошло не так :-(")
finally:
    wd.quit()
