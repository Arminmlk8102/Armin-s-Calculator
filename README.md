# Armin's Calculator
#### Video Demo:  <https://youtu.be/2CQuQfV5ZQ0?si=FjRjmz672l0oq3h8>
#### Description:

Armin's Calculator !

as a mechanical engineer I'm always in need of a calculator that can handle my calculations, so for that and with the help
of this course, I was able to impliment my own Calculator !

My calculator uses two libraries : Tkinter and math
Tkinter was used to design the Calculator as an app when executed and with the help of math I was able to bring complex operators like
ln, sin, cos, tan, log to life without too much calculation Errors.

I have defined several conditions to prevent calculation errors and the things that are not defined in Mathematical world such as divid by zero.

it Features

Basic Arithmetic Operations:

Addition (+)

Subtraction (-)

Multiplication (x)

Division (÷)

Exponentiation (^)

Scientific Functions:

Square root (√)

Sine, Cosine, Tangent (in degrees)

Natural logarithm (ln)

Base-10 logarithm (log)

π (Pi) insertion

Utility Functions:

Clear All (AC)

Negate number (+/-)

Percentage (%)

Delete last digit (del)

Error Handling:

Division by zero

Invalid input for logarithmic functions (ln or log)

Undefined values for tangent (e.g., tan(90°))

User Interface:

The interface is created using tkinter.Frame and tkinter.Button.

Buttons are categorized by color to indicate function types:

Green buttons for numerical input

Black background for operators and scientific functions

The display label shows the current input or result with dynamic updates.

Implementation Details

Button Layout:
Buttons are organized into a 7x4 grid (7 rows, 4 columns). Each button is dynamically assigned a function using a lambda function, connecting user interaction to the button_clicked callback function.

Event Handling:
The button_clicked(value) function handles all button interactions. Depending on the button pressed, it distinguishes between:

Numerical input (0–9 and .)

Basic arithmetic operations (+, -, x, ÷, ^)

Scientific functions (sin°, cos°, tan°, ln, log, √)

Utility functions (AC, +/-, %, π, del)

Calculation Logic:

The calculator maintains a simple state with variables A, B, and Operator.

When an operator is pressed, A stores the first operand, Operator stores the operation type, and B stores the second operand upon pressing =.

Error handling ensures invalid operations (like division by zero or ln(0)) display a user-friendly Error message instead of crashing.

Scientific Functions:

Trigonometric functions are calculated using math.sin, math.cos, math.tan after converting degrees to radians.

Special attention is given to undefined tangent values at angles like 90° and 270°.

ln and log functions include validation for non-positive numbers to prevent mathematical errors.

Display Formatting:

The remove_zero_decimal(num) function ensures that numbers are displayed cleanly, without unnecessary .0 decimals.

Responsive Window Placement:

The window is centered on the screen using dynamic calculation of screen and window dimensions.

Resizing is disabled to maintain a consistent interface layout.

Usage

Run the script using Python 3.x.

Use the buttons to enter numbers and perform calculations.

Use the scientific function buttons for advanced mathematical operations.

Clear entries using AC or remove digits using del.

Dependencies

Python 3.x

Standard library only (tkinter and math) — no external packages required.

Future Enhancements

Support for parentheses and operator precedence.

Ability to handle more advanced scientific functions like e^x, factorial, and mod.

Improved UI with themes, animations, or dynamic resizing.
