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
    
    def list_reset(self):
        """Resets all list to blank"""

        self.rand_list = []
        self.rand_sum = 0

    def generate_list_bruteforce(self):
        """Generate ints 1-20 until either sum > 1000 or 100 ints generated"""

        self.list_reset()
        count = 0
        while self.rand_sum < 1000 and count < 100:
            generate_random = np.random.randint(1, 21)
            self.rand_list.append(generate_random)
            self.rand_sum += generate_random
            count += 1

    def generate_list_minbatch(self):
        """Generate list of 50 ints 1-20 and add"""

        #Generate 50 numbers immediately, guranteed to not exceed 1000
        self.list_reset()
        self.rand_list.extend(np.random.randint(1, 21, size=50).tolist())
        self.rand_sum = np.sum(self.rand_list)
        count = 0

        while self.rand_sum < 1000 and count < 50:
            generate_random = np.random.randint(1, 21)
            self.rand_list.append(generate_random)
            self.rand_sum += generate_random
            count += 1

    def generate_list_maxbatch(self):
        """Generate list of 100 ints 1-20 and trim"""

        #Generate 100 numbers immediately without checking sum <1000
        self.list_reset()
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


def main():
    """Get user input on generation type and print results"""

    while True:
        try:
            option = input(
                f"Please select from the following generation options:\n"
                f"1. Bruteforce Method\n"
                f"2. Minbatch Method\n"
                f"3. Maxbatch Method\n"
                f"Select: "
            )
            option = int(option)
            if 0 < option < 4:
                break
            else:
                print("Please select 1-3.")
                continue
        except ValueError:
            print("Wrong input type.")

    rand = RandomNumGen()
    match option:
        case 1:
            current_time = time.time()
            rand.generate_list_bruteforce()
        case 2:
            current_time = time.time()
            rand.generate_list_minbatch()
        case 3:
            current_time = time.time()
            rand.generate_list_maxbatch()
    
    print(
        f"Random numbers summed to {rand.rand_sum} with {len(rand.rand_list)} elements.\n"
        f"List contains: {rand.rand_list}\n"
        f"Generation took {(time.time()-current_time) * 1000 * 1000:.3f}us."
    )


if __name__ == "__main__":
    main()
