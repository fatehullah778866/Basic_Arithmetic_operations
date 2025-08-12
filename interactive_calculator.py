#!/usr/bin/env python3
"""
Interactive Arithmetic Calculator

This module provides an interactive command-line calculator
that allows users to perform various arithmetic operations.
"""

from typing import Union
import math


def validate_number(value: str) -> float:
    """Validate and convert string input to a number."""
    try:
        return float(value)
    except ValueError:
        raise ValueError(f"Invalid number: {value}")


def get_user_input(prompt: str) -> str:
    """Get user input with a prompt."""
    return input(prompt).strip()


def get_numbers() -> list[float]:
    """Get multiple numbers from user input."""
    numbers = []
    print("Enter numbers (press Enter twice to finish):")
    
    while True:
        user_input = get_user_input("Enter a number: ")
        if user_input == "":
            break
        
        try:
            number = validate_number(user_input)
            numbers.append(number)
        except ValueError as e:
            print(f"❌ {e}")
    
    return numbers


def display_menu():
    """Display the calculator menu."""
    print("\n🧮 Calculator Menu")
    print("=" * 30)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. Average")
    print("9. Exit")
    print("=" * 30)


def perform_addition():
    """Perform addition operation."""
    numbers = get_numbers()
    if not numbers:
        print("❌ No numbers provided")
        return
    
    result = sum(numbers)
    print(f"➕ Sum: {' + '.join(map(str, numbers))} = {result}")


def perform_subtraction():
    """Perform subtraction operation."""
    numbers = get_numbers()
    if not numbers:
        print("❌ No numbers provided")
        return
    
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    
    print(f"➖ Result: {' - '.join(map(str, numbers))} = {result}")


def perform_multiplication():
    """Perform multiplication operation."""
    numbers = get_numbers()
    if not numbers:
        print("❌ No numbers provided")
        return
    
    result = 1
    for num in numbers:
        result *= num
    
    print(f"✖️ Product: {' × '.join(map(str, numbers))} = {result}")


def perform_division():
    """Perform division operation."""
    try:
        dividend = validate_number(get_user_input("Enter dividend: "))
        divisor = validate_number(get_user_input("Enter divisor: "))
        
        if divisor == 0:
            print("❌ Cannot divide by zero")
            return
        
        result = dividend / divisor
        print(f"➗ Division: {dividend} ÷ {divisor} = {result:.4f}")
        
    except ValueError as e:
        print(f"❌ {e}")


def perform_power():
    """Perform power operation."""
    try:
        base = validate_number(get_user_input("Enter base: "))
        exponent = validate_number(get_user_input("Enter exponent: "))
        
        result = math.pow(base, exponent)
        print(f"🔢 Power: {base}^{exponent} = {result}")
        
    except ValueError as e:
        print(f"❌ {e}")


def perform_modulus():
    """Perform modulus operation."""
    try:
        dividend = validate_number(get_user_input("Enter dividend: "))
        divisor = validate_number(get_user_input("Enter divisor: "))
        
        if divisor == 0:
            print("❌ Cannot calculate modulus with zero divisor")
            return
        
        result = dividend % divisor
        print(f"📊 Modulus: {dividend} % {divisor} = {result}")
        
    except ValueError as e:
        print(f"❌ {e}")


def perform_floor_division():
    """Perform floor division operation."""
    try:
        dividend = validate_number(get_user_input("Enter dividend: "))
        divisor = validate_number(get_user_input("Enter divisor: "))
        
        if divisor == 0:
            print("❌ Cannot perform floor division by zero")
            return
        
        result = int(dividend // divisor)
        print(f"🔽 Floor Division: {dividend} // {divisor} = {result}")
        
    except ValueError as e:
        print(f"❌ {e}")


def perform_average():
    """Perform average calculation."""
    numbers = get_numbers()
    if not numbers:
        print("❌ No numbers provided")
        return
    
    result = sum(numbers) / len(numbers)
    print(f"📈 Average of {numbers}: {result:.4f}")


def main():
    """Main interactive calculator function."""
    print("🧮 Welcome to the Interactive Calculator!")
    print("This calculator supports various arithmetic operations.")
    
    while True:
        display_menu()
        choice = get_user_input("Select an operation (1-9): ")
        
        if choice == "1":
            perform_addition()
        elif choice == "2":
            perform_subtraction()
        elif choice == "3":
            perform_multiplication()
        elif choice == "4":
            perform_division()
        elif choice == "5":
            perform_power()
        elif choice == "6":
            perform_modulus()
        elif choice == "7":
            perform_floor_division()
        elif choice == "8":
            perform_average()
        elif choice == "9":
            print("👋 Thank you for using the calculator!")
            break
        else:
            print("❌ Invalid choice. Please select 1-9.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()