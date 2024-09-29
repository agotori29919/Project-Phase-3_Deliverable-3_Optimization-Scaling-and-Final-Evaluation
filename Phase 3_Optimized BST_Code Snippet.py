''' 
This not a complete code, this has a code snippet for BST i.e. AVL tree, a self-balancing binary search tree
Code Snippet For Self-Balancing Binary Search Tree (AVL Tree)
'''

def insert(self, root, price, product):
    if root is None:
        return AVLNode(price, product)
    
    if price < root.price:
        root.left = self.insert(root.left, price, product)
    else:
        root.right = self.insert(root.right, price, product)

    # Update height and balance factor
    root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
    balance = self.get_balance(root)

    # Perform rotations if the tree is unbalanced
    if balance > 1 and price < root.left.price:
        return self.right_rotate(root)
    if balance < -1 and price > root.right.price:
        return self.left_rotate(root)
    return root
