# 50 Python Problems — Solved with Classes

Solutions to a set of 50 programming problems (National Pedagogical
University, Spring 2026), reimplemented in Python using OOP.
Each problem is wrapped in a class with `__init__`, `__str__`, and
where it makes sense — operator overloading and `@property` validation.

Every file is self-contained: class + tests with expected output in
comments. Every run prints a timestamp.

## Progress: 13 / 50

| # | Problem | File | Key concepts |
|---|---------|------|--------------|
| 1 | Sum of odd numbers | — | accumulator, `range` with step |
| 2 | Max of three | — | branching, `>=` edge case |
| 3 | Digit sum | — | `% 10`, `// 10`, non-destructive methods |
| 4 | Multiplication table | `../Multiplication_Table.py` | string building, `join` |
| 5 | Factorial | `Factorial.py` | `@property`, validation, mutation test |
| 6 | Prime check | `Primal.py` | `math.isqrt`, divisor pairs, early return |
| 7 | Fibonacci | `Fibonacci.py` | list accumulation, `result[-1]`/`result[-2]` |
| 8 | GCD | `GCD.py` | Euclid's algorithm, tuple swap `a, b = b, a % b` |
| 9 | Power | `power_hand.py` | loop-based exponentiation |
| 10 | Reverse number | `ReverseNumber.py` | arithmetic digit reversal |
| 11 | Word count | `word_count.py` | short-circuit guard against IndexError |
| 20 | Count vowels | `palindrome.py` | `in` operator, normalization in `__init__` |
| 24 | Palindrome | `palindrome.py` | two pointers, every path returns |

Bonus: `time_recall.py` — the `Time` class (operator overloading:
`__add__` with minute carry, `__eq__`) rewritten from scratch as an
active-recall exercise.

## How to run

    python Factorial.py

Requires Python 3.8+ (uses `math.isqrt`). No external dependencies.