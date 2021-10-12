'''
I thought this one was much, much easier than the leetcode hard I did earlier today (n-queens). Took me less
than 5 minutes to come up with this linear time complexity solution.
'''

def longest_valid(parens):
    stack = []
    max_range = (0, 0)
    for i, paren in enumerate(parens):
        if paren == ')':
            if stack:
                open_index = stack.pop()
                if (i - open_index) > (max_range[1] - max_range[0]):
                    max_range = (open_index, i)
        else:
            stack.append(i)

    return parens[max_range[0]:max_range[1]+1]

print(longest_valid("(())))))))))"))