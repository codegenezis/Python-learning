
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")": "(",
            "]": "[",
            "}": "{" 
        }

        for c in s:
            # print("c:", c)
            if c in closeToOpen:
                # print(stack, stack[-1])
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False

callParen = Solution()
print(callParen.isValid("()"))
print(callParen.isValid("[]"))
print(callParen.isValid("(}"))

# Time complexity = O(n)
# Creating Hash Map  closeToOpen
