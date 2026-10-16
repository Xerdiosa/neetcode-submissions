class WordDictionary:

    def __init__(self):
        self.start = dict()
        

    def addWord(self, word: str) -> None:
        n = self.start
        for i in list(word):
            if i in n:
                n = n[i]
                continue
            n[i] = dict()
            n=n[i]
        if "end" not in n:
            n["end"] = True

    def search(self, word: str) -> bool:
        return self._search(0, word, self.start)

    def _search(self, idx:int, word:str, n:dict) -> bool:
        if idx == len(word):
            return isinstance(n,dict) and "end" in n
        if word[idx] == ".":
            match = False
            for dots in n.values():
                match = match or self._search(idx+1, word, dots)
            return match
        if word[idx] in n:
            return self._search(idx+1, word, n[word[idx]])
        else:
            return False
        