import requests
from bs4 import BeautifulSoup as bs
import selenium 
from selenium import webdriver
from django.core.management.base import BaseCommand
from webapp.models import Item

class Command(BaseCommand):
    help = "Scrape data from e-commerce and recommerce sites and save it to the database"

    def handle(self, *args, **options):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

        url = "https://www.vinted.com/items/4604497803-summer-dress?referrer=catalog"
        response = requests.get(url, headers)
        
        print(f"Status Code: {response.status_code}")

        soup = bs(response.content, "html.parser")

        #search for summer dresses


        items = soup.find_all('div', {"class": "new-item-box__container"})

        for item in items:
            item_description = item.find('div', {"class": "web_ui__Cell_body"})
            item_price = item_description.find('div', {"class": "title_content"}).find('p').text


        print(soup.prettify())