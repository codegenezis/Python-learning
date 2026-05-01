from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # solution 1
        # res = ''
        # for i in range(len(strs[0])):
        #     # print('=>', strs[0][i], i)
        #     for string in strs:
        #         # print('==> 1', string, i, string[i])
        #         if i == len(string) or string[i] != strs[0][i]:
        #             # print('==> 2', string, i, string[i])
        #             return strs[0][:i]
        #     res += strs[0][i]
        # return res

        # solution 2
        
        if not strs:
            return ""
        prefix = strs[0]

        for s in strs[1:]:
            print('=>1', s)
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                print('=>2', prefix)
                if not prefix:
                    return ''
        return prefix

         
# Example usage:
solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))



