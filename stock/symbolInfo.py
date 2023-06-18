import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime
from dbconfig import get_mysql_connection 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dbconfig import InsertIntoTable
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
url_1 = config['mysql']['url_1']
url_2 = config['mysql']['url_2']


def insertSymbolInfo():
    db = get_mysql_connection()

    mycursor = db.cursor(buffered=True)
    query = " SELECT symbol_id FROM symbol ;"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    db.close()
    #driver = webdriver.Chrome()
    #==========================================
    options = webdriver.ChromeOptions()
    options.add_argument(f'--remote-debugging-port=9222')
    options.add_argument(f'--user-data-dir=c:\chrome')
    options.add_experimental_option('debuggerAddress', 'localhost:9222')
    driver = webdriver.Chrome(options=options)

    # switch to the tab with the website
    driver.execute_script('window.open("");')
    driver.switch_to.window(driver.window_handles[0])
    #==========================================

    _time=datetime.datetime.now().time()
    _date=datetime.datetime.now().date()

    row_tuple=[]
    for row in rows:
        symbol_id = row[0]
        driver.refresh()
        # Set up Selenium driver
        driver.get( url_2 + str(symbol_id)+"#")
        

        time.sleep(10)
        current_url = driver.current_url
        print(current_url)
        #avg_1 = driver.find_element(By.XPATH, "//*[contains(@class, 'box2') or contains(@class, 'zil')][1]//div[contains(@class, 'box6') or contains(@class, 'h80')][position() = 4]//tr[4]//td[2]").text
        #avg_1 = avg_1.replace(",", "").replace("M","").replace("m","")
        #print(avg_1)
        #===============================
        if current_url== url_2 + str(symbol_id)+"#":
            element = driver.find_element(By.XPATH, "//*[contains(@class, 'yellow') and not(contains(@class, 'tbl') or contains(@class, 'box'))]")
            driver.execute_script("arguments[0].click(); ii.ShowTab(3);", element)
            time.sleep(10)
            # find the div element with class="box1 yellow tbl"
            tbl_div = driver.find_element(By.XPATH,"//div[contains(@class, 'box1') and contains(@class, 'yellow') and contains(@class, 'tbl') and not(contains(@class, 's280'))][last()]")
        else:
            print("no")
            element = driver.find_element(By.XPATH, "//*[contains(@class, 'yellow') and not(contains(@class, 'tbl') or contains(@class, 'box'))]").click()
            time.sleep(5)
            # find the div element with class="box1 yellow tbl z2_4"
            tbl_div = driver.find_element(By.XPATH,"//div[contains(@class, 'box1') and contains(@class, 'yellow') and contains(@class, 'tbl') and contains(@class, 'z2_4') ][last()]")
        #===============================

        table = tbl_div.find_element(By.XPATH, ".//table[contains(@class,'table1')]")
        tds = table.find_elements(By.XPATH,".//td")
        col2_values = []
        col2_values.append(symbol_id)
        for k in range(1, len(tds), 2): 
            col2_values.append(tds[k].text)
        
        #col2_values.append("0")
        col2_values.append(_time)
        col2_values.append(_date )

        #col2_values.append(avg_1)
        row_tuple.append( tuple(col2_values))
        print(symbol_id,tuple(col2_values),sep='__')
        
        #===============================
    InsertIntoTable(row_tuple,"shenase_symbol")

    mycursor.close()

    
        

