"""
Tutorial 2, Question 3.

Generate random numbers until their sum hits 1000.
Partially vectorized solution to still use for loops taught in lesson.
First 50 numbers are immediately generated without going through sum<1000 check.

Alternative solution to generate 1000 numbers and trim to sum<1000.
Might be faster as vector operations are optimized in np.
"""


from numpy import random as rd
import time


class RandomNumGen:
    """Generate list of random numbers"""

    def __init__(self):
        self.rand_list = []
        self.rand_sum = 0

        #Standardising seed for reproducability
        rd.seed(0) if __debug__ else rd.seed(int(time.time()))
    
    def generate_list(self):
        """Iterate until sum hits 1000"""

        #Generate 50 numbers immediately without checking sum <1000
        #Slightly reduces overhead
        batch_write = rd.randint(1, 21, size=50)
        self.rand_list.extend(batch_write.tolist())
        self.rand_sum = batch_write.sum()

        while self.rand_sum < 1000:
            rand_num = rd.randint(1, 21)
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
        
