
#https://material-exchange.com/water-use-to-create-my-wardrobe/#:~:text=A%20hooded%20sweatshirt%3A%20uses%201%2C715,gallons%20(or%206%2C600%20liters).

gallons_saved = {
    "dress": 1550, #3 droplets
    "jeans": 1800, # 3 and half droplets
    "t-shirt": 800, #715, 1 and half droplets
    "hoodie": 1720, #1715, 3 and half droplets
    "sweatshirt": 1720, #1715, 3 and half droplets
}

#maybe 1 droplet can represent 500 gal


def calculate_gallons(item_type):
    gallons = gallons_saved[item_type]
    return gallons