#!/usr/bin/env python3
"""
Basic Arithmetic Operations Calculator

A comprehensive calculator that performs various arithmetic operations
with proper error handling and user-friendly interface.

Author: [Your Name]
Date: [Current Date]
"""

import math
from typing import Union, Optional
from dataclasses import dataclass


@dataclass
class CalculationResult:
    """Data class to store calculation results."""
    operation: str
    operands: tuple[float, float]
    result: float
    success: bool
    error_message: Optional[str] = None


class ArithmeticCalculator:
    """A comprehensive arithmetic calculator with error handling."""
    
    def __init__(self):
        self.history: list[CalculationResult] = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> CalculationResult:
        """Add two numbers."""
        try:
            result = float(a) + float(b)
            calc_result = CalculationResult("addition", (a, b), result, True)
            self.history.append(calc_result)
            return calc_result
        except (ValueError, TypeError) as e:
            return CalculationResult("addition", (a, b), 0, False, str(e))
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> CalculationResult:
        """Subtract second number from first number."""
        try:
            result = float(a) - float(b)
            calc_result = CalculationResult("subtraction", (a, b), result, True)
            self.history.append(calc_result)
            return calc_result
        except (ValueError, TypeError) as e:
            return CalculationResult("subtraction", (a, b), 0, False, str(e))
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> CalculationResult:
        """Multiply two numbers."""
        try:
            result = float(a) * float(b)
            calc_result = CalculationResult("multiplication", (a, b), result, True)
            self.history.append(calc_result)
            return calc_result
        except (ValueError, TypeError) as e:
            return CalculationResult("multiplication", (a, b), 0, False, str(e))
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> CalculationResult:
        """Divide first number by second number."""
        try:
            if float(b) == 0:
                return CalculationResult("division", (a, b), 0, False, "Division by zero is not allowed")
            result = float(a) / float(b)
            calc_result = CalculationResult("division", (a, b), result, True)
            self.history.append(calc_result)
            return calc_result
        except (ValueError, TypeError) as e:
            return CalculationResult("division", (a, b), 0, False, str(e))
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> CalculationResult:
        """Raise base to the power of exponent."""
        try:
            result = math.pow(float(base), float(exponent))
            calc_result = CalculationResult("power", (base, exponent), result, True)
            self.history.append(calc_result)
            return calc_result
        except (ValueError, TypeError) as e:
            return CalculationResult("power", (base, exponent), 0, False, str(e))
    
    def modulus(self, a: Union[int, float], b: Union[int, float]) -> CalculationResult:
        """Calculate remainder of division."""
        try:
            if float(b) == 0:
                return CalculationResult("modulus", (a, b), 0, False, "Modulus by zero is not allowed")
            result = float(a) % float(b)
            calc_result = CalculationResult("modulus", (a, b), result, True)
            self.history.append(calc_result)
            return calc_result
        except (ValueError, TypeError) as e:
            return CalculationResult("modulus", (a, b), 0, False, str(e))
    
    def floor_divide(self, a: Union[int, float], b: Union[int, float]) -> CalculationResult:
        """Perform floor division."""
        try:
            if float(b) == 0:
                return CalculationResult("floor_division", (a, b), 0, False, "Floor division by zero is not allowed")
            result = float(a) // float(b)
            calc_result = CalculationResult("floor_division", (a, b), result, True)
            self.history.append(calc_result)
            return calc_result
        except (ValueError, TypeError) as e:
            return CalculationResult("floor_division", (a, b), 0, False, str(e))
    
    def get_history(self) -> list[CalculationResult]:
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()


def get_user_input(prompt: str) -> Optional[float]:
    """Get and validate user input."""
    while True:
        try:
            user_input = input(prompt).strip()
            if user_input.lower() in ['q', 'quit', 'exit']:
                return None
            return float(user_input)
        except ValueError:
            print("❌ Invalid input. Please enter a valid number or 'q' to quit.")


