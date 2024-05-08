from os import path
import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import getpass
import datetime

driver_path = r'C:\Users\p.kalinchuk\python\work\drivers\geckodriver.exe'

options = Options()
# Для  скрытия браузера передаём параметр "-headless"
options.add_argument("-headless")
path = Service(driver_path)
wd = webdriver.Firefox(service=path, options=options)

kiasrep = "http://mosrepwbs01/FrontSvcRep/"
kiastest = "http://mosrepwbs01/FrontSvcTest/"

kias = input('Введите нужный стенд "rep" или "test": ')

if kias == "rep":
    kias = kiasrep
elif kias == "test":
    kias = kiastest
else:
    print("\nВведён не корректный стенд!\n")
    sys.exit()

try:
    # Получение данных со страницы сайта
    wd.get(kias)
    wd.implicitly_wait(30)
    kiastest_status = "Статус: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr/td[2]").text
    kiastest_condition = "Состояние: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr[2]/td[2]").text
    kiastest_company = "Компания: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr[3]/td[2]").text
    kiastest_license = "Лицензия: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr[4]/td[2]").text
    kiastest_validity = "Срок действия: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr[5]/td[2]").text
    kiastest_web_service_version = "Версия web-сервиса: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr[6]/td[2]").text
    kiastest_environment_version = "Версия для среды: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr[7]/td[2]").text
    kiastest_database_server = "Сервер БД: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr[8]/td[2]").text
    kiastest_file_storage = "Файловое хранилице: " + \
        wd.find_element(
            By.XPATH, "//div[@id='maindiv']/table/tbody/tr[9]/td[2]").text
    wd.quit()
    date = str(datetime.date.today())
    time = str(datetime.time())
    a = str(datetime.datetime.now())
    print("\n" + kias + "\n" + a + "\n" + "-" * 10 + "\n" + kiastest_status + "\n" + kiastest_condition + "\n" +
          kiastest_company + "\n" + kiastest_license + "\n" +
          kiastest_validity + "\n" + kiastest_web_service_version + "\n"
          + kiastest_environment_version + "\n" + kiastest_database_server + "\n" + kiastest_file_storage + "\n")
except (Exception) as err:
    print(err)
