#!/usr/bin/env python3

seq = []

def count_sort(seq):
    large = max(seq) + 1
    rev = list(reversed(seq))

    a = []
    b = []
    c = []

    a = [0] * large 
    b = [0] * large 

#first step of incrementing those index with one where digit appears

    for i in range(len(seq)):
        a[seq[i]] = a[seq[i]] + 1

    for i in range(len(a)):
        if i == 0:
            b[i] = a[i]
        elif i == 1:
            b[i] = a[i] + a[i-1]
        else:
            b[i] = b[i-1] + a[i]

    print(a)
    print(b)

    b_large = max(b) + 1
    c = [0] * b_large

    for i in range(len(seq)):
        index_rev = rev[i]
        content_b = b[index_rev]
        c[content_b] = rev[i]
        content_b = content_b - 1
        b[index_rev] = content_b
    
    print(c)


size = int(input('Enter the Size of your Array-\t'))
for i in range(size):
    values = int(input('Enter the Elements of Array'))
    seq.append(values)
    
count_sort(seq)