def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for k in range(low, high):
        if nums[k] < pivot:
            i += 1
            smaller = nums[k]
            nums[k] = nums[i]
            nums[i] = smaller
    i += 1
    nums[high] = nums[i]
    nums[i] = pivot
    return i

def quicksort(nums, low, high):
    if low > high:
        return
    pivot = partition(nums, low, high)
    quicksort(nums, low, pivot-1)
    quicksort(nums, pivot+1, high)
    return nums

print(quicksort([9,8,7,6,5,4,3,2,1], 0, 8))

