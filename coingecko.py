#Minton CoinGecko Software Test Engineer automation code
'''
Automation coverage - guest journey:
Navigate through a few pages
Searching for a coin
Loop each currency for each language for each coin
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

def top_bar_nagivation():
    driver.find_element(By.LINK_TEXT, 'New Coins').click() #click new coins
    driver.fullscreen_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Gainers & Losers').click() #click gainers and losers
    driver.fullscreen_window()
    time.sleep(2)
    driver.find_element(By.LINK_TEXT, 'Categories').click() #click categories
    driver.fullscreen_window()
    time.sleep(2)

driver_service = Service(executable_path='D:/Chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=driver_service)
driver.get("https://www.coingecko.com/")

driver.fullscreen_window()
time.sleep(2)
currency_symbol_list = []
currency_list = []
coin_name_in_language_list = []
number_of_languages = driver.find_elements(By.XPATH, "//div[@class='tw-flex flex-row']//span[@class='dropdown-item py-2 tw-cursor-pointer']")
print ("Number of languages:", len(number_of_languages))
number_of_currencies = driver.find_elements(By.XPATH, "//div[@class='dropdown-menu dropdown-popup dropdown-menu-content']//span[@class='d-md-inline currency-name']")
print ("Number of currencies:", len(number_of_currencies))

top_bar_nagivation()

list_of_coins = ["bitcoin", "doge"]
for i in range (0, len(list_of_coins)): #2
    coin = list_of_coins[i]
    driver.find_element(By.CLASS_NAME, 'tw-truncate').click() #click search bar
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "input[class='tw-w-full tw-text-sm tw-border-none tw-px-2 tw-py-3 search-input-dark dark:tw-text-white']").send_keys(coin) #input bitcoin
    time.sleep(8)
    driver.find_element(By.CSS_SELECTOR, "input[class='tw-w-full tw-text-sm tw-border-none tw-px-2 tw-py-3 search-input-dark dark:tw-text-white']").send_keys(Keys.RETURN) #press enter
    driver.fullscreen_window()
    for i in range (0, len(number_of_languages)): #34
        driver.find_element(By.CLASS_NAME, 'tw-cursor-pointer').click() # dropdown language
        time.sleep(2)
        driver.find_elements(By.XPATH, "//div[@class='tw-flex flex-row']//span[@class='dropdown-item py-2 tw-cursor-pointer']")[i].click() #click language
        driver.fullscreen_window()
        coin_name_in_language = driver.find_element(By.CSS_SELECTOR, "span[class='tw-text-gray-500 dark:tw-text-white dark:tw-text-opacity-60 tw-text-sm']").get_attribute('innerHTML').encode('utf-8') #encode('iso-8859-1')
        print (coin_name_in_language)
        coin_name_in_language_list.append(coin_name_in_language)
        for i in range (0, len(number_of_currencies)): #61
            driver.find_element(By.ID, 'currency-selector').click() #dropdown currency
            time.sleep(1)
            driver.find_elements(By.XPATH, "//span[@class='d-md-inline currency-name']")[i].click()
            time.sleep(2)
            currency_symbol = driver.find_element(By.XPATH, '//*[@id="general"]/div[1]/div[1]/h1/span').get_attribute('innerHTML').encode('utf-8') #get currency symbol
            currency = driver.find_element(By.XPATH, "//span[@class='no-wrap']").get_attribute('innerHTML').encode('utf-8') #get currency
            currency_symbol_list.append(currency_symbol)
            currency_list.append(currency)
            print (currency)
        print ("List of languages explored for", coin, coin_name_in_language_list)
        coin_name_in_language_list.clear() #

print ("List of currency symbols explored:", set(currency_symbol_list))
print ("List of currencies explored:", currency_list)

driver.quit()