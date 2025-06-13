# Count how many even and odd numbers in a list

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even = [n for n in numbers if n % 2 == 0]
odd = [n for n in numbers if n % 2 != 0]

print(f"Even count: {len(even)}")
print(f"Odd count: {len(odd)}")
