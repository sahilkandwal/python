# Function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Main function
def main():
    try:
        # Read input from the user
        num = int(input("Enter a number to calculate its factorial: "))
        
        # Calculate factorial
        fact = factorial(num)
        
        # Check if the number is prime
        prime = is_prime(num)
        
        # Print results
        print(f"The factorial of {num} is: {fact}")
        if prime:
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
