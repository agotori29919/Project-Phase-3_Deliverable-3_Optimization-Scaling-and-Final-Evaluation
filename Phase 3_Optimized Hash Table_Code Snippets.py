''' This not a complete code, there are 2 code snippets for Hash Table i.e. Collision Resolution & Dynamic Resizing '''

''' Code Snippet For Collision Resolution via Separate Chaining '''

class HashTable:
    def __init__(self):
        self.table_size = 10  # Example size, can grow
        self.table = [[] for _ in range(self.table_size)]  # Separate chaining using a list of lists

    def _hash_function(self, product_id):
        return product_id % self.table_size

    def add_product(self, product_id, name, quantity, price, category):
        index = self._hash_function(product_id)
        for i, product in enumerate(self.table[index]):
            if product['product_id'] == product_id:
                print(f"Product {product_id} already exists. Updating...")
                product.update({'name': name, 'quantity': quantity, 'price': price, 'category': category})
                return
        self.table[index].append({'product_id': product_id, 'name': name, 'quantity': quantity, 'price': price, 'category': category})
        print(f"Product {product_id} added at index {index}.")

    def search_product(self, product_id):
        index = self._hash_function(product_id)
        for product in self.table[index]:
            if product['product_id'] == product_id:
                return product
        return "Product not found."

    def remove_product(self, product_id):
        index = self._hash_function(product_id)
        for i, product in enumerate(self.table[index]):
            if product['product_id'] == product_id:
                del self.table[index][i]
                print(f"Product {product_id} removed from index {index}.")
                return
        print("Product not found.")


''' Code Snippet For Dynamic Resizing '''
def resize(self):
    new_table_size = self.table_size * 2
    new_table = [[] for _ in range(new_table_size)]
    for bucket in self.table:
        for product in bucket:
            index = product['product_id'] % new_table_size
            new_table[index].append(product)
    self.table = new_table
    self.table_size = new_table_size
