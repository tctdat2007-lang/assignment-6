def remove_odd_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    even_numbers = remove_odd_numbers(numbers)
    print("Original list:", numbers)
    print("Even numbers only:", even_numbers)

if __name__ == "__main__":
    main()
