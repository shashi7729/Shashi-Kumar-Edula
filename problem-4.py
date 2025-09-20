nums = list(map(int, input("Enter numbers separated by space: ").split()))

result = {}

for d in range(1, 10):   # divisors from 1 to 9
    count = 0
    for n in nums:
        if n % d == 0:
            count += 1
    result[d] = count

print(result)
