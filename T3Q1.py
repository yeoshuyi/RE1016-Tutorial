"""
Tutorial 3, Question 1.

Encode i to 26-i
"""


import string


class ReverseEncoder:
    """Encodes a given string"""

    def __init__(self):
        self.input_string = None
        self.output_string = ""

    def encode(self, input_string):
        """Encodes string"""

        self.input_string = input_string
        for char in self.input_string:
            if 96 < ord(char) < 123:
                self.output_string += chr(219 - ord(char))
                continue
            if 64 < ord(char) < 91:
                self.output_string += chr(155 - ord(char))
                continue
            raise ValueError("Input must be a letter.")


if __name__ == "__main__":
    st = ReverseEncoder()
    st.encode("AbC")
    print(st.output_string)