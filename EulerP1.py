a = 0
b = 0
c = 0
d = 0
while a < 1000:
    c = c + a
    a += 3
while b < 1000:
    d = b/3
    d_int = int(d)
    if d_int == d:
        pass
    else:
        c = c + b
    b += 5
print(c)


def sum_of_multiples():
    total_sum = 0
    for i in range(1001):
        if i % 3 == 0 or i % 5 == 0:
            total_sum += i
    print(total_sum)

# Call the function
sum_of_multiples()


