"""
Tutorial 3, Question 2.

Write 2 different functions.
clip_character returns a clipped string by char.
clip_word returns a clipped string by word.
"""


def clip_character(string, num):
    """Returns a string clipped to num amt of chars"""

    if not (isinstance(string, str) and isinstance(num, int)):
        raise TypeError("Wrong input.")
    string = string.strip()

    return string[:num]

def clip_word(string, num):
    """Returns a string clipped to num amt of words"""

    if not (isinstance(string, str) and isinstance(num, int)):
        raise TypeError("Wrong input.")
    string = string.strip()
    num_space = 0
    for i in range(len(string)):
        if string[i] == " ":
            num_space += 1
        if num_space == num:
            last_index = i
            break
    
    return string[:last_index]


if __name__ == "__main__":

    #Testbench Code
    test_string = (
        "This is a test string with more than 20 words and 160 characters! "
        "I love Computing and I love Nanyang Technological University! "
        "This is near the 160th character. This should be clipped."
    )
    print(clip_character(test_string, 160))
    print(clip_word(test_string, 20))