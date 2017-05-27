# write a function that takes in a number n and
# outputs all primes less than that integer,
# the first prime is 2. a prime is defined as a
# number whose divisors are only itself and 1.

# the naive solution is to iterate over the
# number below n and check their primality
# which can be done in O(sqrt(n)) time.
# this can be improved upon by
# only checking odd numbers, or only every
# third number, etc.
import math

def prime(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    else:
        for i in range(2, math.ceil(math.sqrt(n))):
            if n % i == 0:
                return False
    return True


def primes_up_to(n):
    if n < 2:
        return []
    elif n < 3:
        return [2]
    elif n < 4:
        return [2, 3]
    else:
        primes = [2, 3]
        for i in range(5, n, 2):
            if prime(i):
                primes.append(i)
    return primes

print(primes_up_to(18))

# by using O(n) extra space to store an array of booleans
# between 0 and n we can sieve off the values as we add them.
# the sieve of eratosthenes basically shows that as we go,
# starting with 2, the first number we encounter is prime.
# we then remove all elements of the list that are multiples
# of this value. then the next value is 3, and it must be prime.
# we continue in this fashion up to n.

def primes_up_to(n):
    possible_primes = n * [True]
    possible_primes[0], possible_primes[1] = False, False
    primes = []
    for i, boolean in enumerate(possible_primes):
        if boolean:
            primes.append(i)
            for val in range(len(possible_primes)):
                if possible_primes[val]:
                    possible_primes[val] = bool(val % (i))
    return primes

print(primes_up_to(18))

# using similar logic with better method

def primes_up_to(n):
    primes = []
    is_prime = [False, False] + [True] * (n - 1)
    for p in range(2, n):
        if is_prime[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                is_prime[i] = False
    return primes

print(primes_up_to(18))

# to continue to improve we can begin sieving out values at p**2
# since values below that of the form kp should already have been sieved
# out by k for any k less than p. in addition we can just skip even
# numbers because duh.
