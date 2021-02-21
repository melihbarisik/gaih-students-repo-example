import random


def create_prime_number():
    isPrimeNum = False

    while not isPrimeNum:
        num = random.randint(1, 9)
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                isPrimeNum = True
        else:
            isPrimeNum = False

    return num


def print_random_matrix():
    for i in range(sizeOfMatrix):
        for j in range(sizeOfMatrix):
            print(matrix[i][j], end=" ")
        print()


sizeOfMatrix = 3
matrix = [[0 for i in range(sizeOfMatrix)] for j in range(sizeOfMatrix)]

for i in range(sizeOfMatrix):
    for j in range(sizeOfMatrix):
        matrix[i][j] = create_prime_number()

print_random_matrix()
