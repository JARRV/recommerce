import requests
from bs4 import BeautifulSoup as bs
import selenium 
from selenium import webdriver
from django.core.management.base import BaseCommand
#from webapp.models import Item
import json


#item
def handle (item, original_item_id, *args, **options):
    #get data from listing webpage
    #link
    '''
    item = {
        "position": 13,
        "title": "Ophelia Roe Tops | Woman's Thin Strap Flowered White Tank, Size 1x, Ophelia Roe | Color: White | Size: 1x | Gratesell's Closet",
        "link": "https://poshmark.com/listing/Womans-thin-strap-flowered-white-tank-size-1x-Ophelia-Roe-63f4e70856b2f8fbdc6f3a89",
        "source": "Poshmark",
        "source_icon": "https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcRglTQayecXuxgCFUZcgfbfA0OslKHNi_zul24ja6dNR7fFy_QNTwAYGBTDRYwPhEq6SEu7vqbjxSSTFT8JfQQODue5hNhO-4uQ26dgqP4HA44",
        "price": {
            "value": "$13.00*",
            "extracted_value": 13.0,
            "currency": "$"
        },
        "thumbnail": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcSaywz76XVLXnqfiaK1jFow2phHbn_54FQ_W5Tk94kvH1K1h4YI",
        "condition": "Used"
    }
    '''
    link = item.get("link")
    print(link)

    #check if link is listing, if not discard
    if is_listing_link(link) == False:
        print("discard not listing link")
        return None

    page_data = scrape_page(link)
    poshmark_item = scrape_poshmark_data(item, original_item_id, page_data)

    return poshmark_item

def scrape_page(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    url = url
    response = requests.get(url, headers=headers)
    soup = bs(response.content, "html.parser")
    return soup

#boolean function
def is_listing_link(url):
    if "/listing/" in url:
            return True
    else: 
            return False
    
#boolean function
def is_listing_available(data):
    if data.find('div', {"class" : "listing__removed d--b al--center"}):
        return False
    return True

#boolean function
def item_in_stock(data):
    # soup = handle(url)
    #if it is sold out then we dont store it at all
    if data.find('div', {"class" : "listing__inventory-status d--b col-x24 col-m16 bg--light-gray tc--dr"}):
        sold_out_div = data.find('div', {"class" : "listing__inventory-status d--b col-x24 col-m16 bg--light-gray tc--dr"})
        text = sold_out_div.find('h2').text.strip()
        if text == "This item is sold out" or text == "This item is sold":
            return False
    else:
        return True
    
def get_price(data):
    price = str(data.find('p', {"class": "h1"}).contents[0].strip())
    return price

def get_size(data):
    size = str(data.find('button', {"class": "size-selector__size-option btn btn--tertiary tc--m fw--bold br--magenta"}).text.strip())
    return size


#put item back
def scrape_poshmark_data(item, original_item_id, page_data):
    #check if item is in stock or not using the info from google lens
    if "in_stock" in item:
        stock = item.get("in_stock")
        if stock == False:
            print("out of stock")
            return None
    
    #check if listing is available
    if is_listing_available(page_data) == False:
        print("listing_removed")
        return None

    if item_in_stock(page_data) == False:
        print("out of stock")
        #dont store in database
        return None
    
    if "price" in item:
        price = str(item.get("price").get("extracted_value"))
        #might also have to get currency and extracted value or just value
    else:
        price = get_price(page_data)
        print(price)

    size = get_size(page_data)
    #get correct size and translate according to poshmark and our website
    #problem: poshmark has different sizes depending on the product


    item = {
        "original_item_id" : original_item_id,
        "store" : item.get("source"),
        "item_name" : item.get("title"), 
        "picture_link" : item.get("thumbnail"), 
        "price": price, 
        "link": item.get("link"),
        "size": size
        }
    
    
    return item




