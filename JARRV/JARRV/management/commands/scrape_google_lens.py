from serpapi import GoogleSearch
import json
from webapp.models import Item
from webapp.models import Similar_Item
def test():
    for original_item_id, url in Item.objects.values('item_id','picture_link'):
        print(original_item_id,url)

def handle():
    #get rows from ItemTable to retreive item_id and url
    #values returns dictionaries..
    for original_item_id, url in Item.objects.values('item_id','picture_link'):
        results, original_item_id = fetch_similar_images(url, original_item_id)
        save_to_file(results)
        
        parsed_data = select_items(results, original_item_id) #parse_items(results)
        store_items(parsed_data) 



def fetch_similar_images(url, original_item_id):
    params = {
        "engine": "google_lens",
        "url": "https://lp2.hm.com/hmgoepprod?set=quality%5B79%5D%2Csource%5B%2F23%2F77%2F23775f02905967cdc57de792bae29adbcd7cdf33.jpg%5D%2Corigin%5Bdam%5D%2Ccategory%5B%5D%2Ctype%5BLOOKBOOK%5D%2Cres%5Bm%5D%2Chmver%5B1%5D&call=url[file:/product/fullscreen]",
        "no_cache": False,
        "api_key": "f7b7cf352366df12bea5dc2d01fb4d01441e5dee018fcea776e5e5637cc704f7"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    visual_matches = results["visual_matches"]
    return visual_matches, original_item_id
    

def select_items(visual_matches, original_item_id):
    recommerce_stores = ["Poshmark", "Depop", "Vinted", "Next", "ThredUp"]
    selected_items = []
    for item in visual_matches:
        for store in recommerce_stores:
            if item.get("source") == store:
                chosen_item = parse_item(item, original_item_id)
                selected_items.append(chosen_item)
    return(selected_items)



def save_to_file(images_data):
    with open('similar_image_results.json', 'w', encoding='utf-8') as file:
        json.dump(images_data, file, ensure_ascii=False, indent=4)


def parse_item(item, original_item_id):
    if item.get("price"):
        price = item.get("price")
    else:
        price = "Unknown"

    item = {
        "original_item_id" : original_item_id,
        "store" : item.get("source"),
        "item_name" : item.get("title"),
        "picture_link" : item.get("thumbnail"),
        "price": price,
        "link": item.get("link")
    }
    return item
 
    
# def parse_items(visual_matches, original_item_id):
    
#     items = []
    
#     for item in visual_matches:
#         if item.get("price"):
#             price = item.get("price")
#         else:
#             price = "Unknown"

#         item = {
#             "original_item_id" : original_item_id,
#             "store" : item.get("source"),
#             "item_name" : item.get("title"),
#             "picture_link" : item.get("thumbnail"),
#             "price": price,
#             "link": item.get("link")
#         }
 
#         items.append(item)
#     return items

  
def store_items(items):
    for item in items:
        Similar_Item.objects.create(
            original_item_id = item["original_item_id"],
            store = item["store"],
            item_name = ["item_name"],
            picture_link = ["picture_link"] ,
            price = item["price"],
            link = item["link"]
        )


#handle()
test()











