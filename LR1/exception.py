import sys

class Ex():
    """ Exception class """
    def ex_index(self, lst, el):
        """ Try to use function index() """
        try: 
           lst.index(el)
           return int(lst.index(el))
        except BaseException:
            self.printf(self)
            
    def printf(self):
        """ To stop a session """
        print('Failed')
        sys.exit()


class Ex_p(Ex): 
    """ Exception class for insert() of list with pins """
    def printf(self):
        print('Your pin is not correct\nTry adain')
        sys.exit()


class Ex_n(Ex): 
    """ Exception class for insert() of list with numbers """
    def printf(self):
        print('Card number does not exist\nTry again')
        sys.exit()
