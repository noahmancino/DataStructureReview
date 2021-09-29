'''
Lightly disguised binary search. Coding it out took awhile and it's not pretty but I got the idea pretty fast, I think.
Probably breaks for some edge cases but can't be bothered to thorough test it at the moment
'''


def solution(nums, target):
    '''
    If the area is rotated, then we know the first element in the array is the smallest in its segment. Therefore,
    we can do a binary search for the first index in the array with a smaller element. After that, we can do two binary
    searches, one on each of the segments.
    '''

    def binary_search(nums, left_bound, right_bound, targ):
        middle = left_bound + ((right_bound - left_bound) // 2)
        if nums[middle] == targ:
            return middle
        if left_bound >= right_bound:
            return - 1
        if nums[middle] > targ:
            return binary_search(nums, left_bound, middle - 1, targ)
        if nums[middle] < targ:
            return binary_search(nums, middle + 1, right_bound, targ)

    if nums[0] < nums[-1]:
        return binary_search(nums, 0, len(nums) - 1, target)

    if len(nums) == 1:
        if nums[0] == target:
            return 0
        else:
            return -1

    middle = (len(nums) - 1) // 2
    left_bound = 0
    right_bound = len(nums) - 1
    while left_bound <= right_bound:
        if nums[middle] < nums[middle - 1]:
            left_search = binary_search(nums, middle, len(nums) - 1, target)
            right_search = binary_search(nums, 0, middle - 1, target)
            return max([left_search, right_search])
        elif nums[middle] > nums[0]:
            left_bound = middle + 1
            middle = left_bound + (right_bound - left_bound) // 2
        elif nums[middle] < nums[0]:
            right_bound = middle - 1
            middle = left_bound + (right_bound - left_bound) // 2


print(solution([3, 2, 0, 1], 0))
