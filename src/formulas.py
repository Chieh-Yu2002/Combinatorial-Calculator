import math
from functools import lru_cache

def factorial(n):
    return math.factorial(n) if n >= 0 else 0

def P(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    return factorial(n) // factorial(n - r)

def C(n, r):
    if n < 0 or r < 0 or r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def arrangement_with_rep(n, r):
    if n < 0 or r < 0:
        return 0
    return n ** r

def selection_with_rep(n, r):
    return C(r + n - 1, r)

@lru_cache(maxsize=None)
def catalan(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return C(2*n, n) // (n + 1)

def triangular(n):
    return (n * (n + 1)) // 2

def harmonic(n):
    return sum(1/k for k in range(1, n + 1))

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=None)
def lucas(n):
    if n <= 0:
        return 2
    if n == 1:
        return 1
    return lucas(n-1) + lucas(n-2)

@lru_cache(maxsize=None)
def eulerian(n, k):
    """
    Calculate Eulerian number A(n,k) - the number of permutations of size n with k ascents
    n: size of permutation
    k: number of ascents
    """
    if k >= n or k < 0:  # Invalid cases
        return 0
    if n == 0:  # Base case
        return 1 if k == 0 else 0
    if k == 0:  # Special case for k=0
        return 1
    
    # Use the recurrence relation for Eulerian numbers
    # A(n,k) = (n-k)*A(n-1,k-1) + (k+1)*A(n-1,k)
    return ((n - k) * eulerian(n - 1, k - 1) + 
            (k + 1) * eulerian(n - 1, k))

def stirling2(m, n):
    if n <= 0 or n > m:
        return 0
    if m == n:
        return 1
    return stirling2(m-1, n-1) + n * stirling2(m-1, n)

def onto(m, n):
    """Calculate number of onto functions from m distinct objects to n distinct containers"""
    return n * stirling2(m, n)

def sum_stirling2_to_n(m, n):
    """Calculate sum of Stirling numbers S(m,1) + S(m,2) + ... + S(m,n)"""
    return sum(stirling2(m, i) for i in range(1, n + 1))

def partition(m, n):
    """Calculate number of ways to partition integer m into exactly n parts"""
    @lru_cache(maxsize=None)
    def p(m, n):
        if n <= 0 or m <= 0:
            return 0
        if n == 1 or m == n:
            return 1
        return p(m-1, n-1) + p(m-n, n)
    return p(m, n)

def partition_with_zeros(m, n):
    """Calculate number of ways to partition integer m into at most n parts"""
    if n == m:
        return partition(m, m)
    return sum(partition(m, i) for i in range(1, min(m, n) + 1))