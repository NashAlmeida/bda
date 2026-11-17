arr = []
bits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def hash(num):
    n1 = num % 10
    n2 = (num * 3) % 10

    for i in range(len(bits)):
        if i == n1 or i == n2:
            bits[i] = 1

    arr.append(num)


def check(num):
    n1 = num % 10
    n2 = (num * 3) % 10

    if bits[n1] == 1 and bits[n2] == 1:
        print(num, "Maybe Exists")
    else:
        print(num, "Def doesnt exist")


hash(25)
hash(42)

check(25)
check(42)
check(17)

print("Current Stack:", arr)
print("Bloom filter array:", bits)
