''' Write a function that takes in a non-empty array of integers that are sorted in ascending order 
and returns a new array of the same length with the squares of the original integers also sorted 
in ascending order. '''

'''For example:
      array = [1,  2,  3,  5,  6,  8,  9] 
Returns:
      [1,  4,  9,  25,  36,  64,  81]'''

def sortedSquareArray(array):    
    # for i in aray 
    x = [i*i for i in array]
    x.sort()
    return x

print(sortedSquareArray([-6, -3, -1, 2, 4, 5 ]))

      
