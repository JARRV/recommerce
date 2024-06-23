
import requests
from bs4 import BeautifulSoup as bs
from django.core.management.base import BaseCommand
from webapp.models import Item
import subprocess
import json

class Command(BaseCommand):
    help = "Scrape data from depop product page"

    def handle(self, *args, **options):
        link = "https://www.depop.com/products/devonjanegubala-gianni-bini-white-lace-print/"
        product_name = self.extract_between_last_two_slashes(link)
        url = f"https://webapi.depop.com/api/v2/product/{product_name}/?includeSellerShippingInfo=true&lang=en"
        data =self.fetch_depop(url)
        self.save_to_file(data)

            
    def extract_between_last_two_slashes(self,url):
        parts = url.rstrip('/').rsplit('/', 2)
        if len(parts) >= 2:
            return parts[-1]
        return None
    def fetch_depop(self, url):
        

        params = {
            'includeSellerShippingInfo': 'true',
            'lang': 'en'
        }

        # Headers
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'Cache-Control': 'no-cache',
            'Origin': 'https://www.depop.com',
            'Pragma': 'no-cache',
            'Referer': 'https://www.depop.com/',
            'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
            'X-Cached-Sizes': 'true',
            'Cookie': '__cf_bm=0tkVO7i6nvADhq62wZfxi7gqqFepOc5INzsxuq3FTJg-1718766167-1.0.1.1-HmrKrQ_ns_ZFEXJZ..kRjA6_kz6r_hhIfIv15ry28ig3WPfVZFOsPPj.H.JL7TUDbXGaQ7jo5Qz_JlA7RTvCYw; path=/; expires=Wed, 19-Jun-24 03:32:47 GMT; domain=.webapi.depop.com; HttpOnly; Secure; SameSite=None'
        }

        # Sending GET request
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            self.stdout.write(self.style.ERROR(f"Failed: {response.status_code}"))
            return None
                
    def save_to_file(self, data):
        with open('depop_product.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        self.stdout.write(self.style.SUCCESS("Data saved to depop_product.json"))






'''
       # price = soup.find('div', {"class": "ProductDetailsSticky-styles__StyledProductPrice-sc-17bd7b59-4 qJnzl"}).find('div')
       # print(price)

       # size = soup.find('button', {"class": "size-selector__size-option btn btn--tertiary tc--m fw--bold br--magenta"}).text.strip()
       # print(size)
        #if we really want to use sizes we are going to have to make sizes generic to our website, prob use a dictionary for each website
        #matching sizing to ours.

   

    def item_in_stock(self, soup):

        #if it is sold out then we dont store it at all
        if soup.find('div', {"class" : "listing__inventory-status d--b col-x24 col-m16 bg--light-gray tc--dr"}):
            sold_out_div = soup.find('div', {"class" : "listing__inventory-status d--b col-x24 col-m16 bg--light-gray tc--dr"})
            text = sold_out_div.find('h2').text.strip()
            if text == "This item is sold":
                return False
        else:
            return True
'''  

