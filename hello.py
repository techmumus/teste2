#!/usr/bin/env python3
"""
Hello - A friendly introduction to the primes collection.

This script provides a simple interface to explore the prime number
utilities available in this repository.
"""

import sys
from pathlib import Path

def display_welcome():
    """Display a welcome message with available options."""
    print("=" * 50)
    print("Welcome to the Prime Numbers Explorer!")
    print("=" * 50)
    print("\nAvailable prime ranges:")
    print("1. Primes from 1 to 1,000")
    print("2. Primes from 1 to 2,000")
    print("3. Optimized prime generation")
    print("4. Exit")
    print("-" * 30)

def load_primes_file(filename):
    """Safely load a primes file and return the primes list."""
    try:
        file_path = Path(__file__).parent / filename
        with open(file_path, 'r') as f:
            content = f.read()
            # Extract primes from the file (assuming they're in a list format)
            lines = content.strip().split('\n')
            primes = []
            for line in lines:
                if line.strip() and not line.startswith('#'):
                    # Handle different formats: list, tuple, or individual numbers
                    numbers = line.replace('[', '').replace(']', '').replace('(', '').replace(')', '')
                    for num in numbers.split(','):
                        try:
                            primes.append(int(num.strip()))
                        except ValueError:
                            continue
            return primes
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []

def display_primes(primes, title):
    """Display primes in a formatted way."""
    if not primes:
        print(f"No primes found in {title}")
        return
    
    print(f"\n{title}:")
    print("-" * len(title))
    
    # Display in rows of 10
    for i in range(0, len(primes), 10):
        row = primes[i:i+10]
        print(" ".join(f"{p:4d}" for p in row))
    
    print(f"\nTotal primes: {len(primes)}")

def main():
    """Main program loop."""
    while True:
        display_welcome()
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                primes = load_primes_file('primes_1_to_1000.py')
                display_primes(primes, "Prime numbers from 1 to 1,000")
                
            elif choice == '2':
                primes = load_primes_file('primes_1_to_2000.py')
                display_primes(primes, "Prime numbers from 1 to 2,000")
                
            elif choice == '3':
                try:
                    from primes_optimized import generate_primes
                    limit = input("Enter upper limit for prime generation: ").strip()
                    if limit.isdigit() and int(limit) > 0:
                        primes = generate_primes(int(limit))
                        display_primes(primes, f"Primes up to {limit}")
                    else:
                        print("Please enter a valid positive integer.")
                except ImportError:
                    print("Error: primes_optimized.py not found or doesn't have generate_primes function.")
                except Exception as e:
                    print(f"Error generating primes: {e}")
                    
            elif choice == '4':
                print("Thank you for exploring primes! Goodbye.")
                break
                
            else:
                print("Invalid choice. Please enter 1-4.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()