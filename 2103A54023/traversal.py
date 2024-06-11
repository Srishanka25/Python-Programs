class Solution:
    def inOrderTraversal(self,root):
        answer=[]
        self.inordertraversalutil(root,answer)
        return answer
    def inOrderTraversalutil(self,root,answer):
        if root is None:
            return
        self.inOrderTraversalutil(root.left,answer)
        answer.append(root.val)
        self.inOrderTraversalutil(root.right,answer)
        return
    def issymmetric(self,root)
    tree=self.InorderTraversal(root)
    if tree ==tree[::-1]:
        return True
    return False

    