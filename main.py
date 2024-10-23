import math
import time

import mmh3

from operations import example1, example2, example3


class BloomFilter:
    """
    m: "slots"("bits") array length
    n: number of elements
    p: false-positive probability
    l: hash function
    """

    def __init__(self, n, p):
        self.m = -int(n * math.log(p) / (math.log(2) ** 2))
        self.l = int(self.m / n * math.log(2))

        self.slots_array = [0] * self.m

        self.n = n
        self.p = p

    def add(self, item):
        for i in range(self.l):
            digest = universal_hash(item, i, self.n, self.m) % self.m
            if not self.slots_array[digest]:
                self.slots_array[digest] += 1

    def check(self, item):
        for i in range(self.l):
            digest = universal_hash(item, i, self.n, self.m) % self.m
            if not self.slots_array[digest]:
                return False
        return True

    def remove(self, item):
        for i in range(self.l):
            digest = universal_hash(item, i, self.n, self.m) % self.m
            if self.slots_array[digest]:
                self.slots_array[digest] -= 1


def check_if_prime(num):
    flag = False

    if num == 0 or num == 1:
        return False
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = True
                break

        if flag:
            return False
        else:
            return True


def find_params(seed):
    a_seed, b_seed = seed // 2 + 1, seed // 2 + 2
    a = b = 0
    a_count = 0
    while a_count < a_seed:
        a += 1
        if check_if_prime(a):
            a_count += 1

    b_count = 0
    while b_count < b_seed:
        b += 1
        if check_if_prime(b):
            b_count += 1

    return a, b


def universal_hash(s: str, seed, p, m):
    hash_value = 0
    a, b = find_params(seed)
    for k in s:
        hash_value += ((a * ord(k) + b) % p) % m
    return hash_value


def process_operations_bloom(operations, n, p):
    start_time = time.perf_counter()

    bloom_filter = BloomFilter(n, p)

    for i in range(bloom_filter.n):
        operation = operations[i]
        op, string = operation[0], operation[1:].strip()
        if op == '+':
            bloom_filter.add(string)
        elif op == '-':
            bloom_filter.remove(string)
        elif op == '?':
            check_result = bloom_filter.check(string)
            print("Y" if check_result else "N")
        elif op == '#':
            break
    end_time = time.perf_counter()
    print("Computation time: ", end_time - start_time)


def test_standard(n, p):
    print("Testing standard case")
    process_operations_bloom(example1, n, p)


def test_10_to_6_length(n, p):
    print("Testing case: input length = 10^6 elements")
    process_operations_bloom(example2, n, p)


def test_excess_length(n, p):
    print("Testing case: input length > 10^6 elements")
    process_operations_bloom(example3, n, p)


if __name__ == "__main__":
    n = 10 ** 6
    p = 0.01

    test_10_to_6_length(n, p)
