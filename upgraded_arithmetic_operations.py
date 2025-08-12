#!/usr/bin/env python3
"""
Enhanced Arithmetic Operations Calculator

This module provides a comprehensive set of arithmetic operations
with proper error handling, input validation, and modern Python features.
"""

from typing import Union, List
import math


def validate_number(value: Union[int, float, str]) -> float:
    """
    Validate and convert input to a number.
    
    Args:
        value: The value to validate
        
    Returns:
        float: The validated number
        
    Raises:
        ValueError: If the value cannot be converted to a number
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid number: {value}")


def add_numbers(*numbers: Union[int, float, str]) -> float:
    """
    Add multiple numbers together.
    
    Args:
        *numbers: Variable number of numbers to add
        
    Returns:
        float: The sum of all numbers
    """
    if not numbers:
        return 0.0
    
    validated_numbers = [validate_number(num) for num in numbers]
    return sum(validated_numbers)


def subtract_numbers(*numbers: Union[int, float, str]) -> float:
    """
    Subtract numbers from left to right.
    
    Args:
        *numbers: Variable number of numbers to subtract
        
    Returns:
        float: The result of subtraction
    """
    if not numbers:
        return 0.0
    
    validated_numbers = [validate_number(num) for num in numbers]
    result = validated_numbers[0]
    
    for num in validated_numbers[1:]:
        result -= num
    
    return result


def multiply_numbers(*numbers: Union[int, float, str]) -> float:
    """
    Multiply multiple numbers together.
    
    Args:
        *numbers: Variable number of numbers to multiply
        
    Returns:
        float: The product of all numbers
    """
    if not numbers:
        return 0.0
    
    validated_numbers = [validate_number(num) for num in numbers]
    result = 1.0
    
    for num in validated_numbers:
        result *= num
    
    return result


def divide_numbers(dividend: Union[int, float, str], 
                  divisor: Union[int, float, str]) -> float:
    """
    Divide dividend by divisor.
    
    Args:
        dividend: The number to be divided
        divisor: The number to divide by
        
    Returns:
        float: The result of division
        
    Raises:
        ZeroDivisionError: If divisor is zero
    """
    dividend_val = validate_number(dividend)
    divisor_val = validate_number(divisor)
    
    if divisor_val == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    
    return dividend_val / divisor_val


def power(base: Union[int, float, str], 
          exponent: Union[int, float, str]) -> float:
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        float: The result of the power operation
    """
    base_val = validate_number(base)
    exponent_val = validate_number(exponent)
    
    return math.pow(base_val, exponent_val)


def modulus(dividend: Union[int, float, str], 
           divisor: Union[int, float, str]) -> float:
    """
    Calculate the remainder of division.
    
    Args:
        dividend: The number to be divided
        divisor: The number to divide by
        
    Returns:
        float: The remainder
        
    Raises:
        ZeroDivisionError: If divisor is zero
    """
    dividend_val = validate_number(dividend)
    divisor_val = validate_number(divisor)
    
    if divisor_val == 0:
        raise ZeroDivisionError("Cannot calculate modulus with zero divisor")
    
    return dividend_val % divisor_val


def floor_divide(dividend: Union[int, float, str], 
                divisor: Union[int, float, str]) -> int:
    """
    Perform floor division (integer division).
    
    Args:
        dividend: The number to be divided
        divisor: The number to divide by
        
    Returns:
        int: The floor division result
        
    Raises:
        ZeroDivisionError: If divisor is zero
    """
    dividend_val = validate_number(dividend)
    divisor_val = validate_number(divisor)
    
    if divisor_val == 0:
        raise ZeroDivisionError("Cannot perform floor division by zero")
    
    return int(dividend_val // divisor_val)


def calculate_average(*numbers: Union[int, float, str]) -> float:
    """
    Calculate the average of multiple numbers.
    
    Args:
        *numbers: Variable number of numbers
        
    Returns:
        float: The average of all numbers
        
    Raises:
        ValueError: If no numbers are provided
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    validated_numbers = [validate_number(num) for num in numbers]
    return sum(validated_numbers) / len(validated_numbers)


def main():
    """Main function to demonstrate the arithmetic operations."""
    print("🧮 Enhanced Arithmetic Operations Calculator")
    print("=" * 50)
    
    # Example calculations
    try:
        # Basic operations
        print(f"Addition: 4 + 7 = {add_numbers(4, 7)}")
        print(f"Subtraction: 4 - 7 = {subtract_numbers(4, 7)}")
        print(f"Multiplication: 4 × 7 = {multiply_numbers(4, 7)}")
        print(f"Division: 4 ÷ 7 = {divide_numbers(4, 7):.4f}")
        
        # Advanced operations
        print(f"Power: 4^3 = {power(4, 3)}")
        print(f"Modulus: 17 % 5 = {modulus(17, 5)}")
        print(f"Floor Division: 17 // 5 = {floor_divide(17, 5)}")
        print(f"Average of [10, 20, 30, 40]: {calculate_average(10, 20, 30, 40)}")
        
        # Multiple number operations
        print(f"Sum of [1, 2, 3, 4, 5]: {add_numbers(1, 2, 3, 4, 5)}")
        print(f"Product of [2, 3, 4]: {multiply_numbers(2, 3, 4)}")
        
    except (ValueError, ZeroDivisionError) as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()