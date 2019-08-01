"""
Given two singly linked lists that intersect at some point, 
find the intersecting node. The lists are non-cyclical.

For example, given 
A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, 
return the node with value 8.

In this example, assume nodes with the same value are the 
exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of 
the lists) and constant space.
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def traverse(root):

    while(root.next != None):
        print(root.value)
        root = root.next

    print(root.value, '\n')

def findintersection(root, rootalt):

    #find difference of counts
    countroot = 0
    countrootalt = 0
    temproot = root
    temprootalt = rootalt

    while(temproot != None):
        countroot += 1
        temproot = temproot.next

    while(temprootalt != None):
        countrootalt += 1
        temprootalt = temprootalt.next

    d = abs(countroot - countrootalt)
    print(countroot, countrootalt)
    #strategy if both are the same length
    while(root != None):
        if(d == 0):
            print(root.value, rootalt.value)
            if (root.value == rootalt.value):
                return root.value
            root = root.next
            rootalt = rootalt.next
        else:
            if countroot > countrootalt :
                root = root.next
                countroot -= 1
            elif countrootalt > countroot :
                rootalt = rootalt.next
                countrootalt -= 1
            d = abs(countroot - countrootalt)
            
first = Node(4, Node(3, Node(7, Node(8, Node(10)))))
second = Node(99, Node(1, Node(8, Node(10))))

print(findintersection(first, second))