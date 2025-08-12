#!/usr/bin/env python3
"""
Test suite for the Advanced Arithmetic Calculator

This file contains comprehensive tests to validate the calculator's functionality.
Run with: python test_calculator.py
"""

import sys
import os
from typing import List, Tuple

# Add the current directory to the path to import the calculator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the calculator classes and functions
from basic_python_arithmetic_operations import (
    ArithmeticCalculator, 
    CalculationResult,
    get_operator,
    display_result
)


class CalculatorTester:
    """Test suite for the ArithmeticCalculator class."""
    
    def __init__(self):
        self.calculator = ArithmeticCalculator()
        self.test_results: List[Tuple[str, bool, str]] = []
    
    def run_test(self, test_name: str, test_func) -> None:
        """Run a single test and record the result."""
        try:
            result = test_func()
            self.test_results.append((test_name, True, "PASSED"))
            print(f"✅ {test_name}: PASSED")
        except Exception as e:
            self.test_results.append((test_name, False, str(e)))
            print(f"❌ {test_name}: FAILED - {e}")
    
    def test_addition(self) -> bool:
        """Test addition operation."""
        result = self.calculator.add(5, 3)
        assert result.success
        assert result.result == 8.0
        assert result.operation == "addition"
        return True
    
    def test_subtraction(self) -> bool:
        """Test subtraction operation."""
        result = self.calculator.subtract(10, 4)
        assert result.success
        assert result.result == 6.0
        assert result.operation == "subtraction"
        return True
    
    def test_multiplication(self) -> bool:
        """Test multiplication operation."""
        result = self.calculator.multiply(6, 7)
        assert result.success
        assert result.result == 42.0
        assert result.operation == "multiplication"
        return True
    
    def test_division(self) -> bool:
        """Test division operation."""
        result = self.calculator.divide(15, 3)
        assert result.success
        assert result.result == 5.0
        assert result.operation == "division"
        return True
    
    def test_division_by_zero(self) -> bool:
        """Test division by zero error handling."""
        result = self.calculator.divide(10, 0)
        assert not result.success
        assert "Division by zero" in result.error_message
        return True
    
    def test_power(self) -> bool:
        """Test power operation."""
        result = self.calculator.power(2, 8)
        assert result.success
        assert result.result == 256.0
        assert result.operation == "power"
        return True
    
    def test_modulus(self) -> bool:
        """Test modulus operation."""
        result = self.calculator.modulus(17, 5)
        assert result.success
        assert result.result == 2.0
        assert result.operation == "modulus"
        return True
    
    def test_floor_division(self) -> bool:
        """Test floor division operation."""
        result = self.calculator.floor_divide(17, 5)
        assert result.success
        assert result.result == 3.0
        assert result.operation == "floor_division"
        return True
    
    def test_history_tracking(self) -> bool:
        """Test that calculations are tracked in history."""
        # Clear history first
        self.calculator.clear_history()
        
        # Perform some calculations
        self.calculator.add(1, 2)
        self.calculator.multiply(3, 4)
        self.calculator.divide(10, 2)
        
        history = self.calculator.get_history()
        assert len(history) == 3
        assert history[0].operation == "addition"
        assert history[1].operation == "multiplication"
        assert history[2].operation == "division"
        return True
    
    def test_invalid_input_handling(self) -> bool:
        """Test handling of invalid inputs."""
        # Test with string input (should fail gracefully)
        result = self.calculator.add("invalid", 5)
        assert not result.success
        assert result.error_message is not None
        return True
    
    def test_float_operations(self) -> bool:
        """Test operations with floating point numbers."""
        result = self.calculator.add(3.14, 2.86)
        assert result.success
        assert abs(result.result - 6.0) < 0.001  # Allow for floating point precision
        
        result = self.calculator.multiply(2.5, 4.0)
        assert result.success
        assert result.result == 10.0
        return True
    
    def test_operator_symbols(self) -> bool:
        """Test operator symbol mapping."""
        assert get_operator("addition") == "+"
        assert get_operator("subtraction") == "-"
        assert get_operator("multiplication") == "*"
        assert get_operator("division") == "/"
        assert get_operator("power") == "**"
        assert get_operator("modulus") == "%"
        assert get_operator("floor_division") == "//"
        assert get_operator("unknown") == "?"
        return True
    
    def run_all_tests(self) -> None:
        """Run all test cases."""
        print("🧪 RUNNING CALCULATOR TESTS")
        print("=" * 50)
        
        tests = [
            ("Basic Addition", self.test_addition),
            ("Basic Subtraction", self.test_subtraction),
            ("Basic Multiplication", self.test_multiplication),
            ("Basic Division", self.test_division),
            ("Division by Zero", self.test_division_by_zero),
            ("Power Operation", self.test_power),
            ("Modulus Operation", self.test_modulus),
            ("Floor Division", self.test_floor_division),
            ("History Tracking", self.test_history_tracking),
            ("Invalid Input Handling", self.test_invalid_input_handling),
            ("Float Operations", self.test_float_operations),
            ("Operator Symbols", self.test_operator_symbols),
        ]
        
        for test_name, test_func in tests:
            self.run_test(test_name, test_func)
        
        self.print_summary()
    
    def print_summary(self) -> None:
        """Print test summary."""
        print("\n" + "=" * 50)
        print("📊 TEST SUMMARY")
        print("=" * 50)
        
        total_tests = len(self.test_results)
        passed_tests = sum(1 for _, passed, _ in self.test_results if passed)
        failed_tests = total_tests - passed_tests
        
        print(f"Total Tests: {total_tests}")
        print(f"Passed: {passed_tests} ✅")
        print(f"Failed: {failed_tests} ❌")
        print(f"Success Rate: {(passed_tests/total_tests)*100:.1f}%")
        
        if failed_tests > 0:
            print("\n❌ FAILED TESTS:")
            for test_name, passed, error in self.test_results:
                if not passed:
                    print(f"  - {test_name}: {error}")
        else:
            print("\n🎉 ALL TESTS PASSED!")
        
        print("=" * 50)


