## This function does the same job as the recursive function below
def find_prime(n):
    if not(isinstance(n,int)) or n <= 1:
        print ('Please enter a natural number greater than 1!')
        return
    else:
        primel = []
        for i in range(2, n + 1):
            factorl = []
            for j in range(1, i + 1):
                if i % j == 0:
                    factorl.append(j)
            if len(factorl) == 2:
                primel.append(i)
    return primel

## Rucursive function to find prime numbers
primel = []
def find_prime(n):
    ## n must be a valid natural number to start
    if not (isinstance(n, int)) or n <= 1:
        print('Please enter a natural number greater than 1!')
        return
    for i in range(2, n + 1):
        if n % i == 0:
            ## Condition where there is a divisor for n
            if n != i:
                break  # jump out of the loop if n has a divisor other than 1 and n
            else:
                primel.append(n)  # append to prime list if n has a divisor 1 and n
    n = n - 1
    if n <= 2:
        pass  # stop the recursion if n <= 2
    else:
        find_prime(n)  # recursive function to repeat the function until n < = 2
    return primel

find_prime(100)

# from math import sqrt
#
# def find_primes_rec(n):
#     # base case 0
#     if n == 0:
#         return []
#     # base case 1
#     elif n == 1:
#         return []
#     else:
#         p = find_primes_rec(int(sqrt(n))) # recursive call
#         no_p = [j for i in p for j in range(i*2, n + 1, i)]
#         p = [x for x in range(2, n + 1) if x not in no_p]
#         return p
#
# print(find_primes_rec(100))