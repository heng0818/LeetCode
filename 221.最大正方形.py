#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
from typing import List
# dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ans = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                value = matrix[i][j]
                if value == '1':
                    if i > 0 and j > 0:
                        matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1]) + 1
                        ans = max(ans, matrix[i][j])
                    else:
                        matrix[i][j] = 1
                    ans = max(ans, matrix[i][j])
                else:
                    matrix[i][j] = 0
        return ans * ans

# @lc code=end
# matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix = [["0","1"],["1","0"]]
print(Solution().maximalSquare(matrix))
