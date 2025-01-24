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

