# Testing in Python

Python comes with a few unique features specifically for testing.
One of those features is Doctests.
Doctests let you define simple unit tests right on your method.
This is especially useful for test-driven development, where you have explicit examples you need to code against.
Another one of those features is Mocking.
Mocking allows you to overwrite an object and control it's behavior while testing.

## Doctests

@[Can you make this doctest pass?]({"stubs": ["doc_test.py"], "command": "python3 -m doctest doc_test.py"})

## Mocking

Mocking is Python's most powerful testing tool.
A Mock Object completely overwrites the object you specify.
This can be a class or a method.
Mock Objects have two special fields, return_value and side_effect.
Both of these fields effect the result of when a Mock is called.
For example:
```python runnable
from unittest import mock

def func():
    return 3

# Creating our mock
mock_func = mock.MagicMock(return_value=4)
# Overwriting the function with our mock
mock.patch("func", mock_func).start()
# Did it work?
assert func() == 4
```