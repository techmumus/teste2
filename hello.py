#!/usr/bin/env python3
"""
A simple greeting script.

This script prints a friendly hello message to the console.
"""

def say_hello(name: str = "World") -> None:
    """
    Print a personalized greeting message.
    
    Args:
        name: The name to include in the greeting. Defaults to "World".
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # When run directly, greet the world
    say_hello()