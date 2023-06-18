from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv

webdriver_path = 'path/to/chromedriver'

# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path=webdriver_path)
driver.maximize_window()

url = "https://10times.com/pegs-boston"
driver.get(url)

print('====================')
div_elements = driver.find_elements(By.XPATH, "(//div[@class='col-md-10 col-sm-9'])[last()]//div[position() > last() - 3]")
title = div_elements[0].text
date = div_elements[1].text
location = div_elements[2].text
print("Title: " + title)
print("Date: " + date)
print("Location: " + location)
print('============================')

table = driver.find_element("css selector", ".table.noBorder.mng.w-100.trBorder")
rows = table.find_elements("tag name", "tr")

data = [title, date, location]  # Header row

# Iterate over the rows and extract the data
for row in rows:
    columns = row.find_elements("tag name", "td")
    row_data = ""
    for column in columns:
        row_data += column.text.replace('\n', ' ') + ", "
    data.append(row_data.rstrip(", "))

dataHeader = ['TITLE' for _ in data]

# Create CSV file
filename = "data.csv"
with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(dataHeader)  # Write header and detail data in a single row
    writer.writerow(data)  # Write header and detail data in a single row

print(f"Data saved to {filename}")

time.sleep(10)
driver.quit()
