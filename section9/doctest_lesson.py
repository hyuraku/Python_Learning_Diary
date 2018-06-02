class Cal(object):
    def add_num_and_double(self,x,y):
        """Add and Double

        >>> c = Cal()
        >>> c.add_num_and_double(1,2)
        6

        >>> c = Cal()
        >>> c.add_num_and_double('1','1')
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x+y
        return result * 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# >Failed example:
#     c.add_num_and_double(1,2)
# Expected:
#     5
# Got:
#     6
