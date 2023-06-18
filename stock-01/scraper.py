import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import psycopg2
import datetime

def scrape_data():
    # Set up Selenium driver
    driver = webdriver.Chrome()
    driver.get("https://www.forex.com/en/forex-trading/xau-usd/")

    # Wait for the page to load
    time.sleep(5)

    # Set up the CSV writer
    with open('stock_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['i','sell', 'buy','date','time']) # Write the header row to the CSV file
    
        i=0
        while i<40:
            # Extract the data you need using Selenium
            
           
            mydate = time.strftime('%Y-%m-%d')
            mytime = time.strftime('%H:%M:%S')
           
           
            buy = driver.find_element(By.XPATH, "//span[@data-bind='superscriptLastChar: offer, decimals: decimals']")
            buy = buy.text
            print("buy",buy)


            sell = driver.find_element(By.XPATH, "//span[@data-bind='superscriptLastChar: bid, decimals: decimals']")
            sell = sell.text
            print("sell",sell)

           
            # Write the data to the CSV file
            writer.writerow([i,buy, sell,mydate,mytime])

            # Wait for 1 minute before scraping again
            time.sleep(1)
            i=i+1
    # Close the Selenium driver
    driver.quit()

scrape_data()



 