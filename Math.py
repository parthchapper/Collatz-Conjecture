import math

max_it = 0

def collatz(n):
    global max_it
    if n % 2 == 0:
        n = n/2
        max_it += 1
        print(n)
        return collatz(n)
    elif n != 1:
        n = 3*n + 1
        max_it += 1
        print(n)
        return collatz(n)
    else:
        return max_it

num = 2
while True:
    try:
        num = int(input("terminal collatz tester "))
    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

    print(f"it took {collatz(num)} iterations")