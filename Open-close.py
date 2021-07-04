from enum import Enum

class color(Enum):
    Yellow=0
    Red = 1
    Blue=2
    Green=3

class size(Enum):
    ExtraSmall=0
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
            print(f'{prod.product_name} {prod.product_size.name}  {prod.product_color.name}')

    def filterByColor(self, color) -> None:

        for prod in self.catalog:
            if prod.product_color.value == color:
                print(f'Matching product is {prod.product_name}')
    
    def getCatalog(self) -> list:
        return self.catalog
    

    def filterBySize(self, size) -> None:

        for prod in self.catalog:
            if prod.product_size.value == size:
                print(f'Matching product is {prod.product_name}')
    

class Specification:
    def is_specified(self, item):
        pass



class Filter:
    def filter(self, filter):
        pass

class colorSpecification(Specification):
    def __init__(self, color):
        self.color = color
    
    def is_satisfied(self, item):
            if item.product_color.value == self.color:
                return True

class sizeSpecification(Specification):
    def __init__(self, size):
        self.size = size
    
    def is_satisfied(self, item):
            if item.product_size.value == self.size:
                return True

class andSpecification(Specification):
    def __init__(self, *args) -> None:
        self.specs = args
    
    def is_satisfied(self, item):
        #print(list(filter(lambda spec: (spec.is_satisfied(item)))))
        return all(map(
            lambda spec: spec.is_satisfied(item), self.specs))
        #return all(map(lambda spec: (spec.is_satisfied(item)), self.specs))
        #all --> return True if all values are True
        #map --> take a function and apply function to list
        #lambda --> nameless function


class betterFilter(Filter):
    def filter(self, spec, catalog_list):
        for item in catalog_list:
            if (spec.is_satisfied(item)):
                print(f'{item.product_name} {item.product_size.value} {item.product_color.value}') 



if __name__=="__main__":
    cat = catalog()

    for idx in range(1,10):
        cat.addProduct("prod" + str(idx), idx%3, idx%3)
    #cat.showCatalog()

    #cat.filterByColor(2)

    catalog_list = cat.getCatalog()
    color_spec = colorSpecification(1)
    size_spec = sizeSpecification(1)
    size_spec1 = sizeSpecification(2)
    large_blue1 = andSpecification(color_spec, size_spec)
    bf = betterFilter()
    #bf.filter(color_spec, catalog_list)
    bf.filter(large_blue1, catalog_list)
