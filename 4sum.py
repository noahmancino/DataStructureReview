'''
This one took me too long (~50 minutes) and even taking too long, my solution is ugly. Actually most of my time was spent debugging
things that showed my python knowledge was rusty rather than actually making an algorithmic mistake. This also brings
back vague memories of the catalan sequence in my discrete mathematics class.
'''

def parens(n):
    if n == 1:
        return [['(', ')']]
    else:
        solutions = []
        sub = parens(n-1)
        for sub_sol in sub:
            for i in range(len(sub_sol) + 1):
                cpy = sub_sol[:]
                cpy.insert(i, '(')
                for j in range(i + 1, len(sub_sol) + 2):
                    new_cpy = cpy[:]
                    new_cpy.insert(j, ')')
                    solutions.append(new_cpy)

    tuple_set = set(map(tuple, solutions))
    return list(map(list, tuple_set))


parens = parens(8)
parens = list(map("".join, parens))
print(parens)
print(len(parens))