def run_demo_calculations() -> None:
    """Run a series of demo calculations to showcase functionality."""
    print("\n🎯 DEMO CALCULATIONS")
    print("=" * 50)
    
    calculator = ArithmeticCalculator()
    
    # Demo calculations with interesting results
    demo_cases = [
        ("Addition", 123456789, 987654321, "addition"),
        ("Subtraction", 1000, 999, "subtraction"),
        ("Multiplication", 123, 456, "multiplication"),
        ("Division", 22, 7, "division"),  # Approximation of π
        ("Power", 2, 10, "power"),  # 2^10 = 1024
        ("Modulus", 365, 7, "modulus"),  # Days in a week
        ("Floor Division", 365, 7, "floor_division"),  # Weeks in a year
    ]
    
    for name, a, b, operation in demo_cases:
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
    
    print("\n📝 Calculation History:")
    history = calculator.get_history()
    for i, calc in enumerate(history, 1):
        if calc.success:
            print(f"{i}. {calc.operands[0]} {get_operator(calc.operation)} {calc.operands[1]} = {calc.result}")


def main() -> None:
    """Main function to run tests and demo."""
    print("🧮 ADVANCED ARITHMETIC CALCULATOR - TEST SUITE")
    print("=" * 60)
    
    # Run unit tests
    tester = CalculatorTester()
    tester.run_all_tests()
    
    # Run demo calculations
    run_demo_calculations()
    
    print("\n🎉 Test suite completed successfully!")
    print("You can now run the interactive calculator with:")
    print("  python basic_python_arithmetic_operations.py")
    print("Or run the demo mode with:")
    print("  python basic_python_arithmetic_operations.py --demo")


if __name__ == "__main__":
    main()