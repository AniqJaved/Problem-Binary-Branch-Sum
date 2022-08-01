#######################################
##Inserting nodes in binary search tree
#######################################

class Node:
    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
    # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Use the insert method to add nodes
root = Node(27)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.insert(22)

########################################
##Calculating branch sums in binary tree
########################################


def branchSum(root):
    sums = []
    checkSum(root,0,sums)
    return sums
def checkSum(root,runningsum,sums):
    if root is None:
        return
    runningsum = runningsum + root.data
    if root.left is None and root.right is None:
        sums.append(runningsum)
        return
    checkSum(root.left,runningsum,sums)
    checkSum(root.right,runningsum,sums)
    

sums = branchSum(root)

print(sums)


    
