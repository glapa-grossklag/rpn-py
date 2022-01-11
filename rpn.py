#!/usr/bin/env python3
"""
A Reverse Polish Notation calculator.
"""
import operator
from dataclasses import dataclass
from enum import Enum
from typing import Any

PROMPT = ">>> "

# ------------------------------------------------------------------------------
# Scanning & Parsing
# ------------------------------------------------------------------------------

operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
}


class Type(Enum):
    OPERAND = 1
    OPERATOR = 2


@dataclass
class Token:
    type: Type
    value: Any


def tokenize(stream: str) -> list[Token]:
    lexemes = stream.split()
    tokens = []
    for lexeme in lexemes:
        if lexeme.replace(".", "", 1).isnumeric():
            tokens.append(Token(Type.OPERAND, float(lexeme)))
        elif lexeme in operators:
            tokens.append(Token(Type.OPERATOR, operators[lexeme]))
        else:
            raise SyntaxError()

    return tokens


def evaluate(stream: list[Token]) -> float:
    stack = []

    for token in stream:
        match token.type:
            case Type.OPERAND:
                stack.append(token)
            case Type.OPERATOR:
                if len(stack) < 2:
                    raise SyntaxError("expected an operand")

                b = stack.pop()
                a = stack.pop()

                # In this case, the "value" of the token is a binary operator.
                result = Token(Type.OPERAND, token.value(a.value, b.value))
                stack.append(result)
            case _:
                raise NotImplementedError(f"expected one of {Type}")

    if len(stack) != 1:
        raise SyntaxError("expected operator")

    token = stack.pop()

    if token.type != Type.OPERAND:
        raise RuntimeError("something went wrong")

    return token.value


# ------------------------------------------------------------------------------
# Interactive Shell
# ------------------------------------------------------------------------------


def main():
    while True:
        stream = input(PROMPT)
        tokens = tokenize(stream)
        result = evaluate(tokens)
        print(result)


if __name__ == "__main__":
    main()
