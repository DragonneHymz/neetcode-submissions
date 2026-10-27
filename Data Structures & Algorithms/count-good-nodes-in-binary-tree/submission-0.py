# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque()
        queue.append((root,float("-inf")))
        res = 0
        while queue:
            for i in range(len(queue)):
                node, maxRoot = queue.popleft()

                if node and node.val >= maxRoot:
                    res+=1

                if node:
                    queue.append((node.left, max(maxRoot, node.val)))
                    queue.append((node.right, max(maxRoot, node.val)))
        return res
