class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, node, data):
        if self.root is None:
            self.root = Node(data)
            return
        if node is None:
            return Node(data)
        elif data>node.data:
            node.right = self.insert(node.right,data)
        elif data<node.data:
            node.left = self.insert(node.left,data)
        return node #Seems important don forget

    # Search
    def search(self, key):
        node = self.root
        while node is not None:
            if node.data==key:
                return True
            if key>node.data:
                node = node.right
            else:
                node = node.left

    # Minimum value in a subtree
    def min_node(self, node):
        while node.left is not None:
            node = node.left
        return node

    # Delete
    def delete(self,node,key):
        if self.root is None:
            return
        if key<node.data:
            node.left = self.delete(node.left,key)
        elif key>node.data:
            node.right = self.delete(node.right,key)
        else:
            if node.right is None and node.left is None:
                return None
            elif node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                successor = self.min_node(node.right)
                node.data = successor.data
                node.right = self.delete(node.right, successor.data)
        return node

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=" ")
            self.inorder(node.right)

def main():
    bst = BST()
    for x in [50, 30, 70, 20, 99, 40, 60, 80]:
        bst.insert(bst.root,x)

    print("Inorder:  ", end="")
    bst.inorder(bst.root)

    print("\nSearch 60:", bst.search(60))
    print("Search 99:", bst.search(99))

    bst.delete(bst.root,50)
    bst.delete(bst.root,70)
    bst.inorder(bst.root)


main()