# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: , q: ):
        if (not p) and (not q):  # both is None 
            return True
        if (not p) or (not q): # one of tree is None
            return False
        if p.val != q.val: # root value is different
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class Solution:
    def isSymmetric2Tree(self, root1, root2):
        if (not root1) and (not root2):
            return True
        if (not root1) or (not root2):
            return False
        if root1.val != root2.val:
            return False
        return self.isSymmetric2Tree(root1.left, root2.right) and self.isSymmetric2Tree(root1.right, root2.left)
    
    def isSymmetric(self, root: ):
        return self.isSymmetric2Tree(root.left, root.right)

class Solution:
    def heightTree(self, root):
        if not root:
            return -1
        # if (not root.left) and (not root.right):
        #     return 0
        return 1 + max(self.heightTree(root.left), self.heightTree(root.right))        
    
    def isBalanced(self, root: ):
        if not root:
            return True 
        a = self.heightTree(root.left)
        b = self.heightTree(root.right)
        return abs(a-b) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

class Solution:
    def invertTree(self, root: ) :
        if not root:
            return None
        if (not root.left) and (not root.right):
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root
        
class Solution:
    def isValidBST(self, root: ):
        def valid(root, left, right):
            if not root:
                return True
            if not (root.val > left and root.val < right):
                return False
            return valid(root.left, left, root.val) and valid(root.right, root.val, right)
        return valid(root, float("-inf"), float("inf"))

class Solution:
    def countNodes(self, root: )  int:
        if root == None:
            return 0
        return 1+self.countNodes(root.left)+self.countNodes(root.right)

class Solution:
    def searchBST(self, root: , val: int) :
        if root == None:
            return None
        if root.val == val:
            return root
        if root.val < val:
            return self.searchBST(root.right, val)
        return self.searchBST(root.left, val)
        
class Solution:
    def maxDepth(self, root: )  int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))

class Solution:
    def minDepth(self, root: )  int:
        if not root:
            return 0
        if (not root.left) and (not root.right):
            return 1
        if not root.left and root.right:
            return 1 + self.minDepth(root.right)
        if not root.right and root.left:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))  

class Solution:
    def dicElements(self, root):
        if root == None:
            return []
        return [root.val] + self.dicElements(root.left) + self.dicElements(root.right)
      
    def findMode(self, root: )  List[int]:
        a = self.dicElements(root)
        d = {}
        for e in a:
            d[e] = d.get(e, 0)+1
        m = max(d.values())
        res = []
        for key in d:
            if d[key] == m:
                res.append(key)
        return res        

class Solution:
    def insertIntoBST(self, root: , val: int) :
        if root == None:
            return TreeNode(val)
        if val > root.val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root 

class Solution:
    def balancedTree(self, nums, left, right):
        if left > right:
            return None
        mid = int(0.5*(left + right))
        node = TreeNode(nums[mid])
        node.left = self.balancedTree(nums, left, mid - 1)
        node.right = self.balancedTree(nums, mid + 1, right)
        return node
    
    def sortedArrayToBST(self, nums: List[int]) :
        return self.balancedTree(nums, 0, len(nums)-1)

class Solution:
    def leafSq(self, root):
        if (not root.left) and (not root.right):
            return [root.val]
        if (root.left) and (root.right):
            return self.leafSq(root.left)+self.leafSq(root.right)
        if (not root.left) and (root.right):
            return self.leafSq(root.right)
        if (root.left) and (not root.right):
            return self.leafSq(root.left)
        
    def leafSimilar(self, root1: , root2: ):
        leaf1 = self.leafSq(root1)
        leaf2 = self.leafSq(root2)
        return leaf1 == leaf2

class Solution:
    def mergeTrees(self, root1: , root2: ) :
        if root1 == None and root2 == None:
            return None
        if root1 != None and root2 == None:
            return root1
        if root1 == None and root2 != None:
            return root2
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1

                                                                                                              