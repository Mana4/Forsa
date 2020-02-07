from config import *
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys


accounts_name = []
Links = []
# counter = 1

def login(web_url, usr, pas):
    driver.get(web_url)
    login_btn = driver.find_element_by_xpath('//a[contains(text(), "Login")]')
    login_btn.click()
    usr_field = driver.find_element_by_name('email')
    usr_field.send_keys(usr)
    pass_field = driver.find_element_by_name('password')
    pass_field.send_keys(pas)
    login_btn = driver.find_element_by_id('loginBtn')
    login_btn.click()

def scroll_Down_to_end():
    SCROLL_PAUSE_TIME = 0.5

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def scroll_Down_to_Browse_More():

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Browse More")]')))
    except:
        scroll_Down_to_end()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(), "Browse More")]')))
    browse_More = driver.find_element_by_xpath('//button[contains(text(), "Browse More")]')
    browse_More.send_keys(Keys.ENTER)
    scroll_Down_to_end()


def scrap_forsa_data():

    content = driver.page_source
    soup = BeautifulSoup(content,'html.parser')
    scholarships = soup.findAll('div', attrs={'ng-repeat':'opportunity in opportunities'})
    for div in scholarships:
        name = div.find('img', attrs={'class':'opp-image card-img-top ng-hide'})
        link = div.find('a', attrs={'class':'imCont'})
        accounts_name.append(name.get('alt'))
        Links.append(link.get('href'))
    print(len(Links))
    print(len(accounts_name))


    #counter = 1
    # workbook = load_workbook(filename="result.xlsx")
    # sheet = workbook.active
    # for name in accounts_name:
    #     account_name_cell = sheet.cell(row=counter, column=1)
    #     account_name_cell.value = name
    #     counter = counter + 1
    # counter = 1
    # for Link in Links:
    #     comment_cell = sheet.cell(row = counter, column=2)
    #     comment_cell.value = Link
    #     counter = counter+1
    # workbook.save(filename="result.xlsx")
def save_close(title_of_sch,Link_of_sch):
    driver.close()
    df = pd.DataFrame({'Name':title_of_sch,'Link':Link_of_sch})
    df.to_excel('Result.xlsx', index=False, encoding='utf-8')


