"""
Tutorial 2, Question 3.

Generate 100 and trim to avoid long while loop.
This reduces overhead compared to a generate and check loop.
Where N = 100 elements, time and space complexity is O(N).
"""

import numpy as np
import time


class RandomNumGen:
    """Generate list of random numbers"""

    def __init__(self):
        self.rand_list = []
        self.rand_sum = 0

        #Standardising seed for reproducability
        np.random.seed(0) if __debug__ else np.random.seed(int(time.time()))
    
    def generate_list(self):
        """Generate list of 100 ints 1-20 and trim"""

        #Generate 100 numbers immediately without checking sum <1000
        self.rand_list.extend(np.random.randint(1, 21, size=100).tolist())
        self.rand_sum = np.sum(self.rand_list)

        if self.rand_sum <= 1000:
            return self.rand_list

        while self.rand_sum > 999:
            last_item = self.rand_list[-1]
            self.rand_list.pop()
            self.rand_sum -= last_item
        
        self.rand_list.append(last_item)
        self.rand_sum += last_item
        
        return self.rand_list


if __name__ == "__main__":
    current_time = time.time()
    rand = RandomNumGen()
    rand.generate_list()
    print(
        f"Random numbers summed to {rand.rand_sum} with {len(rand.rand_list)} elements.\n"
        f"List contains: {rand.rand_list}\n"
        f"Generation took {(time.time()-current_time):.4f}s."
    )
        
