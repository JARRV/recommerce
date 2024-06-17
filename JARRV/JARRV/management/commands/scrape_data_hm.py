import requests
from bs4 import BeautifulSoup as bs
from django.core.management.base import BaseCommand
from webapp.models import Item
import subprocess
import json



class Command(BaseCommand):
    help = "Scrape data from e-commerce and recommerce sites and save it to the database"

    def handle(self, *args, **options):

        # data = self.fetch_summer_dresses_hm(3)
        # parsed_data = self.parse_items(data)
        all_data = []
        for page in range(1, 2):
            data = self.fetch_summer_dresses_hm(page)
            parsed_data = self.parse_items(data)
            self.store_items(parsed_data)

            self.save_to_file(data)

            
    def fetch_summer_dresses_hm(self, page):
        url = "https://www2.hm.com/hmwebservices/service/products/search/hm-greatbritain/Online/en"
        params = {
            'q': 'summer dresses:stock',
            'currentPage': page,  # You can change the page number as needed
            'pageSize': 36,
            'saleFacets': 'true',
            'enableRetry': 'true',
            'forceSearch': 'false',
            'skipStockCheck': 'false'
        }
        headers = {
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'Cache-Control': 'no-cache',
            'Cookie': 'agCookie=f9264aff-948b-4cbf-9fd9-f46544ed8a78; ...',  # Replace with actual cookie data
            'Pragma': 'no-cache',
            'Referer': 'https://www2.hm.com/en_gb/search-results.html?q=summer%20dresses',
            'Sec-Ch-Ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"macOS"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'X-Customer-Key': 'f9264aff-948b-4cbf-9fd9-f46544ed8a78',
            'X-Session-Key': 'f9264aff-948b-4cbf-9fd9-f46544ed8a78'
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            self.stdout.write(self.style.ERROR(f"Failed to retrieve data from page {page}: {response.status_code}"))
            return None
         
    def save_to_file(self, data):
        with open('summer_dresses_hm.json', 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        self.stdout.write(self.style.SUCCESS("Data saved to summer_dresses_hm.json"))

    def parse_items(self, response):
        items = []
        data = response["results"]

        for item in data:
            code = item.get("code") #product code
            product_code = code.replace("_group_", "")
            store = item.get("brandName")


            item = {
                "item_id": f"{product_code}_hm",
                "store" : item.get("brandName"),
                "item_name" : item.get("name"),
                "item_type" : item.get("name").split()[-1],
                "category" : item.get("categoryName"),
                "picture_link" : item.get("images")[0].get("baseUrl"),
                "brand" : item.get("brandName"),
                "price" : item.get("price").get("value"),
                "link": f"https://www2.hm.com/en_gb/productpage.{product_code}.html",
            }
            items.append(item)
        return items
    
    def store_items(self, items):
        for item in items:
            Item.objects.create(
                item_id=item["item_id"], 
                store=item["store"],
                item_name=item["item_name"],
                item_type=item["item_type"],
                category=item["category"],
                picture_link=item["picture_link"],
                brand=item["brand"],
                price=item["price"],
                link=item["link"],
            )
    