def display_menu() -> None:
    """Display the calculator menu."""
    print("\n" + "="*50)
    print("🧮 ARITHMETIC CALCULATOR")
    print("="*50)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Modulus (%)")
    print("7. Floor Division (//)")
    print("8. View History")
    print("9. Clear History")
    print("0. Exit")
    print("="*50)


def display_result(result: CalculationResult) -> None:
    """Display calculation result in a formatted way."""
    if result.success:
        print(f"✅ {result.operation.title()}: {result.operands[0]} {get_operator(result.operation)} {result.operands[1]} = {result.result}")
    else:
        print(f"❌ Error in {result.operation}: {result.error_message}")


def get_operator(operation: str) -> str:
    """Get the mathematical operator symbol for an operation."""
    operators = {
        "addition": "+",
        "subtraction": "-",
        "multiplication": "*",
        "division": "/",
        "power": "**",
        "modulus": "%",
        "floor_division": "//"
    }
    return operators.get(operation, "?")


def display_history(calculator: ArithmeticCalculator) -> None:
    """Display calculation history."""
    history = calculator.get_history()
    if not history:
        print("📝 No calculations in history.")
        return
    
    print("\n📝 CALCULATION HISTORY:")
    print("-" * 50)
    for i, calc in enumerate(history, 1):
        if calc.success:
            print(f"{i}. {calc.operands[0]} {get_operator(calc.operation)} {calc.operands[1]} = {calc.result}")
        else:
            print(f"{i}. {calc.operation}: {calc.error_message}")
    print("-" * 50)


def main() -> None:
    """Main function to run the calculator."""
    calculator = ArithmeticCalculator()
    
    print("🎉 Welcome to the Advanced Arithmetic Calculator!")
    print("This calculator supports various mathematical operations with error handling.")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (0-9): ").strip()
            
            if choice == "0":
                print("👋 Thank you for using the calculator! Goodbye!")
                break
            
            elif choice == "8":
                display_history(calculator)
                continue
            
            elif choice == "9":
                calculator.clear_history()
                print("🗑️ History cleared successfully!")
                continue
            
            elif choice not in ["1", "2", "3", "4", "5", "6", "7"]:
                print("❌ Invalid choice. Please select a number between 0-9.")
                continue
            
            # Get operands
            print("\nEnter your numbers (or 'q' to quit):")
            a = get_user_input("Enter first number: ")
            if a is None:
                continue
            
            b = get_user_input("Enter second number: ")
            if b is None:
                continue
            
            # Perform calculation based on choice
            operations = {
                "1": calculator.add,
                "2": calculator.subtract,
                "3": calculator.multiply,
                "4": calculator.divide,
                "5": calculator.power,
                "6": calculator.modulus,
                "7": calculator.floor_divide
            }
            
            result = operations[choice](a, b)
            display_result(result)
            
        except KeyboardInterrupt:
            print("\n\n👋 Calculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ An unexpected error occurred: {e}")


def run_demo() -> None:
    """Run a demonstration of the calculator with predefined values."""
    print("🎯 DEMONSTRATION MODE")
    print("="*50)
    
    calculator = ArithmeticCalculator()
    
    # Demo calculations
    demo_calculations = [
        (4, 7, "addition"),
        (4, 7, "subtraction"),
        (4, 7, "multiplication"),
        (4, 7, "division"),
        (2, 3, "power"),
        (17, 5, "modulus"),
        (17, 5, "floor_division")
    ]
    
    for a, b, operation in demo_calculations:
        operations = {
            "addition": calculator.add,
            "subtraction": calculator.subtract,
            "multiplication": calculator.multiply,
            "division": calculator.divide,
            "power": calculator.power,
            "modulus": calculator.modulus,
            "floor_division": calculator.floor_divide
        }
        
        result = operations[operation](a, b)
        display_result(result)
    
    print("\n📝 Final History:")
    display_history(calculator)


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
    else:
        main()
