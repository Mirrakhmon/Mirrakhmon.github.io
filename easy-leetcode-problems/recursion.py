def sum_to_n(n):
    # base case: что если n == 0 или n == 1?
    # рекурсивный случай: sum_to_n(n) = n + sum_to_n(n-1)
    if n<=1:
        return 1
    return n+sum_to_n(n-1)

print(sum_to_n(5))    # ожидается 15  (1+2+3+4+5)
print(sum_to_n(1))    # ожидается 1