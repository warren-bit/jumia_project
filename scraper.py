# imports
from bs4 import BeautifulSoup
from urllib import request
import requests
import pandas as pd
import numpy as np
import time
import csv


base_url = 'https://www.jumia.co.ke/all-products/?page={}#catalog-listing'
starting_page = 1
ending_page = 50

base_url = 'https://www.jumia.co.ke/all-products/?page={}#catalog-listing'
starting_page = 1
ending_page = 50
def scraper(url,starting_page,ending_page):
    product_list = []
    for page_num in range(starting_page,(ending_page+1)):
        url = base_url.format(page_num)
        time.sleep(5)
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f'Page {page_num} scraped successfully')
            items = soup.find_all('article', attrs={'class':'prd _fb col c-prd'})
            for item in items:
                item_name = item.find('h3').text
                current_price = item.find('div', attrs={'class': 'prc'}).text
                old_price_element = item.find('div', attrs={'class' : 'old'})
                discount_element = item.find('div', attrs={'class' : 'bdg _dsct _sm'})
                link = item.find('a', attrs={'class':'core'}).get('href')
                old_price =None
                discount =None
                if discount_element:
                    old_price = old_price_element.text
                    discount = discount_element.text
                    product_list.append((item_name,current_price,old_price,discount,link))
        else:
            print(f'Failed to retrieve page, {page_num}')
    
    csv_filename =  'C:/Users/Dell/Desktop/jumia_project/jumia_products.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Item name', 'Current price', 'Old price', 'Discount', 'Link'])
        csv_writer.writerows(product_list)
    return(print(f'Number of products scraped: {len(product_list)}'))
            
scraper(base_url,starting_page,ending_page)