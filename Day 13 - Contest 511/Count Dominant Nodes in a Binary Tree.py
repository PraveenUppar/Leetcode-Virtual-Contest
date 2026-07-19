class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        
        self.count = 0
        def get_subtree_max(node: TreeNode | None) -> float:
            
            if not node:
                return float('-inf')
            
            left_max = get_subtree_max(node.left)
            right_max = get_subtree_max(node.right)
            
            current_max = max(node.val, left_max, right_max)
            
            if node.val == current_max:
                self.count += 1
                
            return current_max

        get_subtree_max(root)
        return self.count
