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
            return self.tree_search(x.left, k)
        else:
            return self.tree_search(x.right, k)
        
    def tree_minimum(self, x):
        while (x.left != None):
            x = x.left
        return x

    def tree_maximum(self, x):
        while (x.right != None):
            x = x.right
        return x
    
    def tree_succesor(self, x):
        if (x.right != None):
            return self.tree_minimum(x.right)
        else:
            y = x.parent
            while ((y != None) and (x == y.right)):
                x = y
                y = y.parent
            return y
        
    def tree_predecessor(self, x):
        if (x.left != None):
            return self.tree_maximum(x.left)
        else:
            y = x.parent
            while ((y != None) and (x == y.left)):
                x = y
                y = y.parent
            return y
    
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

    def transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v != None:
            v.parent = u.parent

    def tree_delete(self, z):
        if z.left == None:
            self.transplant(z, z.right)
        elif z.right == None:
            self.transplant(z, z.left)
        else:
            y = self.tree_minimum(z.right)
            if y.parent != z:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y

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

tree.inorder_tree_walk(tree.root)
print("\n")
tree.preorder_tree_walk(tree.root)
print("\n")
tree.postorder_tree_walk(tree.root)
