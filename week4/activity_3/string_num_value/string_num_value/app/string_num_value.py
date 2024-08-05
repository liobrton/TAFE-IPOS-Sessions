def is_valid_string(s):
    """
    Validate that the string inputted has no special characters.
    :param s: String
    """
    for char in s:
        if char.isnumeric() is False and char.isalpha() is False:
            return False
    return True


class StringNumValue:
    """
    This class calculates the numeric value of any string. It can be
    initialised with a string. The string can be overriden using the {set}
    method or the user may append to it using the {append} method.

    This class returns the value of the string like this:
    a (or A) => 1
    b (or B) => 2
    ...
    z (or Z) => 26

    0 => 0
    1 => 1
    ...
    9 => 9

    In short, numeric characters retain their value and the letters of the
    alphabet are converted. Any other characters count as 0.

    If a string contains multiple characters, the value of the entire string
    is the sum of the values of each separate character. **This is not yet
    implemented and is part of the exercise!**
    """
    def __init__(self, s=''):
        if is_valid_string(s):
            self.string = s
        else:
            raise TypeError("String can only be comprised of numeric or alphabetical characters.")

    @property
    def value(self):
        """
        Calculate and return the value of the string based on the rules laid
        out in the docstring of the class.

        :return: The numeric value of the string
        """

        return_value = 0
        UNICODE_START = 96

        for char in self.string:
            if char.isnumeric():
                char = int(char)
            else:
                char = ord(char.lower()) - UNICODE_START
            return_value = return_value + char

        return return_value
        # return ord(self.string) - ord('0') if len(self.string) else 0

    def set(self, s):
        """
        Overwrite the value of the string.

        :param s: String to write
        """
        if is_valid_string(s):
            self.string = s
        else:
            raise TypeError("String can only be comprised of numeric or alphabetical characters.")

    def append(self, s):
        """
        Append a new string to the end of the existing string.

        :param s: String to append
        """
        if is_valid_string(s):
            self.string = self.string + s
        else:
            raise TypeError("String can only be comprised of numeric or alphabetical characters.")

    @property
    def get_string(self):
        return self.string
