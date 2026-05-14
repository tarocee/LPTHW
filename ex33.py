i = 8
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ",numbers)
    print(f"At the bottom i is {i}")

print("The nembers: ")

for num in numbers:
    print(num)


def while_loop(start,counter):
    while start < 6:
        print(f"At the top num is {start}")
        numbers.append(start)

        start += counter
        print("Numbers now:",numbers)
        print(f"At the bottom num is {start}")


while_loop(0,2)
