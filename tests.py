from Warehouse import *

laptop_warehouses = [Warehouse("Toronto", "Canada", [2,2], 1), 
                     Warehouse("Montreal", "Canada", [3,-1], 99), 
                     Warehouse("Seattle", "USA", [1,1], 100)]

laptop = Product("Laptop", laptop_warehouses)

tom = Buyer("Tom", "Vancouver", "Canada", [-2,5])
kevin_usa = Buyer("Kevin", "Seattle", "USA", [1,1])
john_uk = Buyer("John", "London", "UK", [0,0])
print(laptop.ship_within_country(SaleInfo(tom, "Laptop", 1)))
print(laptop.ship_within_country(SaleInfo(kevin_usa, "Laptop", 1)))