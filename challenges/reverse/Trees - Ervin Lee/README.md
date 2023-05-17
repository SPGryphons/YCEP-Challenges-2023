# Trees
===

## Summary
* **Author:** Ervin Lee
* **Discord Tag:** perspectives#9963
* **Category:** Reverse Engineering / Programming
* **Difficulty:** Hard

## Solution
1. The progam is an algorithm to count the number of binary search trees within a binary tree
2. Binary tree is randomly generated and visualized
3. Binary tree is traversed and the number of binary search trees within it is counted
4. Algorithm is as per solution.py

## Flag
```
YCEP2023{TR335_AR3_Y0Ur_835t_Fr13nd5_T00!}
```

## Solving Algorithm 
```python
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
```