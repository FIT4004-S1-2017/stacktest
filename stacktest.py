import unittest
from mock import *

from stack import *

class StackTests(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_emptytrue(self):
        self.assertTrue(self.stack.is_empty())

    def test_emptyfalse(self):
        self.stack.push(0)
        self.assertFalse(self.stack.is_empty())

    def test_emptied(self):
        self.stack.push(0)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_overemptied(self):
        with self.assertRaises(EmptyStackException):
            self.stack.pop()

    def test_push(self):
        self.stack.push(0)
        self.assertTrue(self.stack.pop() == 0)
        self.assertTrue(self.stack.is_empty())

    @patch('pickle.dump')
    @patch('builtins.open')
    def test_save(self,openmock,dumpmock):
        self.stack.save("fubar")
        openmock.assert_called_with("fubar", "wb")
        dumpmock.assert_called_with(self.stack.data, ANY, 0)

if __name__ == '__main__':
    unittest.main()
    with open("test.txt", "w") as ofile:
        ofile.write("test")
