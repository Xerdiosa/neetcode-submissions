class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        return len(self.findOrder(numCourses, prerequisites))>0
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pm = [[] for _ in range(numCourses)]
        visited = set()
        learned = set()
        ans = []
        for prerequisite in prerequisites:
            pm[prerequisite[0]].append(prerequisite[1])
        print(pm)
        def helper(i):
            if i in visited:
                raise Exception("loop detected!")
            visited.add(i)
            for prerequisite in pm[i]:
                if prerequisite in learned:
                    continue
                helper(prerequisite)
            learned.add(i)
            ans.append(i)
        try:
            for i in range(numCourses):
                if i not in learned:
                    helper(i)
            return ans
        except Exception as e:
            print(e)
            return []