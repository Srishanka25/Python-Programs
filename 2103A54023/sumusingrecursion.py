def sum(nums):
    if not nums:
        return 0
    else:
        return nums[0] + sum(nums[1:])
numbers = list(map(int,input().split()))
result = sum(numbers)
print(result)
      
         