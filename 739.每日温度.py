#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
from typing import List
# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(0, len(temperatures)):
            while len(stack) > 0 and stack[-1][1] < temperatures[i]:
                # 栈中温度低于当前温度的需要被排除
                days = i - stack[-1][0]
                ans[stack[-1][0]] = days
                stack.pop()
            stack.append((i, temperatures[i]))
        return ans
# @lc code=end
print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
print(Solution().dailyTemperatures([30,40,50,60]))
print(Solution().dailyTemperatures([30,60,90]))
