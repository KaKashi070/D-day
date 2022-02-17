from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

uname = "120081038"
pwd = "kkwagh"
npwd = "abcd12345"

url  = "https://192.168.3.254:8443/userportal/webpages/myaccount/login.jsp"


chrome_options = Options()
# chrome_options.add_argument()
driver = webdriver.Chrome("D:\D-Day\chromedriver")
driver.get(url)

driver.find_element_by_id("details-button").click()
driver.find_element_by_id("proceed-link").click()
driver.find_element_by_id("username").send_keys(uname)
driver.find_element_by_id("password").send_keys(pwd)
driver.find_element_by_name("loginbutton").click()

time.sleep(5)

driver.find_element_by_id("mymenu_menu0_1").click()
driver.find_element_by_id("mymenu_menu0_1_0").click()
time.sleep(5)

driver.find_element_by_name("oldpasswd").send_keys(pwd)
driver.find_element_by_id("passwordpasswd").send_keys(npwd)
driver.find_element_by_id("confirmpasswordpasswd").send_keys(npwd)
driver.find_element_by_css_selector(".cp-wrapper .cp-btn, .cp-wrapper input[type=\"button\"]").click()


#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.LINK_TEXT, "Change password"))
# )
#
# finally:

#
#




print("done")