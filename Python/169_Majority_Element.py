from heapq import merge


def answer(nums):

    mergesort(nums)

    return nums[len(nums)//2] 

def mergesort(nums):
    if len(nums) > 1:
        r = len(nums)//2
        L = nums[:r]
        M = nums[r:]
        mergesort(L)
        mergesort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = M[j]
                j += 1
            k+= 1
        
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            nums[k] = M[j]
            j += 1
            k += 1


if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(answer(nums))