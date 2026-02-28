def analyze_numbers():
    numbers = list(range(1, 11))

    total = sum(numbers)
    average = total / len(numbers)
    largest = max(numbers)
    smallest = min(numbers)

    print("Numbers:", numbers)
    print("Sum:", total)
    print("Average:", average)
    print("Largest number:", largest)
    print("Smallest number:", smallest)

analyze_numbers()
