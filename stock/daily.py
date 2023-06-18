from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import datetime
from dbconfig import InsertIntoTable, get_mysql_connection

def insertSymbolDaily():
    options = webdriver.ChromeOptions()
    options.add_argument(f'--remote-debugging-port=9222')
    options.add_argument(f'--user-data-dir=c:\chrome')
    options.add_experimental_option('debuggerAddress', 'localhost:9222')
    driver = webdriver.Chrome(options=options)

    # switch to the tab with the website
    driver.execute_script('window.open("");')
    driver.switch_to.window(driver.window_handles[0])

    
    k=1
    _datefinish=datetime.time(12, 30)
    while True:  # loop indefinitely
        class_name = "{c}"
        main_class = driver.find_elements(By.XPATH, f"//*[contains(@class, '{class_name}')]")
        print("main_class",len(main_class))
        ids = [el.get_attribute("id") for el in main_class]
        #====================== for new Symbol first insert into symbol table 
        """
        symbols = []
        for row in main_class:
            symbols.append(tuple([row.get_attribute("id") ,  str(row.find_elements(By.CLASS_NAME, "inst")[0].text) ])) #+ str(inst_element[1].text)))
        #time.sleep(5)
        InsertIntoTable(symbols,"symbol")
        """
        #===============================================
        time.sleep(5)
        #===============================================
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        #=============================================== _cfield2 it is ok 
        class_name = "t0c ch{_cfield1}"
        inner_class = soup.find_all('div', class_=class_name)
        cfield1 = [div.text for div in inner_class]
        #=============================================== _cfield2 it is ok 
        class_name = "t0c ch{_cfield2}"
        inner_class = soup.find_all('div', class_=class_name)
        cfield2 = [div.text for div in inner_class]
        #===============================================
        mydata = []
        for row in cfield2:
            mydata.append(row.split(','))

        new_data = []  # store the new data that was scraped
        _time=datetime.datetime.now().time()
        _date=datetime.datetime.now().date()
        for i in range(len(ids)):
            row = [ids[i]] + list(mydata[i]) 
            new_data.append(tuple(row + [str(_time), str(_date)]))

        
      
        InsertIntoTable( new_data, "symbol_daily")
        #time.sleep(120)  # wait for 2 minutes before scraping the page again
        print("new game" + str(k))
        k+=1

        if datetime.datetime.now().time() >= _datefinish:
            exit()

