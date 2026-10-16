class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastSeen = dict()
        for i, v in enumerate(nums):
            if v in lastSeen:
                if abs(i-lastSeen[v]) <= k:
                    return True
            lastSeen[v] = i
        return False