class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lst = [0 for _ in range(26)]
        s1lst = [0 for _ in range(26)]
        if s1 == s2:
            return True
        for i in s1:
            s1lst[ord(i)-97] = s1lst[ord(i)-97] + 1 
        for i in range(len(s2)):
            if i < len(s1):
                lst[ord(s2[i])-97] = lst[ord(s2[i])-97] + 1 
            else:
                print(lst)
                print(s1lst)
                print()
                if tuple(lst) == tuple(s1lst):
                    return True
                lst[ord(s2[i-len(s1)])-97] = lst[ord(s2[i-len(s1)])-97] - 1
                lst[ord(s2[i])-97] = lst[ord(s2[i])-97] + 1 
                if tuple(lst) == tuple(s1lst):
                    return True
        if tuple(lst) == tuple(s1lst):
            return True        
        return False
