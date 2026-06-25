class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        ans = 0
        n = len(nums)

        for i in range(n):
            cnt = 0

            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1

                length = j - i + 1

                if cnt * 2 > length:
                    ans += 1

        return ans