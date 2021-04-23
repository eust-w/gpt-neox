"""
run with 

```python
pytest run_tests.py
```
"""


import unittest
from tests import DuplicateArgumentTest, ArgumentUsageTest#, ValidateArgumentTest

if __name__ == "__main__":
    unittest.TextTestRunner(failfast=True)