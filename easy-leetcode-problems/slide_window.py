def findMaxAverage(nums, k):
    if len(nums)<k:
        return "array is less then window k"
    window_sum = sum(nums[0:k])      # шаг 0
    max_sum = window_sum

    for right in range(k, len(nums)):
        window_sum=window_sum-nums[right-k]+nums[right]
        # используйте формулу из таблицы: window_sum = window_sum - ушедший + пришедший
        if window_sum>max_sum:
            max_sum=window_sum
        # обновите max_sum, если новая сумма больше

    return max_sum / k

print(findMaxAverage([1, 12, -5, -6, 50, 3], 4))    # 12.75
print(findMaxAverage([5], 1))                          # 5.0