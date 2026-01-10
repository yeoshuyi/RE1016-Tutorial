"""
Tutorial 2, Question 3.

Generate random numbers until their sum hits 1000.
"""


from numpy import random as rd


class RandomNumGen:
    """Generate list of random numbers"""

    def __init__(self):
        self.rand_list = []
        self.rand_sum = 0

        #Standardising seed for reproducability
        rd.seed(0)
    
    def generate_list(self):
        """Iterate until sum hits 1000"""

        while self.rand_sum < 1000:
            rand_num = rd.randint(1, 20)
            self.rand_list.append(rand_num)
            self.rand_sum += rand_num
        
        return 0


if __name__ == "__main__":
    rand = RandomNumGen()
    rand.generate_list()
    print(
        f"Random numbers summed to: {rand.rand_sum}\n"
        f"List contains: {rand.rand_list}"
    )
        
