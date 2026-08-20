class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        subarray_count = Counter()

        for i in range(n-k+1):
            unique_elements = set(nums[i:i+k])
            for num in unique_elements:
                subarray_count[num] += 1
        ans = -1
        for num , count in subarray_count.items():
            if count == 1:
                ans = max(ans,num)
        return ans

        