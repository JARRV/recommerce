import requests
from bs4 import BeautifulSoup as bs
import selenium 
from selenium import webdriver
from django.core.management.base import BaseCommand
from JARRV.models import Item
import subprocess
import json



class Command(BaseCommand):
    help = "Scrape data from e-commerce and recommerce sites and save it to the database"

    def handle(self, *args, **options):
        all_data = []
        for page in range(1, 5):
            data = self.fetch_summer_dresses_hm(page)
            all_data.append(data)
            if data:
                all_data.extend(data)
        if all_data:
            self.save_to_file(all_data)

            
    def fetch_summer_dresses_hm(self, page):
        url = "https://www2.hm.com/hmwebservices/service/products/search/hm-greatbritain/Online/en"
        params = {
            'q': 'summer dresses:stock',
            'currentPage': page,
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
            'Cookie': 'your_cookie_data_here',  # Replace with actual cookie data if needed
            'Pragma': 'no-cache',
            'Referer': 'https://www2.hm.com/en_gb/search-results.html?q=summer%20dresses&image-size=small&image=stillLife&sort=stock&page=6',
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