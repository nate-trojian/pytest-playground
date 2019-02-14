# In Depth Mocking Example
How would you mock the `func` method?
```python
from unittest import mock


class Test:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def hello(self):
        return 1


def new_test():
    return Test()


def func():
    with new_test() as t:
        return t.hello()
```

::: Answer
``` python
def test_TestWith():
    test_hello_mock = mock.MagicMock(return_value=2)
    test_enter_ret_mock = mock.MagicMock(
        hello=test_hello_mock
    )
    test_enter_mock = mock.MagicMock(
        return_value=test_enter_ret_mock
    )
    test_mock = mock.MagicMock(
        __enter__=test_enter_mock,
        __exit__=mock.MagicMock(return_value=None)
    )
    patcher = mock.patch("__main__.new_test", return_value=test_mock)
    patcher.start()
    ret = func()
    test_mock.__enter__.assert_called_once()
    test_mock.__exit__.assert_called_once()
    assert ret == 2
    patcher.stop()
```
:::
