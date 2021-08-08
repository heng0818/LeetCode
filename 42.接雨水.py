#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#
from typing import List
# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        return self.func1(height)

    # 自低向上查（超时）
    def func1(self, height: List[int]) -> int:
        ans = 0
        max_h = max(height)
        left, right = 0, len(height) - 1
        while max_h > 0:
            # 找到两边的墙
            found = False
            while right - left > 1:
                if height[left] != 0 and height[right] != 0:
                    # 找到两堵墙
                    found = True
                    break
                if height[left] == 0:
                    left += 1
                if height[right] == 0:
                    right -= 1    

            if found:
                i = left
                while i <= right:
                    if i != left and i != right and height[i] == 0:
                        ans += 1
                    # 修改墙数据
                    height[i] = max(0, height[i] - 1)
                    i += 1
            max_h -= 1
        return ans
# @lc code=end
print(Solution().trap([4,2,0,3,2,5]))
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
