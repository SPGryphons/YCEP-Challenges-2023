import random
from binarytree import Node, tree, bst, heap, build

INT_MIN = -2**31
INT_MAX = 2**31

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

def tree(size):
    root = Node(random.randint(0, 100))
    for i in range(1, size):
        insert_node(root, random.randint(0, 100))
    return root

def insert_node(root, value):
    if not root:
        return Node(value)
    if random.random() < 0.5:
        root.left = insert_node(root.left, value)
    else:
        root.right = insert_node(root.right, value)
    return root

def search_node(root, value):
    if root is None:
        return False
    if root.value == value:
        return True
    return search_node(root.left, value) or search_node(root.right, value)

def findSomething(root, path, k):
    if root is None:
        return False
    path.append(root.value)
    
    if root.value == k:
        return True
    
    if ((root.left != None and findSomething(root.left, path, k)) or (root.right!= None and findSomething(root.right, path, k))):
        return True

    path.pop()
    return False

def getSomething(root, n1, n2):
    path1 = []
    path2 = []

    if (not findSomething(root, path1, n1) or not findSomething(root, path2, n2)):
        return -1
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]

root = tree()
n1 = random.randint(0, 100)
n2 = random.randint(0, 100)
search_n1 = search_node(root, n1)
search_n2 = search_node(root, n2)
while not search_n1 or not search_n2:
    n1 = random.randint(0, 100)
    n2 = random.randint(0, 100)
    search_n1 = search_node(root, n1)
    search_n2 = search_node(root, n2)