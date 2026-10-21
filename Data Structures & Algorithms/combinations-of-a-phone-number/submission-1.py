class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        dct = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        ans = []
        tmp = []
        def helper(idx):
            if idx == len(digits):
                ans.append("".join(tmp))
                return
            for letter in dct[digits[idx]]:
                tmp.append(letter)
                helper(idx+1)
                tmp.pop()

        helper(0)
        return ans
        