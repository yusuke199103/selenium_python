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

main_url_links = "main urls"

user_name = ""
user_post_address = ""
user_address_info = ""
user_prefect_info = ""
user_city_info = ""
user_direct_address = ""
user_tel_num = ""
user_other_text_info = ""

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

def strip_direct_address(address_str):
    prefect_array = set("北海道", "青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県", "茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都", "神奈川県", "新潟県", "富山県", "石川県", "福井県", "山梨県", "長野県", "岐阜県", "静岡県", "愛知県", "三重県", "滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県", "鳥取県", "島根県", "岡山県", "広島県", "山口県", "徳島県", "香川県", "愛媛県", "高知県", "福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県", "鹿児島県", "沖縄県")
    city_array = set("市", "町", "村", "郡")
    for pref_val in prefect_array:
        if address_str.find(pref_val) > -1:
            prefect_info = pref_val
            break
    for city_val in city_array:
        if address_str.find(city_val) > -1:
            city_info = city_val
            break
    direct_address = address_str.lstrip(prefect_info)
    direct_address = direct_address.lstrip(city_info)
    return direct_address

def remake_direct_address(direct_address_str):
    number_array = set("一", "二", "三", "四", "五", "六", "七", "八", "九", "十")
    number_count_val = 1
    for number_val in number_array:
        return_address_info = direct_address_str.replace(number_val, number_count_val)
        number_count_val=+1
    return return_address_info

def strip_organization_func(organization_str):
    organization_array = set("organization_str")
    for organization_val in organization_array:
        if organization_str.find(organization_val) > -1:
            ret_organization_name = organization_str.lstrip(organization_val)
            break
    return ret_organization_name

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
    util_func(driver, u_struct)
    
def util_func(driver, u_struct):
    driver.get(main_url_links)
    wait = WebDriverWait(driver, 10)
    element = wait.until(expected_conditions.presence_of_element_located((By.ID, "phSearchInput")))
    element.send_keys(u_struct.company_name)
    element.send_keys(Keys.ENTER)
    sleep(5)
    page_source = driver.page_source
    html_str = BeautifulSoup(page_source, 'html.parser')
    if page_source.find("not found") > -1:
            print("not found!")
            driver.close()
            driver.quit()
            sys.exit(0)
    driver.find_element_by_id("element name").click()
    cur_url = driver.current_url
    driver.get(cur_url)
    driver.implicitly_wait(5)
    url_list = []
    for tr_element in driver.find_elements_by_tag_name("TR"):
        try:
            for ancher_value in tr_element.find_elements_by_tag_name("A"):
                try:
                    if len(ancher_value.get_attribute("href")) <= 70 and ancher_value.get_attribute("href").find("main urls") >=0:
                        url_list.append(ancher_value.get_attribute("href"))
                except:
                    i = 0
        except:
            i = 0
    for url_cnt in url_list:
        driver.get(url_cnt)
        value_ret = get_customer_info(driver)
        print(value_ret)
    print("verifyed")
    driver.close()
    driver.quit()

def get_customer_info(driver_obj):
    elm_flag = False
    for td_elm in driver_obj.find_elements_by_class_name("pbBody"):
        try:
            for datacol_elm in td_elm.find_elements_by_tag_name("TD"):
                try:
                    if elm_flag == True:
                        return datacol_elm.text
                    if datacol_elm.text == "category name":
                        elm_flag = True
                except:
                    i = 0
        except:
            i = 0

def ietest():
    u_struct = input_user()
    u_struct.company_name = ""
    u_struct.post_address = ""
    u_struct.address_info = ""
    u_struct.prefect_info = ""
    u_struct.city_info = ""
    u_struct.direct_address = ""
    u_struct.tel_num = ""
    u_struct.other_text_info = ""
    iedriver = webdriver.Ie("./IEDriverServer.exe")
    util_func(iedriver, u_struct)
    
if __name__ == '__main__':
    #chrometest()
    ietest()
