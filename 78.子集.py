#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        def _subsets(sub_nums: List[int]) -> List[List[int]]:
            res = []
            for i in range(0, len(sub_nums)):
                num = sub_nums[i]
                next_nums = sub_nums[i+1:]
                sub_sets = _subsets(next_nums)
                res.append([num])
                if len(sub_sets) > 0:
                    for sub_set in sub_sets:
                        cur_set = [num]
                        cur_set += sub_set
                        res.append(cur_set)
            return res
        ans = _subsets(nums)
        ans.append([])
        return ans
# @lc code=end
print(Solution().subsets([1,2,3]))

