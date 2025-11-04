import sys
from ft_filter import ft_filter

if __name__ == "__main__":
        """
        program that accepts two arguments: a string (S) and an integer (N). The
        program should output a list of words from S that have a length greater than N.
        • Words are separated from each other by space characters.
        • Strings do not contain any special characters (punctuation or invisible).
        • The program must contain at least one list comprehension expression and one
        lambda.
        • If the number of arguments is different from 2, or if the type of any argument is wrong,
        the program prints an AssertionError"""
        elif len(sys.argv) == 3:
            line = sys.argv[1]
        else:
            raise AssertionError("arguments are bad")
        try:
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("Argument is not an integer")
        
        words = txt.split(line)