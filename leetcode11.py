'''
I found this brute force method quickly but I should have seen the optimal method
'''

def solution(heights):
    max_area = 0
    for i, height1 in enumerate(heights):
        trimmed_heights = heights[i+1:]
        for j, height2 in enumerate(trimmed_heights):
            i += 1
            j += i + 1
            area = (abs(j - i)) * min([height1, height2])
            print(f'heights: {height1}, {height2}\tarea: {area}\tmaxarea: {max_area}')
            max_area = max([max_area, area])

    return max_area

print(solution([1,2,3,4,5]))