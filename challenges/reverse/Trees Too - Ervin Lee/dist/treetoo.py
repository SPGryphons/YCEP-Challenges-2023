import random

# Things to study for my Computer Science exam:
# - Catalan numbers
# - Binomial coefficients
# - Factorials

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