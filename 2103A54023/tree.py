def totalSum(self,root):
    if root is None:
        return 0
    else:
        leftsum=totalSum(root,left)
        rightsum=totalsum(root.right)
        return root.data+leftsum+rightsum
    
def treeMax(self,root):
    if root is None:
        return 0
    else:
        leftMax=treeMax(root,left)
        rightMax=treeMax(root,right)
        return max(root.data,leftMax,rightMax)
def treeHeight(self,root):
    if root is None:
        return 0
    else:
        leftHeight=treeHeight(root.left)
        rightHeight=treeHeight(root.right)
        return 1 + max(leftHeight,rightHeight)
def existInTree(self,root,value):
    if root is None:
        return False
    else:
        inLeft=existInTree(root.left,value)
        inRight=existIntree(root.right,value)
        return root.data==value or inLeft or inRight
def reverseTree(self,root):
    if root is None:
        return
    else:
        reverseTree(root.left)
        reverseTree(root.right)
        root.left,root.right=root.right,root.left
    
 
