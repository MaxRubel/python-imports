from appliances.kitchen import Refrigerator, CoffeeMaker, Dishwasher
from appliances.laundry import Dryer, Washer

whirlpool_dishwasher = Dishwasher("black")
whirlpool_dishwasher.wash_dishes()

samsung_washer = Washer("red", "electric")
samsung_dryer = Dryer("red", "gas")

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()
