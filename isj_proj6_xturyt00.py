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
            if type(args[0]) != list:
                self.args = list(args[:])
            else:
                self.args = args[0][:]
        else: # if the argument is a dictionary
            # find max index
            max_index = list(sorted(kwargs.keys())[-1]).pop()
            # array init with max index + 1
            self.args = [0]*(int(max_index)+1)
            # assign values to the list
            for key in sorted(kwargs.keys()):
                self.args[int(list(key).pop())] = kwargs[key]
        
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

        for i in range(len(self.args)):
            # skips 0
            if self.args[i] == 0:
                continue

            k=''
            # removes "1x" 
            if abs(self.args[i]) == 1:
                k = '' if i > 0 else '1'
            else:
                k = str(abs(self.args[i])) if abs(self.args[i]) != 1 else '1'

            # adds X to a coefficient
            if i == 0:
                res = k 
            elif i == 1:
                res = k + 'x' + res 
            else:
                res = k + f'x^{i}' + res 
            # places signs
            if len(self.args) - 1 != i:
                res = (' + ' if self.args[i] > 0 else ' - ') + res
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

        new = Polynomial(self.args)

        # fins smaller polynom
        min_len = min(len(new.args),len(target.args))
        # adds up elements of the polynoms [small first]
        res = [new.args[index] + target.args[index] for index in range(min_len)]
        # copies the rest
        new.args = [*res, *new.args[min_len:]] if len(new.args) > len(target.args) else [*res, *target.args[min_len:]]

        return new

    def __pow__(self,n):
        """
        Raises a polynomial to a power (newton binomial)
        Parameters:
        n - number (pow)
        return value is new Polynomial object with the result
        Example: (x + 1)^2 => x^2 + 2x + 1
        """
        # return object
        new = Polynomial([])

        def binomialCoeff(n, k):
            """
            Calculates coefficient for each position in a polynom of pow of n
            n - pow
            k - coefficient position
            return value is a number
            """
            if k > n:
                return 0
            if k == 0 or k == n:
                return 1
 
            return binomialCoeff(n - 1, k - 1) + binomialCoeff(n - 1, k)
        # calculates pow for each element of the polynom
        for index in range(n+1):
            new.args.append(binomialCoeff(n,index)*(self.args[0]**(n-index))*(self.args[1]**index))
        

        return new

    def derivative(self):
        """
        Finds the derivative of a polynomial
        return value is a string Polynom
        Example: x^2 + 2x + 1 => "2x + 2"
        """
        # return object
        new = Polynomial([])
        # shifts array to the left by 1 to remove first item
        for index in range(len(self.args)):
            if index > 0:
                new.args.append(self.args[index]*index) # derivates
        return new
    
    def at_value(self, x1, x2 = None):
        """
        Calculates the result of polynom with x = x1,
        or calculates delta X = f(x2) - f(x1)
        Arguments:
        x1 - number
        x2 - number (optional)
        return value is a number
        """
        def solve_polynom(polynom,x):
            """
            Calculates the result of polynom,
            Arguments:
            x - number
            return value is a number
            Example: x^2 + 2x + 1 and x = 1 => 4
            """
            return sum(polynom[index] * (x**index) for index in range(len(polynom)))

        return solve_polynom(self.args,x1) if x2 is None else solve_polynom(self.args,x2) - solve_polynom(self.args,x1)

