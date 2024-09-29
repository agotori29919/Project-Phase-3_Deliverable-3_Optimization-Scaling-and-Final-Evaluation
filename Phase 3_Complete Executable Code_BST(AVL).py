'''
Here, is the complete AVL Tree implementation with self-balancing (rotations), allowing it to handle larger datasets efficiently

'''
class AVLNode:
    def __init__(self, price, product):
        self.price = price
        self.product = product
        self.left = None
        self.right = None
        self.height = 1  # Height of the node


class AVLTree:
    # Get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Calculate balance factor of a node
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Perform a right rotation
    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Perform a left rotation
    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    # Insert a product into the AVL Tree
    def insert(self, node, price, product):
        # Perform normal BST insertion
        if not node:
            return AVLNode(price, product)
        if price < node.price:
            node.left = self.insert(node.left, price, product)
        else:
            node.right = self.insert(node.right, price, product)

        # Update the height of the current node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        # Get the balance factor to check if the node is unbalanced
        balance = self.get_balance(node)

        # Perform rotations to balance the tree if needed
        # Left Left Case
        if balance > 1 and price < node.left.price:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and price > node.right.price:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and price > node.left.price:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and price < node.right.price:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    # Find the product with the minimum price in the tree
    def find_min(self, node):
        if node is None or node.left is None:
            return node
        return self.find_min(node.left)

    # Delete a node from the AVL Tree
    def delete(self, root, price):
        # Standard BST delete
        if not root:
            return root
        elif price < root.price:
            root.left = self.delete(root.left, price)
        elif price > root.price:
            root.right = self.delete(root.right, price)
        else:
            # Node with only one child or no child
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            # Node with two children: get the in-order successor
            temp = self.find_min(root.right)
            root.price = temp.price
            root.product = temp.product
            root.right = self.delete(root.right, temp.price)

        # Update the height of the current node
        if root is None:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Balance the tree
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Search for products in a price range
    def search_price_range(self, node, low, high):
        if not node:
            return []
        result = []
        if low <= node.price <= high:
            result.append(node.product)
        if node.price > low:
            result += self.search_price_range(node.left, low, high)
        if node.price < high:
            result += self.search_price_range(node.right, low, high)
        return result

# Example usage of the AVL Tree
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    # Inserting products into the AVL Tree
    root = tree.insert(root, 1200, "Laptop")
    root = tree.insert(root, 500, "Tablet")
    root = tree.insert(root, 150, "Chair")
    root = tree.insert(root, 300, "Monitor")
    root = tree.insert(root, 50, "Keyboard")
    root = tree.insert(root, 200, "Mouse")

    # Searching for products in a price range
    products_in_range = tree.search_price_range(root, 100, 600)
    print("Products in price range 100 to 600:", products_in_range)

    # Deleting a product from the tree
    root = tree.delete(root, 500)
    print("Products after deleting 500 price product:")
    products_in_range = tree.search_price_range(root, 100, 600)
    print(products_in_range)
