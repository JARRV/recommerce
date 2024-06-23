#import serpapi
from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup as bs
import json
import sys
from django.core.management.base import BaseCommand
import os
from dotenv import load_dotenv
load_dotenv()
api_key = "f7b7cf352366df12bea5dc2d01fb4d01441e5dee018fcea776e5e5637cc704f7"#os.getenv('GOOGLE_LENS_API')
country = "us"
print("api_key", api_key)
from webapp.models import Item, Similar_Item
from .scrape_data_poshmark import handle as scrape_poshmark_1

class Command(BaseCommand):
    
    def test(self):
        #print(Item.objects.values('item_id','picture_link'))
        #print('-------------------')
        #print(type(Item.objects.values('item_id','picture_link')))
        
        for original_item_id, url in Item.objects.values_list('item_id','picture_link'):
            print(original_item_id,url)

    def handle(self,*args, **options):
        #get rows from ItemTable to retreive item_id and url
        #values returns dictionaries..

        for original_item_id, url in Item.objects.values_list('item_id','picture_link'):
            results, original_item_id = self.fetch_similar_images(url, original_item_id)
            self.save_to_file(results)
            
            parsed_data = self.select_items(results, original_item_id) #parse_items(results)
            print(parsed_data)
            self.store_items(parsed_data) 

        
        '''
        original_item_id = "1025935022_hm"

        item = {
        "position": 11,
        "title": "Vici | Tops | Vici Satin Halter Neck Blouse In Dusty Lavender | Poshmark",
        "link": "https://poshmark.ca/listing/VICI-Satin-Halter-Neck-Blouse-in-Dusty-Lavender-63817746bd062959cc127a5b",
        "source": "poshmark.ca",
        "source_icon": "https://encrypted-tbn1.gstatic.com/favicon-tbn?q=tbn:ANd9GcSLwCxIrEYwlqzTEytUsNpsaFhGtQxcVB0H_Pb0ZsV427zC6_cTUvjvpb6-NVBoW59zr5gXVIXj3OSEr9u6JtB7nkQnedVw6-Mw5HM-ShX3WA",
        "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQtd_V2CG2vLkpYd_jTs-sVmX2NAqSNcmOYCDKQoICh2zgAse2O"
    }

        item = {
            "position":
            2,
            "title":
            "Byron Lars | Dresses | Byron Lars Red Dress | Poshmark",
            "link":
            "https://poshmark.com/listing/Byron-Lars-Red-Dress-616492ff1460bbb2977d0117",
            "source":
            "Poshmark",
            "source_icon":
            "https://encrypted-tbn0.gstatic.com/favicon-tbn?q=tbn:ANd9GcRglTQayecXuxgCFUZcgfbfA0OslKHNi_zul24ja6dNR7fFy_QNTwAYGBTDRYwPhEq6SEu7vqbjxSSTFT8JfQQODue5hNhO-4uQ26dgqP4HA44",
            "thumbnail":
            "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcTc7KdnjmuvcG4g765kCWxvZ2Qpa89Gh6iZjkeMT3Tc-dVGVRCt"
        }
        

        self.parse_item(item, original_item_id)
    
    '''
    def fetch_similar_images(self, url, original_item_id):
        print('--call to fetch similar images--')
        params = {
            "engine": "google_lens",
            "url": url,
            "no_cache": False,
            "country": country,
            "api_key": api_key 
        }

        
        #search = serpapi.search(params)
        #visual_matches = search["visual_matches"]
        search = GoogleSearch(params)
        results = search.get_dict()
        visual_matches = results["visual_matches"]
    
        return visual_matches, original_item_id
           

    def select_items(self,visual_matches, original_item_id):
        recommerce_stores = ["Poshmark", "Depop", "Vinted", "Next", "thredup"]
        selected_items = []
        for item in visual_matches:
           if item.get("source") in recommerce_stores:
                #parse_item returns either None or item
                #if not None we will append to selected_items
                chosen_item = self.parse_item(item, original_item_id)
                if chosen_item != None:    
                    selected_items.append(chosen_item)
        return(selected_items)

    
    def save_to_file(self,images_data):
        with open('similar_image_results.json', 'w', encoding='utf-8') as file:
            json.dump(images_data, file, ensure_ascii=False, indent=4)
   
 
    def parse_item(self, item, original_item_id):
    
        #Scraping poshmark
        if item.get("source") == "Poshmark":
            poshmark_data = scrape_poshmark_1(item, original_item_id)
            print(poshmark_data)
            return poshmark_data

        if item.get("source") == "Depop":  
            return None
        
        if item.get("source") == "Vinted":  
            return None
           
        if item.get("source") == "Next":  
            return None
        
        if item.get("source") == "thredup":  
            return None
        
        '''
            link = item.get("link")
            print(link)
            #check if link is listing, if not discard
            if scrape_poshmark.is_listing_link(link) == False:
                print("discard not listing link")
                return 0
        
            #check if item is in stock or not using the info from google lens
            if "in_stock" in item:
                stock = item.get("in_stock")
                if stock == False:
                    print("not in stock false")
                    return 0
            
            #get data from listing webpage
            item_data = scrape_poshmark.handle(link)
            
            if scrape_poshmark.item_in_stock(item_data) == False:
                print("out of stock")
                #dont store in database
                return 0
        
            if "price" in item:
                price = item.get("price").get("extracted_value")
                #might also have to get currency and extracted value or just value
            else:
                price = scrape_poshmark.get_price(item_data)
                print("Unkwown")
                print(price)
        '''
        '''
        item = {
                "original_item_id" : original_item_id,
                "store" : item.get("source"),
                "item_name" : item.get("title"), 
                "picture_link" : item.get("thumbnail"), 
                "price": price, 
                "link": item.get("link"),
                "size": size
        }
        '''
        return 0 


    def store_items(self,items):
        for item in items:
            try:
                original_item_instance = Item.objects.get(item_id=item["original_item_id"])
                Similar_Item.objects.create(
                    original_item_id = original_item_instance,
                    store = item["store"],
                    item_name = item["item_name"],
                    picture_link = item["picture_link"] ,
                    price = item["price"],
                    link = item["link"],
                    size = item["size"]
            )
            except Item.DoesNotExist:
                print(f"Item does not exist")
