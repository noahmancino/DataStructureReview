'''
This works n^2 time. If you want to remove duplicate numbers instead of duplicate coordinates, that is trivial (add sets to the set instead of adding tuples to the set). Missed the optimal method but better than brute
force.
'''

def two_sum(num_list):
    sums_dict = {}
    for i, num1 in enumerate(num_list):
        for j, num2 in enumerate(num_list[i + 1:]):
            j += i + 1
            sum = num1 + num2
            if sum in sums_dict.keys():
                sums_dict[sum].append((i, j))
            else:
                sums_dict[sum] = [(i, j)]

    return sums_dict


def three_sum(num_list):
    solution_set = set()
    two_sums = two_sum(num_list)
    for i, num1 in enumerate(num_list):
        if -num1 in two_sums.keys():
            for j, k in two_sums[-num1]:
                if j > i and k > i:
                    solution_set.add((num_list[i], num_list[j], num_list[k]))

    return solution_set


print(three_sum([-1, 0, 1, 2, -1, -4]))
