#!/usr/bin/env python3
"""
List all prime numbers from 1 to 1000.

This script uses an optimized approach to find prime numbers efficiently.
"""

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_primes_up_to(limit):
    """
    Find all prime numbers up to a given limit.
    
    Args:
        limit (int): The upper bound (inclusive)
        
    Returns:
        list: A list of all prime numbers up to the limit
    """
    primes = []
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    """Main function to find and display primes from 1 to 1000."""
    limit = 1000
    primes = find_primes_up_to(limit)
    
    print(f"Prime numbers from 1 to {limit}:")
    print("=" * 50)
    
    # Display primes in a formatted way (10 per line)
    for i, prime in enumerate(primes, 1):
        print(f"{prime:4d}", end=" ")
        if i % 10 == 0:
            print()
    
    # Print summary
    print(f"\n\nTotal prime numbers found: {len(primes)}")
    
    # Also save to a file for reference
    with open("primes_1_to_1000.txt", "w") as f:
        f.write(f"Prime numbers from 1 to {limit}:\n")
        f.write("=" * 50 + "\n")
        for prime in primes:
            f.write(f"{prime}\n")
    
    print("\nPrime numbers have also been saved to 'primes_1_to_1000.txt'")

if __name__ == "__main__":
    main()