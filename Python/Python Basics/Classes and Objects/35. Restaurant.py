class Restaurant:
   name = ''
   category = ''
   rating = 0.0
   delivery = False

red_restaurant = Restaurant()
red_restaurant.name = 'Red Restaurant'
red_restaurant.delivery = True
red_restaurant.category = 'Italian Food'
red_restaurant.rating = 4.9

print(vars(red_restaurant))