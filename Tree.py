# Python program for preorder traversals

# Structure of a Binary Tree Node
class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

def printPreorder(node):
    if node is None:
        return
    print(node.data, end=' ')
    printPreorder(node.left)
    printPreorder(node.right)

def printPreorderIt(node):
    if root is None:
        return
    
    stack = []
    stack.append(node)
    
    while stack:
        node = stack.pop()
        print (node.data, end=" ")
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
            

    
    
def printInorder(node):
    if node is None:
        return
    
    printInorder(node.left)
    print(node.data, end=' ')
    printInorder(node.right)


def printPostorder(node):
    if node is None:
        return

    printPostorder(node.left)
    printPostorder(node.right)
    print(node.data, end=' ')

def lowAncestor(root, val1, val2):
    if root is None:
        return None
    
    if root.data > val1 and root.data > val2:
        return lowAncestor(root.left, val1, val2)
    
    if root.data < val1 and root.data < val2:
        return lowAncestor(root.right, val1, val2)
    
    return root.data
     
    


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    printPreorder(root)
    print()
    printPreorderIt(root)
    print()

    root1 = Node(20)
    root1.left = Node(8)
    root1.right = Node(22)
    root1.left.left = Node(4)
    root1.left.right = Node(12)
    root1.left.right.left = Node(10)
    root1.left.right.right = Node(14)
    print(lowAncestor(root1, 4, 14))