def numIdenticalPairs(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    good_pairs = 0
    for key in count:
        n = count[key]
        if n > 1:
            good_pairs += (n * (n - 1)) // 2
    
    return good_pairs

nums=list(map(int,input().split()))

