# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        queue = [root]
        isFirst = root.val
        queue.append(None)
        while (len(queue)>=1):
            start = queue.pop(0)
            if(len(queue) >=1 and start == None):
                queue.append(None)
                isFirst = queue[0].val
                continue
            elif start == None:
                break
            print(start.val)
            if start.left != None: 
                queue.append(start.left)
            if start.right != None: 
                queue.append(start.right)
        return isFirst
    def constructTree(self,nums):
        """
        :rtype : root
        """
        start = None
        for i in nums:
            temp = TreeNode(i)
            temp.left = start
            start = temp
        return start
sol = Solution()
root = sol.constructTree([2,1,3])
print(sol.findBottomLeftValue(root))