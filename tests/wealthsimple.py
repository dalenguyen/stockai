import sys
sys.path.append('../stockai')

if sys.version_info < (2, 7):
    from unittest2 import main as test_main, SkipTest, TestCase
else:
    from unittest import main as test_main, SkipTest, TestCase

from stockai import WealthSimple


# class TestStock(TestCase):

#     def setUp(self):
#         self.ws = WealthSimple()

#     def test_td_summary_profile(self):
#         print(self.ws.test())
#         self.assertEqual(self.ws.test(), 'test')


# if __name__ == "__main__":
#     test_main()
