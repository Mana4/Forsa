from selenium import webdriver
import time

url = 'https://www.for9a.com/en'

usr = 'Abdo.mana75@gmail.com'
pas = '01524505018'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('disable-gpu')
options.add_argument('--disable-notifications')
options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome('chromedriver\\chromedriver.exe',chrome_options= options)

#driver = webdriver.Ie('ieDriver\\IEDriverServer.exe')
driver.maximize_window()


def highlight(element):
    """Highlights a Selenium webdriver element"""
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)

    orignal_style = element.get_attribute('style')
    apply_style("border: 4px solid red")
    if (element.get_attribute("style") != None):
        time.sleep(5)
    apply_style(orignal_style)
