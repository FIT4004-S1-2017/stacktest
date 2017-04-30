#/usr/bin/env python-3.4
'''
A simple implementation of a stack using lists

@author rgmerk
'''

import pickle

class EmptyStackException(Exception):
    '''Exception raised if the stack is empty'''
    def __init__(self):
        pass
    
    def __str__(self):
        print("The stack is empty, bozo!")
        
class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        ''' return true if the stack contains no elements, false otherwise'''
        return not self.data

    def push(self, element):
        '''add element to the stack'''
        self.data.append(element)

    def pop(self):
        '''remove item from stack, and return it

        throw EmptyStackException if the stack is empty
        '''        
        if self.is_empty():
            return
        return self.data.pop()

    def save(self, filename):
        with open(filename, 'wb') as ofile:
            pickle.dump(self.data, ofile, 0)

    def load(self, filename):
        with open(filename, 'rb') as ifile:
            self.data=pickle.load(ifile)

if  __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.save("pickled")

    t = Stack()
    t.load("pickled")
    while (not t.is_empty()):
        print(t.pop())
            
