class Solution:
    def filterOccupiedIntervals(self, occupiedIntervals: List[List[int]], freeStart: int, freeEnd: int) -> List[List[int]]:

        if not occupiedIntervals:
            return []

        occupiedIntervals.sort(key=lambda x: x[0])
    
        merged = [occupiedIntervals[0][:]]
        for start, end in occupiedIntervals[1:]:
            current = merged[-1]
            if start - current[1] <= 1: 
                current[1] = max(current[1], end)
            else:
                merged.append([start, end])
    
        result = []
        for s, e in merged:
            if e < freeStart or s > freeEnd:
                result.append([s, e])
            else:
                if s < freeStart:
                    result.append([s, freeStart - 1])
                if e > freeEnd:
                    result.append([freeEnd + 1, e])
    
        return result
