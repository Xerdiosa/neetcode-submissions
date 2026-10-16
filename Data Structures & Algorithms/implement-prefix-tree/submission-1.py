class PrefixTree:

    def __init__(self):
        self.start = dict()

    def insert(self, word: str) -> None:
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
        n = self.start
        for i in list(word):
            if i in n:
                n = n[i]
            else:
                return False
        return "end" in n

    def startsWith(self, prefix: str) -> bool:
        n = self.start
        for i in list(prefix):
            if i in n:
                n = n[i]
            else:
                return False
        return True
        
        