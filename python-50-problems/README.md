# 50 C++ Problems — Solved in Python with OOP

Solutions to 50 programming problems (National Pedagogical University
of Uzbekistan, Spring 2026), originally written for C++, reimplemented
here in Python using classes: `__init__`, `__str__`, operator
overloading and `@property` validation where it makes sense.

Every file is self-contained: class + test calls with expected output
in comments. Most runs print a timestamp.

## Progress: 28 / 50

Numbering follows the original problem set exactly.

| # | Problem | File | Key concepts |
|---|---------|------|--------------|
| 4 | Multiplication table | `../Multiplication_Table.py` | string building, `join` |
| 5 | Factorial | `Factorial.py` | `@property`, validation, mutation test |
| 6 | Prime check | `Primal.py` | `math.isqrt`, divisor pairs, early return |
| 7 | Count digits of a number | `Count_Digits_of_a_Number.py` | `while`, `% 10` / `// 10` |
| 8 | Sum of even numbers 1..N | `sum_of_even_numbers.py` | accumulator |
| 9 | Fibonacci first N terms | `Fibonacci.py` | list accumulation, `result[-1]`/`result[-2]` |
| 10 | Celsius to Fahrenheit | `celsius_to_fahrenheit.py` | simple formula |
| 11 | GCD of two numbers | `GCD.py` | Euclid's algorithm, tuple swap |
| 12 | Power function | `Pover.py` | loop-based exponentiation |
| 13 | Count down from N | `count_down_from_n.py` | list + join, reverse range |
| 14 | Even or odd check | `even_or_odd_check.py` | `@property`, ternary in `__str__` |
| 15 | Sum of numbers in range | `sum_of_numbers_in_range.py` | accumulator with custom bounds |
| 16 | Reverse a number | `Reverse Number.py` | arithmetic digit reversal |
| 17 | Reverse an array | `Reverse_Array.py` | negative indexing |
| 18 | Count uppercase letters | `count_uppercase_letters.py` | `.isupper()` |
| 19 | Average of array | `Average_of_List.py` | `@property`, empty-list validation |
| 20 | Count vowels in a word | `palindrome.py` | `in` operator, normalization in `__init__` |
| 21 | Find minimum in array | `find_minimum_in_array.py` | single-pass tracking |
| 22 | Count occurrences in array | `count_occurrences_in_array.py` | linear scan + counter |
| 23 | Reverse a string | `reverse_a_string.py` | negative indexing, string immutability |
| 24 | Palindrome check | `palindrome.py` | two pointers, every path returns |
| 25 | Count words in a sentence | `word_count.py` | short-circuit guard against IndexError |
| 26 | Find second largest | `Second_Largest.py` | two-tracker pattern, negative numbers |
| 28 | Largest vs smallest difference | `largest_vs_smallest_difference.py` | single-pass min+max, `@property` |
| 35 | Min and max of array | `Find_Min_and_Max_in_One_Pass.py` | two independent trackers |
| 42 | Count even and odd in array | `Count_Even_and_Odd.py` | single-pass classification |

### Known gaps
- Remaining problems (31–34, 36–41, 43–50) not yet attempted.

## Bonus exercises (not part of the original 50)

| File | Description |
|---|---|
| `Character_Frequency.py` / `Frequency_of_Every_Character.py` | Hashmap pattern: count + find most frequent character |
| `Remove_Duplicates.py` | Dedup a list while preserving order |
| `Sum_of_squares.py` | Accumulator variant |
| `text_stats.py` | Classify characters into uppercase/lowercase/digit/other via dict |
| `time_recall.py` | `Time` class rebuilt from scratch — active recall exercise (operator overloading) |
| `word_recall.py` | `Word` class rebuilt from scratch — active recall exercise (two pointers, `in`) |

## How to run

    python Factorial.py
    python name of the file.py

Requires Python 3.8+ (uses `math.isqrt`). No external dependencies.