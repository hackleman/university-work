"""
Given the root to a binary search tree, find the second largest node in the tree.
"""
import numpy as np


class Node:
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data

class Solution:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left,data)
                root.left=cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        return root
  

myTree = Solution()
root = None
parent = None
input = np.random.randint(100, size = 10)
print(np.sort(input))

for i in range(10):
    data = input[i]
    root = myTree.insert(root,data)

def reverseinorder(root, c):

    if root == None:
        return
    
    reverseinorder(root.right, c)

    if len(c) > 1:
        return

    c.append(root.data)


    reverseinorder(root.left, c)

c = []

reverseinorder(root, c)
print(c, c[1])