# Testing in Python

Python comes with a few unique features specifically for testing.
One of those features is Doctests.
Doctests let you define simple unit tests right on your method.
This is especially useful for test-driven development, where you have explicit examples you need to code against.
Another one of those features is Mocking.
Mocking allows you to overwrite an object and control it's behavior while testing.

## Doctests

@[Can you make this doctest pass?]({"stubs": ["doc_test.py"], "command": "python3 doc_test.py"})

## Mocking

Mocking is Python's most powerful testing tool.
A Mock Object completely overwrites 