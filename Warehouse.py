import math
class Warehouse:
    def __init__(self, city, country, coordinates, stock):
        self.city = city
        self.country = country
        self.coordinates = coordinates
        self.stock = stock
    
class Product:
    def __init__(self, name, warehouses):
        self.name = name
        self.warehouses = warehouses
        
    def ship_within_country(self, sale_info):
        if self.name != sale_info.product:
            return []
        cities = []
        for warehouse in self.warehouses:
            if warehouse.country == sale_info.buyer.country:
                cities.append(warehouse.city)
        return cities

    def euclidean_distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    def closest_to_buyer(self, sale_info):
        if self.name != sale_info.product:
            return []
        min_distance = float('inf')
        min_city = []
        for warehouse in self.warehouses:
            distance = self.euclidean_distance(sale_info.buyer.coordinates[0], sale_info.buyer.coordinates[1], warehouse.coordinates[0], warehouse.coordinates[1])
            if distance < min_distance:
                min_city = [warehouse.city]
                min_distance = distance
            
        return min_city
        
        

class Buyer:
    def __init__(self, name, city, country, coordinates):
        self.name = name
        self.city = city
        self.country = country
        self.coordinates = coordinates

class SaleInfo:
    def __init__(self, buyer, product, quantity):
        self.buyer = buyer
        self.product = product
        self.quantity = quantity

