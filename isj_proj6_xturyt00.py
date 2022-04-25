#!/usr/bin/env python3

class Polynomial():

    def __init__(self,*args,**kwargs):
        """
        Constructor for Polynomial class
        a,b,c and d is a number
        Arguments as a list: [a,b, ...]
        Arguments as a sequence: a,b, ... 
        Arguments as a dictionary : x1 = a, x2 = b ... 
        """
        # if the argument is an array
        if len(args) > 0:
            if isinstance(args[0],list):
                self.args = args[0]
            else:
                self.args = list(args)
        elif len(kwargs.values()) > 0: # if the argument is a dictionary

            keys = list(kwargs.keys())
            
            #finds max key
            max_key = max([int(key[1:]) for key in keys])

            # array init with max index + 1
            self.args = [0]*(max_key+1)

            # assign values to the list
            for key in keys:
                self.args[int(key[1:])] = kwargs[key]
        else:
            self.args = [0]

        #removes all the 0 at the end
        while len(self.args) > 0:
            if self.args[-1] == 0:
                self.args.pop()
            else:
                break
    


        
    def __str__(self):
        """
        Converts list into polynom string
        return value is a string
        Example: [1,2] => "2x + 1"
        """
        res = ''
        
        # returns 0 if polynom is empty
        if len(self.args) == 0:
            return '0' 

        for index in range(len(self.args)):
            # skips 0
            if self.args[index] == 0:
                continue

            temp_val=''
            # removes "1x" 
            if abs(self.args[index]) == 1:
                temp_val = '' if index > 0 else '1'
            else:
                temp_val = str(abs(self.args[index])) if abs(self.args[index]) != 1 else '1'

            # adds X to a coefficient
            if index == 0:
                res = temp_val 
            elif index == 1:
                res = temp_val + 'x' + res 
            else:
                res = temp_val + f'x^{index}' + res 
            # places signs
            if len(self.args) - 1 != index:
                res = (' + ' if self.args[index] > 0 else ' - ') + res
            else:
                if self.args[index] < 0:
                    res = '- ' + res
                    

        return res

    # compares polynoms
    def __eq__(self, target):
        """
        Compares 2 polynoms
        return value is a bollean True or False
        Example: 2x + 1 == 2x + 1 => True
        """
        return self.__str__() == target.__str__()
    
    def __add__(self, target):
        """
        Adds up 2 polynoms
        return value is new Polynomial object with the result
        Example: (2x + 1) + (x - 1)
        """

        new = []

        # fins smaller polynom
        min_len = min(len(self.args),len(target.args))

        # adds up elements of the polynoms [small first]
        new = [self.args[index] + target.args[index] for index in range(min_len)]

        # copies the rest
        new = [*new, *self.args[min_len:]] if len(self.args) > len(target.args) else [*new, *target.args[min_len:]]

        return Polynomial(new)

    def __pow__(self,pow_size):
        """
        Powers polynom by n
        return value is a Polynomial object with the result
        Example: (2x + 1)^2 => 4x^2 + 4x + 1
        """
        
        def to_pow(args,pow_size):
            new_args = [0]* len(args) * 2
            old_args = [*self.args,*[0]*(len(new_args)-len(self.args))]
            if pow_size == 1:
                return args
            for index_mul in range(len(args)):
                for index in range(len(args)):
                    new_args[index+index_mul] += old_args[index] * args[index_mul]
            return to_pow(new_args,pow_size-1)

        return Polynomial(to_pow(self.args,pow_size))

    def derivative(self):
        """
        Finds the derivative of a polynomial
        return value is a string Polynom
        Example: x^2 + 2x + 1 => "2x + 2"
        """
        # return object
        new = []
        # shifts array to the left by 1 to remove first item
        for index in range(len(self.args)):
            if index > 0:
                new.append(self.args[index]*index) # derivates
        return Polynomial(new)
    
    def at_value(self, x_1, x_2 = None):
        """
        Calculates the result of polynom with x = x1,
        or calculates delta X = f(x2) - f(x1)
        Arguments:
        x1 - number
        x2 - number (optional)
        return value is a number
        """
        def solve_polynom(polynom,x_var):
            """
            Calculates the result of polynom,
            Arguments:
            x - number
            return value is a number
            Example: x^2 + 2x + 1 and x = 1 => 4
            """
            return sum(polynom[index] * (x_var**index) for index in range(len(polynom)))

        return solve_polynom(self.args,x_1) if x_2 is None else solve_polynom(self.args,x_2) - solve_polynom(self.args,x_1)
