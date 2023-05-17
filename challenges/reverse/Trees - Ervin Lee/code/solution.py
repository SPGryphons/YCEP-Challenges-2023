import random
from binarytree import Node, tree, bst, heap, build

INT_MIN = -2**31
INT_MAX = 2**31

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

def generate_random_binary_tree(size):
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

# Function to count the number of binary search trees within a random binary tree.
def number_of_binary_search_trees(root):
    if root is None:
        return 0, INT_MIN, INT_MAX, True
    if root.left is None and root.right is None:
        return 1, root.value, root.value, True
    L = number_of_binary_search_trees(root.left)
    R = number_of_binary_search_trees(root.right)

    BST = [0] * 4
    BST[2] = min(root.value, (min(L[2], R[2])))
    BST[1] = max(root.value, (max(L[1], R[1])))

    if L[3] and R[3] and root.value > L[1] and root.value < R[2]:
        BST[0] = L[0] + R[0] + 1
        BST[3] = True

    else:
        BST[0] = L[0] + R[0]
        BST[3] = False
    
    return BST


def main():
    root = generate_random_binary_tree(75)
    print(root)
    n = number_of_binary_search_trees(root)[0]
    user_input = int(input("How many binary search trees are present in this binary tree? >>> "))
    if user_input == n:
        print("Correct!")
        with open('flag.txt', 'r') as f:
            print(f.read())
    else:
        print("Incorrect!")

if __name__ == '__main__':
    main()