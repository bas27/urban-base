class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'
class Shop:
    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        content = file.read()
        file.close()
        return content

    def add(self, *products):
        file = open(self.__file_name, 'a')
        file_w = self.get_products()
        for product in products:
            if product.name in file_w:
                print(f'Продукт {product.name} уже есть в магазине')
                continue
            else:
                file.write(str(product) + '\n')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
p4 = Product('Meat', 5.5, "Meat")


print(p2) # __str__

s1.add(p1, p2, p3, p4)

print(s1.get_products())