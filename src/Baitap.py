# 1. Write a Python function to find the maximum of three numbers.
def max_of_numbers(*args:int) -> int:
    m=args[0]
    for x in args:
        if x>m: m= x
    return m

if __name__ == '__main__':
    largest = max_of_numbers(3,56,73,57,28,47,90)
    print(largest)
# 2. Write a Python function to sum all the numbers in a list.
def sum_list(numbers:float)->float:
    total = 0
    for num in numbers:
        total += num
    return total
nums = [3,53,53,5,6,3,4,9.2]
print("The sum is:", sum_list(nums))
# 3. Write a Python program to reverse a string.
def reverse_string(s):
    return s[::-1]
print(reverse_string("phamdaotramy"))
# 4. Write a Python function to calculate the factorial of a number (a non-negative
# integer). The function accepts the number as an argument.
def factorial(n):
    if n<0:
        return "Factorial not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

# 5. Write a Python function that takes a number as a parameter and checks
# whether the number is prime or not.
def is_prime(num:int)->bool:
    if num<2: return False
    for i in range(2, int(num/2)):
        if num%i==0:
            return False
    return True
if __name__ == '__main__':
    print(is_prime(46))
    print(is_prime(37))
# 6. Write a Python function to print
# 1. all prime numbers that less than a number (enter prompt keyboard).
# 2. the first N prime numbers
def print_primes_under_number(n):
    for i in range(2,n):
        if is_prime(i):
            print(i)

def print_first_n_primes(n):
    '''In ra n so nguyen to dau tien'''
    pass

if __name__ == '__main__':
    print_primes_under_number(20)
# 7. Write a Python function to check whether a number is "Perfect" or not. Then
# print all perfect number that less than 1000.
def is_perfect():
    if n<2:
        return False
    divisors_sum = 1
    for i in range(2, n//2+1):
        if n%i ==0:

# 8. Write a Python function to check whether a string is a pangram or not.
# (Note : Pangrams are words or sentences containing every letter of the alphabet at
# least once. For example : "The quick brown fox jumps over the lazy dog"
