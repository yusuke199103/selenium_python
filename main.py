from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import sys

main_url_links = "url of main-page"

class input_user:
    company_name = ""
    post_address = ""
    address_info = ""
    prefect_info = ""
    city_info = ""
    direct_address = ""
    tel_num = ""
    other_text_info = ""

class sf_serch_list:
    company_name = ""
    address_info1 = ""
    address_info2 = ""
    tel_num = ""
    facility_type = ""
    url_info = ""

#sf_user_struct
class sf_user_struct:
    organization_type = ""
    company_name = ""
    post_address = ""
    global_address_info = ""
    country_address = ""
    prefect_address = ""
    city_address = ""
    fine_address = ""
    modern_address = ""
    tel_num = ""
    facility_type = ""
    introduct_status = ""
    maker_name = ""

def chrometest():
    u_struct = input_user()
    u_struct.company_name = ""
    u_struct.post_address = ""
    u_struct.address_info = ""
    u_struct.prefect_info = ""
    u_struct.city_info = ""
    u_struct.direct_address = ""
    u_struct.tel_num = ""
    u_struct.other_text_info = ""
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(main_url_links)
    wait = WebDriverWait(driver, 10)
    element = wait.until(expected_conditions.presence_of_element_located((By.ID, "input id")))
    element.send_keys(u_struct.company_name)
    element.send_keys(Keys.ENTER)
    page_source = driver.page_source
    html_str = BeautifulSoup(page_source, 'html.parser')
    if page_source.find("not found message") > -1:
            sys.exit(0)
    driver.find_element_by_id("click ids").click()
    cur_url = driver.current_url
    driver.get(cur_url)
    driver.implicitly_wait(10)
    for ancher_value in driver.find_elements_by_tag_name("A"):
        try:
            print(ancher_value.text)
        except:
            i = 1
    driver.close()
    driver.quit()

def ietest():
    driver = webdriver.Ie("./IEDriverServer.exe")
    driver.get(main_url_links)
    sleep(1)
    wait = WebDriverWait(driver, 10)
    element = wait.until(expected_conditions.presence_of_element_located((By.ID, "input id")))
    element.send_keys("test")
    element.send_keys(Keys.ENTER)
    
if __name__ == '__main__':
    chrometest()
    #ietest()
