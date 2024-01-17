# Fibonacci Sequence
# Factorial Calculation
# Prime Numbers
# Palindrome Check

def fibonacci(numOfterms):
    fibo_seq = [0,1]
    while len(fibo_seq) < numOfterms:
       fibo_seq.append(fibo_seq[-1] + fibo_seq[-2])
    return fibo_seq[:numOfterms]   

def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


def prime_numbercheck(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# i have just used python reversed string function
def is_palindrome(word):
    return word == word[::-1]

def main():
    while True:
        print("\nChoose an operation:")
        print("1. Fibonacci Sequence")
        print("2. Factorial Calculation")
        print("3. Prime Numbers Check")
        print("4. Palindrome Check")
        print("5. Exit")   
        choice = input("Enter the number of your choice (1-5): ")

        if choice == '1':
            n = int(input("Enter the number of terms for the Fibonacci sequence: "))
            result = fibonacci(n)
            print(f"Fibonacci Sequence: {result}")

        elif choice == '2':
            num = int(input("Enter a number to calculate its factorial: "))
            result = factorial(num)
            print(f"Factorial of {num}: {result}")

        elif choice == '3':
            num = int(input("Enter a number to check if it's prime: "))
            result = prime_numbercheck(num)
            print(f"{num} is {'prime' if result else 'not prime'}.")

        elif choice == '4':
            word = input("Enter a word to check if it's a palindrome: ").lower()
            result = is_palindrome(word)
            print(f"{word.capitalize()} is {'a palindrome' if result else 'not a palindrome'}.")

        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()