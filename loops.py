# Write a program that:
# Prints even numbers from 1 to 20
# Skips numbers divisible by 3
for num in range(1,21):
    if num % 2 == 0:
        if num % 3 != 0:
            print(num)
