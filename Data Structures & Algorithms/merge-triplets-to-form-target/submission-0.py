class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cana, canb, canc = False, False, False
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:
                cana = True
            if triplet[1] == target[1] and triplet[0] <= target[0] and triplet[2] <= target[2]:
                canb = True
            if triplet[2] == target[2] and triplet[1] <= target[1] and triplet[0] <= target[0]:
                canc = True
        return cana and canb and canc