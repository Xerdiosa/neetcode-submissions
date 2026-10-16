class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(self.inverse(i))
            if i == ")" or i == "}" or i == "]":
                if len(stack) == 0:
                    return False
                if stack.pop() != i:
                    return False
            print(stack)
        return len(stack) == 0

    def inverse(self, i: str) -> str:
        if i == "(":
            return ")"
        if i == "[":
            return "]"
        if i == "{":
            return "}"
        return "undefined"