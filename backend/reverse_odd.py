def min_sub_array_len(target : int, nums : [int]) -> int:

    n = len(nums)
    prefix_sum = [0] * (n + 1)

    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + nums[i]

    min_len = float('inf')


print(min_sub_array_len(4, [1, 4, 4]))
