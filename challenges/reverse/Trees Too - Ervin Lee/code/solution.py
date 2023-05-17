import random
from binarytree import Node
def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def binomial_coefficient(n, k):
    res = 1
    if (k > n - k):
        k = n - k
    
    for i in range(0, k):
        res *= (n - i)
        res //= (i + 1)
    return res

def catalan(n):
    c = binomial_coefficient(2 * n, n)
    return c // (n + 1)

def count_binary_search_trees(n):
    count = catalan(n)
    return count

def count_binary_trees(n):
    count = catalan(n)
    return count * factorial(n)

def main():
    n = random.randint(500, 1000)  # Replace with desired number of nodes
    binary_search_trees = count_binary_search_trees(n)
    binary_trees = count_binary_trees(n)

    q1 = int(input("How many binary search trees can be formed with " + str(n) + " nodes? "))
    if q1 == binary_search_trees:
        print("Correct!")
        q2 = int(input("How many binary trees can be formed with " + str(n) + " nodes? "))
        if q2 == binary_trees:
            print("Correct!")
            with open('flag.txt', 'r') as f:
                print(f.read())
        else:
            print("Incorrect!")
    else:
        print("Incorrect!")

if __name__ == '__main__':
    main()
