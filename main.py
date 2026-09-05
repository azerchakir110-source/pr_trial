#!/usr/bin/env python3
"""
Simple Python script for testing Kodus code review functionality.
"""


def greet(name: str) -> str:
    """
    Greet a person with their name.
    
    Args:
        name: The name of the person to greet.
        
    Returns:
        A greeting message.
    """
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number.
        b: Second number.
        
    Returns:
        The sum of a and b.
    """
    return a + b


def main():
    """Main entry point of the script."""
    print("=== Kodus Code Review Test Script ===")
    print()
    
    # Test greet function
    greeting = greet("World")
    print(greeting)
    
    # Test add function
    result = add(5, 3)
    print(f"5 + 3 = {result}")
    
    print()
    print("Script completed successfully!"


if __name__ == "__main__":
    main()
