#!/usr/bin/env python3
"""
Optimized version using the Sieve of Eratosthenes algorithm
to find all prime numbers from 1 to 1000.
"""

def sieve_of_eratosthenes(limit):
    """
    Find all prime numbers up to a given limit using the Sieve of Eratosthenes.
    
    This is more efficient for finding multiple primes than checking each number individually.
    
    Args:
        limit (int): The upper bound (inclusive)
        
    Returns:
        list: A list of all prime numbers up to the limit
    """
    if limit < 2:
        return []
    
    # Initialize a boolean array "is_prime" and set all entries as True
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    # Start with the smallest prime number, 2
    p = 2
    while p * p <= limit:
        # If is_prime[p] is not changed, then it is a prime
        if is_prime[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = [num for num in range(2, limit + 1) if is_prime[num]]
    return primes

def main():
    """Main function to find and display primes using the optimized method."""
    limit = 1000
    primes = sieve_of_eratosthenes(limit)
    
    print(f"Prime numbers from 1 to {limit} (using Sieve of Eratosthenes):")
    print("=" * 60)
    
    # Display primes in a formatted way
    for i, prime in enumerate(primes, 1):
        print(f"{prime:4d}", end=" ")
        if i % 10 == 0:
            print()
    
    print(f"\n\nTotal prime numbers found: {len(primes)}")
    
    # Display the primes as a comma-separated list
    print("\nComma-separated list:")
    print(", ".join(map(str, primes)))

if __name__ == "__main__":
    main()