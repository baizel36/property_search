import random
from bs4 import BeautifulSoup
import webbrowser
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time
from fake_useragent import UserAgent

##############################User Defined Variables#####################################
zip_codes = ['26187', '26101', '26105']
houses_file = "/home/db/zillow_houses.txt"
path_executable = r'/home/db/Python_Projects/webscraper/selenium-firefox/drivers/geckodriver'
##########################################################################################

xpath = '/html/body/div[1]/div[5]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button[2]'
xpath2 = '/html/body/div[1]/div[5]/div/div/div[1]/div[1]/div[1]/div/div[1]/div/button[1]'
for_sale_by_owner = True

def search_zillow(list:zip_codes, boolean:for_sale_by_owner):
    for i in zip_codes:
        sleep_ = random.randrange(2, 5)
        time.sleep(sleep_)
        user_agent = ua.random
        options = Options()
        options.add_argument(f'user-agent=[{user_agent}]')
        options.headless = True
        driver = webdriver.Firefox(options=options, executable_path=path_executable)
        try:
            url = f'https://www.zillow.com/homes/{i}_rb/'
            website = driver.get(url)
            if for_sale_by_owner:
                button = driver.find_element_by_xpath(xpath2)
                button.click()
            elif not for_sale_by_owner:    
                button = driver.find_element_by_xpath(xpath)
                button.click()
            time.sleep(sleep_)
            soup = BeautifulSoup(driver.page_source, 'lxml')
            on_sale = soup.find_all(class_='list-card-info')
            for x in on_sale:
                try:
                    sale_url = (x.a.get('href'))
                    price = x.find(class_='list-card-price').contents[0]
                    address = x.find(class_='list-card-addr').contents[0]
                    entry = str(price) + ":" + str(address)
                    if i in sale_url and entry not in old_list and entry not in new_houses:
                        new_houses.append(entry)
                        webbrowser.open(sale_url)
                except AttributeError as error:
                    pass
            driver.quit()
        except AttributeError as error:
            print(error)
            print(i, url)

ua = UserAgent(use_cache_server=True)
old_list = []
new_houses = []

with open(houses_file, "r") as z:
    content = z.readlines()
    old_list = [n.strip("\n") for n in content]

search_zillow(zip_codes, for_sale_by_owner)
for_sale_by_owner = False
search_zillow(zip_codes, for_sale_by_owner)

if new_houses:
    with open(houses_file, "a") as z:
        for x in new_houses:
            z.write(str(x) + "\n")
else:
    print("Sorry, there are no new listings today")

