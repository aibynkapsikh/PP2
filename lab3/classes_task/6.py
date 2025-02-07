def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n * 0.5) + 1):
        if n % i == 0:
            return False
    
    return True

numbers = [10, 3, 5, 8, 11, 15, 17, 23, 24]

prime_numbers = list(filter(lambda x : is_prime(x), numbers))

print("Prime numbers :", prime_numbers)
