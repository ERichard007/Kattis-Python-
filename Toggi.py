import math

def max_pi_digits(C):
    limit = C * 10**6
 
    left, right = 1, limit
    best_n = 1
    
    while left <= right:
        mid = (left + right) // 2
        if mid * math.log10(mid) <= limit:
            best_n = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return best_n

C = int(input())
print(max_pi_digits(C))