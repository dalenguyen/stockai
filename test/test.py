
import sys

if sys.version_info < (2, 7):
    from unittest2 import main as test_main, SkipTest, TestCase
else:
    from unittest import main as test_main, SkipTest, TestCase

from stockai.settings import Values
from stockai import Base

test = Base._prepare_request()
print(test)