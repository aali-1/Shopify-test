from Warehouse import *

laptop_warehouses = [Warehouse("Toronto", "Canada", [2,2], 1), 
                     Warehouse("Montreal", "Canada", [3,-1], 99), 
                     Warehouse("Seattle", "USA", [-2,1], 5),
                     Warehouse("London", "UK", [10,3], 10),]

laptop = Product("Laptop", laptop_warehouses)

tom = Buyer("Tom", "Vancouver", "Canada", [-2,5])
kevin_usa = Buyer("Kevin", "Seattle", "USA", [1,1])
john_uk = Buyer("John", "London", "UK", [0,0])
jack_paris = Buyer("Jack", "Paris", "France", [15,-3])
print("ship within country")
print(laptop.ship_within_country(SaleInfo(tom, "Laptop", 1)))
print(laptop.ship_within_country(SaleInfo(kevin_usa, "Laptop", 1)))
print("ship closest to buyer")
print(laptop.closest_to_buyer(SaleInfo(jack_paris, "Laptop", 1)))
print("stock availability")
print(laptop.stock_availability(SaleInfo(tom, "Laptop", 5)))
print(laptop.stock_availability(SaleInfo(kevin_usa, "Laptop", 98)))