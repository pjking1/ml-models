# This code is designed to pull info from an Amazon Product Page every hour.


# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 16:17:08 2022

@author: patking4
"""
# Import Librairies
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime

# Connect to website
URL = "https://www.amazon.co.uk/Xbox-Wireless-Controller-Mineral-Special/dp/B093X59B31/ref=zg_bsms_videogames_sccl_8/259-5513564-6711269?psc=1"

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "DNT":"1", "Connection":"close", "Upgrade-Insecure-Requests": "1"} 

page = requests.get(URL, headers=headers)
print(page)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# Finds the text attached to the tag given
title = soup2.find(id="productTitle") 
price = soup2.find(id="priceblock_ourprice")

title = title.get_text()
price = price.get_text()

title = title.strip() # .strip() removes the blank space before
price = price.strip()[1:]
today = datetime.date.today()
times = datetime.datetime.now()

import csv

# Create data and header
header = ['Title','Price','Date','Time']
data = [title, price, today, times]

# Write the data and header to a csv
with open('AmazonWebScraperDataset.csv','w', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    
# Show the data frame
import pandas as pd

df = pd.read_csv("C:/Users/patking4/Documents/Black Friday Scraper/AmazonWebScraperDataset.csv")
print(df)

# Append new data to csv
with open('AmazonWebScraperDataset.csv','a', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)

# Create an email send function
#def send_mail():
#    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
#    server.ehlo()
#    server.starttls()
#    server.ehlo()
#    server.login('patrick.send.csv@gmail.com','example123.')
    
#    subject = "The Controller is now below Retail Price!"
#    body = "Link here: https://www.amazon.co.uk/Xbox-Wireless-Controller-Mineral-Special/dp/B093X59B31/ref=zg_bsms_videogames_sccl_8/259-5513564-6711269?psc=1"
    
#    msg = f"Subject: {subject}\n\n{body}"
    
#    server.sendmail('patrick.king@profitero.com', msg)

# Function to append
def check_price():
    URL = "https://www.amazon.co.uk/Xbox-Wireless-Controller-Mineral-Special/dp/B093X59B31/ref=zg_bsms_videogames_sccl_8/259-5513564-6711269?psc=1"

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36", "Accept-Encoding": "gzip, deflate, br", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "DNT":"1", "Connection":"close", "Upgrade-Insecure-Requests": "1"} 

    page = requests.get(URL, headers=headers)
    print(page)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    # Finds the text attached to the tag given
    title = soup2.find(id="productTitle") 
    price = soup2.find(id="priceblock_ourprice")

    title = title.get_text()
    price = price.get_text()

    title = title.strip() # .strip() removes the blank space before
    price = price.strip()[1:]
    today = datetime.date.today()
    times = datetime.datetime.now()

    import csv

    # Create data and header
    header = ['Title','Price','Date','Time']
    data = [title, price, today, times]
    
    with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
    
#    if(price == '54.99'):
#        send_mail()

# Repeat proces every hour to add a new line to the csv
while(True):
    check_price()
    time.sleep(3600)
