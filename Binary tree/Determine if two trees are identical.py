
#Represent a node of binary tree
class Node:
    def __init__(self,data):
        #Assign data to the new node, set left and right children to None
        self.data = data;
        self.left = None;
        self.right = None;

class IdenticalTrees:
    def __init__(self):
        #Represent the root of binary tree
        self.root = None;

    #areIdenticalTrees() finds whether two trees are identical or not
    @staticmethod
    def areIdenticalTrees(root1, root2):
        #Checks if both the trees are empty
        if(root1 == None and root2 == None):
            return True;
        #Trees are not identical if root of only one tree is null thus, return false
        if(root1 == None and root2 == None):
            return True;
        #If both trees are not empty, check whether the data of the nodes is equal
        #Repeat the steps for left subtree and right subtree
        if(root1 != None  and root2 != None):
            return ((root1.data == root2.data) and
            (IdenticalTrees.areIdenticalTrees(root1.left, root2.left)) and
            (IdenticalTrees.areIdenticalTrees(root1.right, root2.right)));
        return False;

#Adding nodes to the first binary tree
bt1 = IdenticalTrees();
bt1.root = Node(1);
bt1.root.left = Node(2);
bt1.root.right = Node(3);
bt1.root.left.left = Node(4);
bt1.root.right.left = Node(5);
bt1.root.right.right = Node(6);

#Adding nodes to the second binary tree
bt2 = IdenticalTrees();
bt2.root = Node(1);
bt2.root.left = Node(2);
bt2.root.right = Node(3);
bt2.root.left.left = Node(4);
bt2.root.right.left = Node(5);
bt2.root.right.right = Node(6);

#Displays whether both the trees are identical or not
if(IdenticalTrees.areIdenticalTrees(bt1.root, bt2.root)):
    print("Both the binary trees are identical");
else:
    print("Both the binary trees are not identical");