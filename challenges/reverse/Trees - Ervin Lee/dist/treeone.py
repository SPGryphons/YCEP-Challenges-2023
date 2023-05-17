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

# TO-DO: Searching for other fellow trees searching for other trees within the mother tree.
#             .        +          .      .          .
#      .            _        .                    .
#   ,              /;-._,-.____        ,-----.__
#  ((        .    (_:#::_.:::. `-._   /:, /-._, `._,
#   `                 \   _|`"=:_::.`.);  \ __/ /
#                       ,    `./  \:. `.   )==-'  .
#     .      ., ,-=-.  ,\, +#./`   \:.  / /           .
# .           \/:/`-' , ,\ '` ` `   ): , /_  -o
#        .    /:+- - + +- : :- + + -:'  /(o-) \)     .
#   .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
#    `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
#               \:  `  X` _| _,\/'   .-'
# .               ":._:`\____  /:'  /      .           .
#                     \::.  :\/:'  /              +
#    .                 `.:.  /:'  }      .
#            .           ):_(:;   \           .
#                       /:. _/ ,  |
#                    . (|::.     ,`                  .
#      .                |::.    {\
#                       |::.\  \ `.
#                       |:::(\    |
#               O       |:::/{ }  |                  (o
#                )  ___/#\::`/ (O "==._____   O, (O  /
#           ~~~w/w~"~~, :/,-(~"~~~~~~~~"~o~\~/~w|/~
# dew   ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~
