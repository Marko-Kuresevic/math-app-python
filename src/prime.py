def compute_prime(num):
    prime_list = []

    for i in range(2, num):
        j = 2

        while j < i and i % j != 0:
            j += 1

        if j == i:
            prime_list.append(i)

    return prime_list

if __name__ == "__main__":
    compute_prime()