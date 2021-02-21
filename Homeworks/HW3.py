def prime_first(prime_number):
    print(prime_number)


def prime_second(prime_number):
    print(prime_number)


def create_prime_number(num):
    is_number_prime = False

    if num > 1:

        for i in range(2, num):
            if (num % i) == 0:
                is_number_prime = False
                break
        else:
            is_number_prime = True

    else:
        is_number_prime = False

    return is_number_prime


for i in range(1000):
    if 0 < i < 500:
        if create_prime_number(i):
            prime_first(i)


    elif 500 < i < 1000:
        if create_prime_number(i):
            prime_second(i)
