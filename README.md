# rpn-py

A Reverse Polish Notation calculator.

```
>>> 2 2 +
4
>>> 100 76 -
24.0
>>> 2 10 ^
1024.0
>>> 11 2 * 7 /
3.142857142857143
>>>
```

# Architecture

1. The input stream is parsed into tokens.
	a. Every token is either an operator or an operand.
	b. All operators are binary operators (i.e., they apply to two operands.)
	c. All numbers are considered operands, and all operands are stored as
	   floating-point numbers.
2. The token stream is evaluated using shift-reduce parsing.
3. The result is displayed.
