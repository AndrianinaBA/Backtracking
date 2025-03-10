def permutation(nums,curr= []):
    if len(nums) == len(curr):
        print(curr[:])
        return
    
    for num in nums :
        if num not in curr:
            curr.append(num)
            permutation(nums,curr)
            curr.pop()
    
permutation([1,2,3,4,5])
