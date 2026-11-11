class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charmap = dict()
        for i in range(len(list(order))):
            charmap[order[i]]=i
        for i in range(1, len(words)):
            idx=0
            if words[i]==words[i-1]:
                continue
            while True:
                if idx>=len(words[i]) or idx>=len(words[i-1]):
                    if len(words[i-1])>len(words[i]):
                        # print(words[i-1], words[i])
                        return False
                    break
                if charmap[words[i-1][idx]]>charmap[words[i][idx]]:
                    # print(words[i-1],words[i],idx, charmap[words[i-1][idx]],charmap[words[i][idx]])
                    return False
                if charmap[words[i-1][idx]]<charmap[words[i][idx]]:
                    break
                idx+=1 
        return True