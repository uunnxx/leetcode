class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # curr = 0
        # original = nums
        #
        # def sum_it(nums, target, current=1):
        #     nonlocal curr
        #     curr += current
        #     if len(nums) < 1:
        #         return 1
        #
        #     for i in range(len(nums)-1):
        #         print(f"Adding {nums[0]} to {nums[i+1]} to get {target}")
        #         if nums[0] + nums[i+1] == target:
        #             first = original.index(nums[0])
        #             second = original.index(nums[i+1], first+1)
        #             print(f"target found {target}: at {[original.index(nums[0]), original.index(nums[i+1])]}")
        #             return [first, second]
        #
        #     print(f"Iteration: {current} list: {nums}")
        #
        #     return sum_it(nums[current:], target, 1)
        # return sum_it(nums, target)
        #
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                # if nums[i] + nums[j] == target:
                #     print(f"{nums[i]} + {nums[j]} == target: {target}")
                #     print(f"index of them: {nums.index(nums[i])}, {nums.index(nums[j], nums[i]+1)}")
                #     print('ye')
                #     first = nums.index(nums[j])
                #     second = nums.index(nums[i], first + 1)
                    # return [first, second]
                print(f"i: {i}, j: {j}")
                print(f"e_i: {nums[i]}, e_j: {nums[j+1]}")
        return []


n = Solution()

p = n.twoSum([1, 11, 15, 7, 1, 3, 3, 4, 2], 9)
# p = n.twoSum([3, 3], 6)

print(p)
