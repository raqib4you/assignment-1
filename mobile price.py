mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

ALL_Data = mobile_data.get("data")

for User in ALL_Data :
    name = User.get("name")
    price = User.get("price")
    price_valu = price.replace("USD", " ")
    made = User.get("made")
    Echange_rate = mobile_data.get("exchnage_rate")
    BDT = (float(price_valu)) * Echange_rate
    Output = f"{name} is made in {made}. The Price is 300 usd which is almost {BDT} bdt"
    print(Output)