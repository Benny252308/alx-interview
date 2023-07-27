#!/usr/bin/python3
'''
module to return pascal triangle
'''


def pascal_triangle(num):
    ''' function that returns a pascal triangle '''
    lst = []
    if num <= 0:
        return lst
    for i in range(num):
        lst.append([])
        lst[i].append(1)
        for j in range(1, i):
            lst[i].append(lst[i - 1][j - 1] + lst[i - 1][j])
        if i > 0:
            lst[i].append(1)
    return lst
