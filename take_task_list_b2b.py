from cmath import e
from os import path
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import getpass

driver_path = r'C:\Users\p.kalinchuk\python\work\drivers\geckodriver.exe'

options = Options()
options.headless = True
path = Service(driver_path)
wd = webdriver.Firefox(service=path, options=options)
wd.implicitly_wait(30)

# Создаём пустой список
take_list = []
count_tasks = 0

# Получаем пароль к Jire от пользователя при этом скрываем вводимое
pass_key = getpass.getpass('\nПароль пользователя Jira: ')

# Выбираем из какого фильтра брать задачи
source_list = input(
    "\nВыберите откуда брать задачи: \n 1 - задачи в тестировании\n 2 - задачи в планировании\nВыбран номер: ")
if source_list == "1":
    source_list = "https://jira.absolutins.ru/issues/?filter=12239"
if source_list == "2":
    source_list = "https://jira.absolutins.ru/issues/?filter=12912"

# Авторизовываемся в Jira
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
 # Переходим на страницу фильтра со списком задач  В2В Моторы готовые к тестированию
    wd.get(source_list)
# Собираем номера задач со страницы фильтра
    try:
        a = wd.find_elements(
            By.XPATH, '//td[@class="issuekey"]')
# Записываем полученные номера задач в список take_list
        for i in a:
            take_list.append(i.text)
            count_tasks += 1
# Разбираем созданный список задач для более удобного восприятия
        take_list = map(lambda x: x + '\n', take_list)
# Записываем разобранный список задач в файл
        with open('tasks.txt', 'w') as f:
            f.writelines(take_list)
        print('Количество задач: ' + str(count_tasks) +
              '\nНомера задач записаны в файл \'tasks.txt\'\n')
# Обработка исключений (ошибок при выполнении)
    except:
        print('Что-то пошло не так в блоке создания файла')
# Обработка исключений (ошибок при выполнении)
except:
    print("Что-то пошло не так :-(\n")
# Завершаем работу скрипта
finally:
    wd.quit()
