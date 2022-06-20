def answer(nums):

    result = []

    if (len(nums)) == 1:
        return [nums[:]]

    for i in range(len(nums)):

        n = nums.pop(0)
        perms = answer(nums)
        
        for perm in perms:
            perm.append(n)
        
        result.extend(perms)
        nums.append(n)

    return result

if __name__ == "__main__":

    nums = [1,2,3]

    print(answer(nums))