from typing import List

class Nodo(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
    
    def __str__(self):
        return f"Nodo con key: {self.key}"

class Tree(object):
    def __init__(self):
        self.root = None
    
    def tree_insert(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == None:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def inorder_tree_walk(self, x):
        if x != None:
            self.inorder_tree_walk(x.left)
            print(x.key)
            self.inorder_tree_walk(x.right)

    def preorder_tree_walk(self, x):
        if x != None:
            print(x.key)
            self.preorder_tree_walk(x.left)
            self.preorder_tree_walk(x.right)

    def postorder_tree_walk(self, x):
        if x != None:
            self.postorder_tree_walk(x.left)
            self.postorder_tree_walk(x.right)
            print(x.key)
    
    def tree_search(self, x, k):
        if ((x == None) or (k == x.key)):
            return x
        if (k < x.key):
            return Tree.tree_search(self, x.left, k)
        else:
            return Tree.tree_search(self, x.right, k)
        
    def tree_minimum(self, x):
        while (x.left != None):
            x = x.left
        return x

    def tree_maximum(self, x):
        while (x.right != None):
            x = x.right
        return x


tree = Tree()
tree.tree_insert(Nodo(12))
tree.tree_insert(Nodo(5))
tree.tree_insert(Nodo(18))
tree.tree_insert(Nodo(2))
tree.tree_insert(Nodo(9))
tree.tree_insert(Nodo(15))
tree.tree_insert(Nodo(19))
tree.tree_insert(Nodo(13))
tree.tree_insert(Nodo(17))

#root = Nodo(1)
#root.left = Nodo(2)
#root.right = Nodo(3)
#root.left.left = Nodo(4)
#root.left.right = Nodo(5)
'''tree.inorder_tree_walk(tree.root)
print("\n")
tree.preorder_tree_walk(tree.root)
print("\n")
tree.postorder_tree_walk(tree.root)'''

print(tree.tree_minimum(tree.root))
print(tree.tree_maximum(tree.root))
print(tree.tree_search(tree.root, 5))