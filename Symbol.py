from selenium import webdriver
from selenium.webdriver.common.by import By
from dbconfig import InsertIntoTable, get_mysql_connection
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
url_1 = config['mysql']['url_1']
url_2 = config['mysql']['url_2']



import time
def insertSymbol():
    options = webdriver.ChromeOptions()
    options.add_argument(f'--remote-debugging-port=9222')
    options.add_argument(f'--user-data-dir=c:\chrome')
    options.add_experimental_option('debuggerAddress', 'localhost:9222')
    driver = webdriver.Chrome(options=options)

    # switch to the tab with the website
    driver.execute_script('window.open("");')
    driver.switch_to.window(driver.window_handles[0])
    driver.get(url_1)
    time.sleep(10)


    class_name = "{c}"
    main_class = driver.find_elements(By.XPATH, f"//*[contains(@class, '{class_name}')]")
    print("main_class",len(main_class))
        
    symbols = []
    for row in main_class:
        symbols.append(tuple([row.get_attribute("id") ,  str(row.find_elements(By.CLASS_NAME, "inst")[0].text) ])) #+ str(inst_element[1].text)))
    #time.sleep(5)
    #===============================================
    db = get_mysql_connection()
    InsertIntoTable( symbols, "symbol")



