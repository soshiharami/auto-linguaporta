from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# Seleniumをあらゆる環境で起動させるChromeオプション
options = Options()
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');

DRIVER_PATH = 'chromedriver.exe'

# ブラウザの起動
driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)


url = 'https://w5.linguaporta.jp/user/seibido/index.php'
driver.get(url)
selector = '#content-login > form > table > tbody > tr:nth-child(1) > td > input[type=text]'
element = driver.find_element_by_css_selector(selector)
element.send_keys('j19420')

selector = '#content-login > form > table > tbody > tr:nth-child(2) > td > input[type=password]'
element = driver.find_element_by_css_selector(selector)
element.send_keys('12345678')

selector = '#btn-login'
element = driver.find_element_by_css_selector(selector)
element.click()

selector = '#menu > ul > li:nth-child(2) > form > a'
element = driver.find_element_by_css_selector(selector)
element.click()

time.sleep(1)
selector = '//*[@id="content-study"]/form/div/div[2]/div[3]/input'
element = driver.find_element(By.XPATH, selector)
element.click()

selector = '#content-study > div.pagination.unit_list_page > a:nth-child(21)'
element = driver.find_element_by_css_selector(selector)
element.click()

selector = '#content-study > div.pagination.unit_list_page > a:nth-child(6)'
element = driver.find_element_by_css_selector(selector)
element.click()

time.sleep(0.1)
selector = '//*[@id="content-study"]/div[1]/div[10]/div[1]/div/input'
element = driver.find_element(By.XPATH, selector)
driver.execute_script("arguments[0].click();", element)

SUCCESS = False
while True:
    SUCCESS = False
    while SUCCESS == False:
        try :
            time.sleep(0.5)
            selector = '//*[@id="answer_0_0"]'
            element = driver.find_element(By.XPATH, selector)
            element.click()

            selector = '//*[@id="ans_submit"]'
            element = driver.find_element(By.XPATH, selector)
            element.click()

            time.sleep(0.5)
            selector = '//*[@id="under_area"]/form[2]/input[1]'
            element = driver.find_element(By.XPATH, selector)
            element.click()
        except :
            time.sleep(0.5)
            selector = '//*[@id="under_area"]/form/input[1]'
            element = driver.find_element(By.XPATH, selector)
            element.click()
            SUCCESS = True
