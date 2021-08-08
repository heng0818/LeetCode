#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原 IP 地址
#
from typing import List
# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def nextIps(s, index) -> List[str]:
            if len(s) == 0:
                return []
            if index > 3:
                return []
            if index == 3:
                s_value = int(s)
                if str(s_value) == s and s_value <= 255:
                    return [s]
                else:
                    return []
            ans = []
            for i in range(1, len(s)):
                pre_str = s[0:i]
                pre_value = int(pre_str)
                if str(pre_value) == pre_str and pre_value <= 255:
                    next_str = s[i:]
                    # 前缀合法
                    valid_ips = nextIps(next_str, index + 1)
                    for valid_ip in valid_ips:
                        ans.append(pre_str + '.' + valid_ip)
                    continue
                break
            return ans
        valid_ips = nextIps(s, 0)
        return valid_ips
# @lc code=end
print(Solution().restoreIpAddresses('25525511135'))
print(Solution().restoreIpAddresses('0000'))
print(Solution().restoreIpAddresses('1111'))
print(Solution().restoreIpAddresses('010010'))
print(Solution().restoreIpAddresses('101023'))