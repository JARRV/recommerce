import requests
from bs4 import BeautifulSoup as bs
import selenium 
from selenium import webdriver
from django.core.management.base import BaseCommand
from JARRV.models import Item
import subprocess



class Command(BaseCommand):
    help = "Scrape data from e-commerce and recommerce sites and save it to the database"

    def bypass_403(url):
        command = ['./nomore403/nomore403.sh', url]

    def handle(self, *args, **options):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        url = "https://www2.hm.com/en_us/productpage.1228855001.html"
        response = requests.get(url, headers)
        
        print(f"Status Code: {response.status_code}")

        soup = bs(response.content, "html.parser")

        #search for summer dresses


        items = soup.find_all('div', {"class": "new-item-box__container"})

        for item in items:
            item_description = item.find('div', {"class": "web_ui__Cell_body"})

            item_description.find('div', {"class": "title_content"}).f


        print(soup.prettify())