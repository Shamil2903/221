def mod_exponentiation(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result
 
def geometric_sum(a, n, m):
    if a == 1:
        return n % m  # Direct sum for a = 1
    num = mod_exponentiation(a, n + 1, m * (a - 1)) - a  # a^(n+1) - a
    den = a - 1
    return (num // den) % m  # Compute sum % m
 
# Read input
T = int(input())
for _ in range(T):
    a, n, m = map(int, input().split())
    print(geometric_sum(a, n, m)) 