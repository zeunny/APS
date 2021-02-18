import re
from collections import defaultdict

def solution(str1, str2):
    A, B = defaultdict(int), defaultdict(int)
    for i in range(max(len(str1), len(str2))-1):
        if i < len(str1)-1:
            if len(re.sub('([^a-zA-Z]+)', '', str1[i:i+2]).lower()) == 2:
                A[str1[i:i+2].lower()] += 1
        if i < len(str2)-1:
            if len(re.sub('([^a-zA-Z]+)', '', str2[i:i+2]).lower()) == 2:
                B[str2[i:i+2].lower()] += 1

    intersection = 0
    union = 0
    for k, v in A.items():
        intersection += min(A[k], B[k])
        union += max(A[k], B[k])
        A[k], B[k] = 0, 0
    
    for k, v in B.items():
        intersection += min(A[k], B[k])
        union += max(A[k], B[k])
    
    return int(intersection/union*65536) if union else 65536