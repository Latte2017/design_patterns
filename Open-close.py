from enum import Enum

class color(Enum):
    Red = 1
    Blue=2
    Green=3

class size(Enum):
    Small=1
    Medium=2
    Large=3

class product:
    def __init__(self, product_name, product_size, product_color) -> None:
        self.product_name = product_name
        self.product_size = size(product_color)
        self.product_color = color(product_color)

class catalog:
    def __init__(self) -> None:
        self.catalog = []

    def addProduct(self, product_name, product_size, product_color) -> None:
        prod = product(product_name, product_size, product_color)
        self.catalog.append(prod)
    
    def showCatalog(self) -> None:
        for prod in self.catalog:
            print(f'product is {prod.product_name} {prod.product_size.name}  {prod.product_color.name} \n\n')
    

if __name__=="__main__":
    cat = catalog()
    cat.addProduct("prod1", 1,1)
    cat.showCatalog()