#!/usr/bin/env python3

# ukol za 2 body

def first_odd_or_even(numbers):
    """Returns 0 if there is the same number of even numbers and odd numbers
       in the input list of ints, or there are only odd or only even numbers.
       Returns the first odd number in the input list if the list has more even
       numbers.
       Returns the first even number in the input list if the list has more odd 
       numbers.

    >>> first_odd_or_even([2,4,2,3,6])
    3
    >>> first_odd_or_even([3,5,4])
    4
    >>> first_odd_or_even([2,4,3,5])
    0
    >>> first_odd_or_even([2,4])
    0
    >>> first_odd_or_even([3])
    0
    """
    
    #searches for even nums
    even = [num for num in numbers if num % 2 == 0]
    #searches for odd nums
    odd = [num for num in numbers if num % 2 != 0]
    #returns 0 if number of even is equal to odd or one of them is 0, or returns first odd if 
    #even nums > odd else returns first even
    return (0 if len(even) == len(odd) or len(even) == 0 or len(odd) == 0 else odd[0] if len(even) > len(odd) else even[0])

    
    


# ukol za 3 body
def to_pilot_alpha(word):
    """Returns a list of pilot alpha codes corresponding to the input word

    >>> to_pilot_alpha('Smrz')
    ['Sierra', 'Mike', 'Romeo', 'Zulu']
    """
    pilot_alpha = ['Alfa', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot',
        'Golf', 'Hotel', 'India', 'Juliett', 'Kilo', 'Lima', 'Mike',
        'November', 'Oscar', 'Papa', 'Quebec', 'Romeo', 'Sierra', 'Tango',
        'Uniform', 'Victor', 'Whiskey', 'Xray', 'Yankee', 'Zulu']
    
    # gets letters out of word
    upper_word = [s for s in word.upper()]

    #searches names by the letters in a word
    pilot_alpha_list = [[name for name in pilot_alpha if name.find(letter) != -1][0] for letter in upper_word]
     
    return pilot_alpha_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
