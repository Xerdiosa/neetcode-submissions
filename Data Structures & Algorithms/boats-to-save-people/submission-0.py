class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        count = 0
        # print(left,right,people)
        while left <= right:
            print(left,right,count)
            if people[left]+people[right] <= limit:
                left+=1
                right-=1
                count+=1
            else:
                right-=1
                count+=1
        return count