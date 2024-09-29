'''
Here's the complete code for the optimized hash table with collision handling and resizing, 
along with an example script to demonstrate adding, searching, and removing products.
'''

class HashTable:
    def __init__(self):
        self.table_size = 10  # Initial size
        self.count = 0  # Track the number of products
        self.table = [[] for _ in range(self.table_size)]  # Separate chaining using list of lists

    # Hash function to determine the index for a given product ID
    def _hash_function(self, product_id):
        return product_id % self.table_size

    # Add product to the hash table
    def add_product(self, product_id, name, quantity, price, category):
        index = self._hash_function(product_id)
        # Check for existing product with the same product_id in the chain
        for i, product in enumerate(self.table[index]):
            if product['product_id'] == product_id:
                print(f"Product {product_id} already exists. Updating...")
                product.update({'name': name, 'quantity': quantity, 'price': price, 'category': category})
                return

        # Add new product if no conflict
        self.table[index].append({'product_id': product_id, 'name': name, 'quantity': quantity, 'price': price, 'category': category})
        self.count += 1
        print(f"Product {product_id} added at index {index}.")

        # Resize if load factor exceeds threshold (e.g., load factor > 0.7)
        if self.count / self.table_size > 0.7:
            self.resize()

    # Search for product by product ID
    def search_product(self, product_id):
        index = self._hash_function(product_id)
        for product in self.table[index]:
            if product['product_id'] == product_id:
                return product
        return "Product not found."

    # Remove a product by product ID
    def remove_product(self, product_id):
        index = self._hash_function(product_id)
        for i, product in enumerate(self.table[index]):
            if product['product_id'] == product_id:
                del self.table[index][i]
                self.count -= 1
                print(f"Product {product_id} removed from index {index}.")
                return
        print("Product not found.")

    # Resize the hash table and rehash all products
    def resize(self):
        new_table_size = self.table_size * 2
        new_table = [[] for _ in range(new_table_size)]
        # Rehash all products
        for bucket in self.table:
            for product in bucket:
                index = product['product_id'] % new_table_size
                new_table[index].append(product)
        self.table = new_table
        self.table_size = new_table_size
        print(f"Resized hash table to new size {new_table_size}.")

# Example usage of the HashTable class
if __name__ == "__main__":
    # Create a hash table instance
    inventory = HashTable()

    # Add products to the inventory
    inventory.add_product(1, "Mobile", 10, 1200, "Electronics")
    inventory.add_product(2, "Tablet", 15, 500, "Electronics")
    inventory.add_product(12, "Chair", 5, 150, "Furniture")  # Will collide with product_id 2

    # Update an existing product
    inventory.add_product(2, "Tablet", 20, 550, "Electronics")

    # Search for products
    print(inventory.search_product(1))  
    print(inventory.search_product(12)) 
    print(inventory.search_product(3))  

    # Remove a product
    inventory.remove_product(12)  

    # Search again after removal
    print(inventory.search_product(12))  

    # Add more products to trigger resizing
    inventory.add_product(13, "Monitor", 8, 300, "Electronics")
    inventory.add_product(23, "Keyboard", 25, 50, "Electronics")
    inventory.add_product(33, "Mouse", 30, 25, "Electronics")

    # This will trigger a resize because the load factor > 0.7
