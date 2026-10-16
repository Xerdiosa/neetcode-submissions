class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictoftuples = dict()
        for i in strs:
            anagram = [0 for i in range(26)]
            for j in list(i):
                anagram[ord(j)-97]=anagram[ord(j)-97]+1
            tupleanagram = tuple(anagram)
            if tupleanagram not in dictoftuples:
                dictoftuples[tupleanagram] = [i]
            else:
                dictoftuples[tupleanagram].append(i)
        return list(dictoftuples.values())
