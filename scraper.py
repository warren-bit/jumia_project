# imports
from bs4 import BeautifulSoup
from urllib import request
import requests
import pandas as pd
import numpy as np
import time
import csv


base_url = 'https://www.jumia.co.ke/all-products/?page={}#catalog-listing'
starting_page = 1   #starting page
ending_page = 50    #ending page

# this functions scrapes product information prom all the pages and saves the data into a csv file
def scraper(url,starting_page,ending_page):
    product_list = []   #creating an empty  list to store our data temporarily
    # looping through all the pages
    for page_num in range(starting_page,(ending_page+1)):
        url = base_url.format(page_num)
        time.sleep(5)   #delay for 5 seconds before the next requests
        response = requests.get(url)   
        # tracking if each page is scraped successfully
        if response.status_code == 200: 
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f'Page {page_num} scraped successfully')
            items = soup.find_all('article', attrs={'class':'prd _fb col c-prd'})
            # looping through all products in each page
            for item in items:
                item_name = item.find('h3').text
                current_price = item.find('div', attrs={'class': 'prc'}).text
                old_price_element = item.find('div', attrs={'class' : 'old'})
                discount_element = item.find('div', attrs={'class' : 'bdg _dsct _sm'})
                link = item.find('a', attrs={'class':'core'}).get('href')
                old_price =None
                discount =None
                # only appending products with discount
                if discount_element:
                    old_price = old_price_element.text
                    discount = discount_element.text
                    product_list.append((item_name,current_price,old_price,discount,link))
        else:
            print(f'Failed to retrieve page, {page_num}')
    # creating the csv file
    csv_filename =  'C:/Users/Dell/Desktop/jumia_project/jumia_products.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Item name', 'Current price', 'Old price', 'Discount', 'Link']) # column names
        csv_writer.writerows(product_list)
    return(print(f'Number of products scraped: {len(product_list)}')) # returns total number of products scraped

 #calling the function           
scraper(base_url,starting_page,ending_page)