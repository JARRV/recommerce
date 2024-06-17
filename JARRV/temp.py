#just testing retrival for different responses

import json 
import openai
openai.api_key = "sk-proj-il4VkGaj46AgbBN0kqK7T3BlbkFJ7R5nIVvNe6tLasArJRMC"

with open('summer_dresses_hm.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

curr_product = 2

print(data["results"][curr_product].get("name")) #item name
print(data["results"][curr_product].get("name").split()[-1]) #item type
print(data["results"][curr_product].get("price").get("value")) #item price
print(data["results"][curr_product].get("brandName")) #brand
image_url = (data["results"][curr_product].get("defaultArticle").get("images")[0].get("baseUrl")) #product image url 
print(data["results"][curr_product].get("categoryName")) #Category (kids, women, men)
code = data["results"][curr_product].get("code") #product code
product_code= code.replace("_group_", "")
product_link = f"https://www2.hm.com/en_us/productpage.{product_code}.html"
print(product_link)



def parse_items(response):
    items = []
    data = response["results"]

    for item in data:
        code = item.get("code") #product code
        product_code= code.replace("_group_", "")

        item = {
            "store" : item.get("brandName"),
            "item_name" : item.get("name"),
            "item_type" : item.get("name").split()[-1],
            "category" : item.get("categoryName"),
            "picture_link" : item.get("images")[0].get("baseUrl"),
            "brand" : item.get("brandName"),
            "price" : item.get("price").get("formattedValue"),
            "link": f"https://www2.hm.com/en_gb/productpage.{product_code}.html",
        }
        items.append(item)
    return items
print(parse_items(data))


