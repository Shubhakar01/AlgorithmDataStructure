class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        curr = self.root
        while True:
            if data < curr.data:
                if not curr.left:
                    curr.left = new_node
                    break
                curr = curr.left
            elif data > curr.data:
                if not curr.right:
                    curr.right = new_node
                    break
                curr = curr.right
            else:
                # Duplicate datas not inserted
                break

    def search(self, data):
        curr = self.root
        while curr:
            if data == curr.data:
                return curr
            elif data < curr.data:
                curr = curr.left
            else:
                curr = curr.right
        return None

    def delete(self, data):
        parent = None
        curr = self.root

        # Find the node to delete and its parent
        while curr and curr.data != data:
            parent = curr
            if data < curr.data:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            return  # Node not found

        # Case 1: Node has 0 or 1 child
        if not curr.left or not curr.right:
            child = curr.left if curr.left else curr.right
            
            if not parent:
                self.root = child
            elif parent.left == curr:
                parent.left = child
            else:
                parent.right = child

        # Case 2: Node has 2 children
        else:
            # Find the in-order successor (minimum in the right subtree)
            succ_parent = curr
            succ = curr.right
            while succ.left:
                succ_parent = succ
                succ = succ.left

            # Copy successor's value to current node
            curr.data = succ.data

            # Delete the successor node
            if succ_parent.left == succ:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right

    def inorder_traversal(self):
        result = []
        stack = []
        curr = self.root

        while curr or stack:
            # Reach the leftmost node of the curr node
            while curr:
                stack.append(curr)
                curr = curr.left

            # Current must be None at this point
            curr = stack.pop()
            result.append(curr.data)

            # We have visited the node and its left subtree. Now, it's right subtree's turn
            curr = curr.right

        return result

bst = BinarySearchTree()

# Insertion
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

# In-order Traversal (will output sorted order: [20, 30, 40, 50, 60, 70, 80])
print("In-order:", bst.inorder_traversal())

# Searching (returns the node object if found, or None)
node = bst.search(40)
print("Found:", node.data if node else "Not Found")

# Deletion (deleting node with two children)
bst.delete(50)
print("In-order after deleting 50:", bst.inorder_traversal())