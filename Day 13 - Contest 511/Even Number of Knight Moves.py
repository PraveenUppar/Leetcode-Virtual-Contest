class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:

        x1, y1 = start
        
        x2, y2 = target
        
        start_parity = (x1 + y1) % 2
        target_parity = (x2 + y2) % 2
        
        return start_parity == target_parity
        
        
        
# a knight can only land on the target square in an even number of moves if the target square is the same color as the starting square.