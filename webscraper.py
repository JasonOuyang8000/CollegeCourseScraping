## Script to acccess College Categoriescl
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import string

driver = webdriver.Chrome(r"./driver/chromedriver")
driver.get("https://mycollege-guest.laccd.edu/psc/classsearchguest/EMPLOYEE/HRMS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL?Campus=ELAC&strm=2232")
driver.maximize_window()

## Access Courses Category
button = driver.find_element(By.NAME, "CLASS_SRCH_WRK2_SSR_PB_SUBJ_SRCH$0")
button.click()
driver.implicitly_wait(5)
totalElements = []
for i in string.ascii_uppercase:
    time.sleep(5)
    element = driver.find_element(By.LINK_TEXT, i)
    element.click()
    elements = driver.find_elements(By.CSS_SELECTOR, "[id^=SUBJECT_TBL_DESCRFORMAL]")
    for x in elements:
        print(x.text)


