def count_numbers(target, numbers):
    count = 0
    for i in numbers:
        if target == i:
            count +=1
    return count

print(count_numbers(1, [1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 1, 1, 1, 1, 1, 20, 23])) #9
print(count_numbers(10, [42, 10, 10, 10, 10, 64, 23, 10, 10, 10])) #7
print(count_numbers(54, [45, 46, 23, 65])) #0
