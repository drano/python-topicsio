import unittest
from tests.client import ClientTestCase

def all_tests():
    suite = unittest.TestSuite()
    suite.addTest( unittest.makeSuite( ClientTestCase))
    return suite