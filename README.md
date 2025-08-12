# 🧮 Advanced Arithmetic Calculator

A comprehensive Python calculator that performs various arithmetic operations with proper error handling, type hints, and a user-friendly interface.

## ✨ Features

- **Multiple Operations**: Addition, subtraction, multiplication, division, power, modulus, and floor division
- **Error Handling**: Comprehensive error handling for invalid inputs and division by zero
- **Type Safety**: Full type hints for better code maintainability
- **Calculation History**: Track and view all previous calculations
- **Interactive Interface**: User-friendly menu-driven interface
- **Demo Mode**: Run predefined calculations for testing
- **Modern Python**: Uses dataclasses, type hints, and modern Python features

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- No external dependencies required (uses only built-in modules)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd <your-repo-name>
```

2. Run the calculator:
```bash
python basic_python_arithmetic_operations.py
```

### Usage

#### Interactive Mode
```bash
python basic_python_arithmetic_operations.py
```

#### Demo Mode
```bash
python basic_python_arithmetic_operations.py --demo
```

## 📋 Available Operations

| Operation | Symbol | Description |
|-----------|--------|-------------|
| Addition | `+` | Add two numbers |
| Subtraction | `-` | Subtract second number from first |
| Multiplication | `*` | Multiply two numbers |
| Division | `/` | Divide first number by second |
| Power | `**` | Raise base to the power of exponent |
| Modulus | `%` | Calculate remainder of division |
| Floor Division | `//` | Perform floor division |

## 🏗️ Project Structure

```
├── basic_python_arithmetic_operations.py  # Main calculator application
├── requirements.txt                       # Python dependencies
├── README.md                             # Project documentation
└── .gitignore                            # Git ignore file
```

## 🔧 Code Architecture

### Core Classes

#### `ArithmeticCalculator`
The main calculator class that handles all arithmetic operations:
- **Methods**: `add()`, `subtract()`, `multiply()`, `divide()`, `power()`, `modulus()`, `floor_divide()`
- **Features**: Error handling, calculation history, type safety

#### `CalculationResult`
A dataclass to store calculation results:
- **Fields**: `operation`, `operands`, `result`, `success`, `error_message`
- **Purpose**: Structured result storage with success/failure status

### Key Functions

- `main()`: Main application loop
- `run_demo()`: Demonstration mode with predefined calculations
- `get_user_input()`: Safe user input handling
- `display_menu()`: User interface
- `display_result()`: Formatted result output
- `display_history()`: Calculation history display

## 🧪 Testing

### Manual Testing
Run the demo mode to see all operations in action:
```bash
python basic_python_arithmetic_operations.py --demo
```

### Example Output
```
🎯 DEMONSTRATION MODE
==================================================
✅ Addition: 4 + 7 = 11.0
✅ Subtraction: 4 - 7 = -3.0
✅ Multiplication: 4 * 7 = 28.0
✅ Division: 4 / 7 = 0.5714285714285714
✅ Power: 2 ** 3 = 8.0
✅ Modulus: 17 % 5 = 2.0
✅ Floor Division: 17 // 5 = 3.0

📝 Final History:
--------------------------------------------------
1. 4 + 7 = 11.0
2. 4 - 7 = -3.0
3. 4 * 7 = 28.0
4. 4 / 7 = 0.5714285714285714
5. 2 ** 3 = 8.0
6. 17 % 5 = 2.0
7. 17 // 5 = 3.0
--------------------------------------------------
```

## 🛡️ Error Handling

The calculator includes comprehensive error handling for:
- **Division by zero**: Prevents crashes and provides clear error messages
- **Invalid input**: Handles non-numeric input gracefully
- **Type errors**: Converts inputs to appropriate types safely
- **Keyboard interrupts**: Graceful exit on Ctrl+C

## 🔄 Future Enhancements

Potential improvements for future versions:
- [ ] Scientific calculator functions (sin, cos, log, etc.)
- [ ] Memory functions (M+, M-, MR, MC)
- [ ] File-based calculation history persistence
- [ ] GUI interface using tkinter or PyQt
- [ ] Unit tests with pytest
- [ ] Configuration file support
- [ ] Plugin system for custom operations

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

[Your Name] - [Your Email]

## 🙏 Acknowledgments

- Python community for excellent documentation
- PEP 8 for code style guidelines
- Type hints for better code maintainability

---

**Happy Calculating! 🎉**
