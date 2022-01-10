from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
# для скрытия браузера
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
import datetime

driver_path = r'drivers/chromedriver.exe'

#  4 строки для выполнения "без запуска" браузера
ua = dict(DesiredCapabilities.CHROME)
options = Options()
options.page_load_strategy = 'normal'
options.add_argument('headless')
path = Service(driver_path)
wd = webdriver.Chrome(service=path, options=options)

# Получение данных со страницы сайта
# wd = webdriver.Chrome(executable_path=driver_path)
wd.implicitly_wait(30)
wd.get("http://mosrepwbs01/FrontSvcTest/")
kiastest_status = "Статус: " + \
    wd.find_element(By.XPATH, "//div[@id='maindiv']/table/tbody/tr/td[2]").text
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
print("\n" + "КИАСТЕСТ" + "\n" + a + "\n" + "-" * 10 + "\n" + kiastest_status + "\n" + kiastest_condition + "\n" +
      kiastest_company + "\n" + kiastest_license + "\n" +
      kiastest_validity + "\n" + kiastest_web_service_version + "\n"
      + kiastest_environment_version + "\n" + kiastest_database_server + "\n" + kiastest_file_storage + "\n")
