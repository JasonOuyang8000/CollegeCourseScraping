## Script to acccess College Categoriescl
from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver = webdriver.Chrome(r"./driver/chromedriver")
driver.get("https://mycollege-guest.laccd.edu/psc/classsearchguest/EMPLOYEE/HRMS/c/COMMUNITY_ACCESS.CLASS_SEARCH.GBL?Campus=ELAC&strm=2232")
driver.maximize_window()

## Access Courses Category
button = driver.find_element(By.NAME, "CLASS_SRCH_WRK2_SSR_PB_SUBJ_SRCH$0")
button.click()
time.sleep(10)
