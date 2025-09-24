#!/usr/bin/env python3

def operate(a=None, b=None, op=None):
    if a is None or b is None or op is None:
        return None

    if op == 'add':
        return a + b
    elif op == 'subtract':
        return a - b
    elif op == 'multiply':
        return a * b
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

