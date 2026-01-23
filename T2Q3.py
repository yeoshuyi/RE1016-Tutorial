"""
Tutorial 2, Question 3.

Generate up to 100 random integers that sum up to 1000.
Each integer ranges 1 - 20.

3 methods of generation is proposed, using:
a) Bruteforce, b) Min Batch, c) Max Batch, d) Max Batch with Cumulative Sum
"""


import numpy as np
import time


class RandomNumGen:
    """Generate list of random numbers, with 3 methods available."""

    def __init__(self):
        """
        Initialise generator and decide seed.\n
        Run in debug mode for fixed seed (0), else seed is based on system time.
        """

        self.rand_list = []
        self.rand_sum = 0

        #Standardising seed for reproducability
        np.random.seed(0) if __debug__ else np.random.seed(int(time.time()))
    
    def list_reset(self):
        """Resets rand_list and rand_sum to empty."""

        self.rand_list = []
        self.rand_sum = 0

    def generate_list_bruteforce(self):
        """
        Generate a list of I until either the sum reaches 1000, or len(list) reaches 100,
        where I is an integer ranging from 1-20.\n
        Bruteforce method appends one integer and checks sum with ever iteration.
        """

        self.list_reset()
        count = 0
        while self.rand_sum < 1000 and count < 100:
            generate_random = np.random.randint(1, 21)
            self.rand_list.append(generate_random)
            self.rand_sum += generate_random
            count += 1
        return self.rand_list

    def generate_list_minbatch(self):
        """
        Generate a list of I until either the sum reaches 1000, or len(list) reaches 100,
        where I is an integer ranging from 1-20.\n
        Minbatch method generates 50 integers immediately, and appends with each iteration.
        """

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
        return self.rand_list

    def generate_list_maxbatch(self):
        """
        Generate a list of I until either the sum reaches 1000, or len(list) reaches 100,
        where I is an integer ranging from 1-20.\n
        Maxbatch method generates 100 integers immediately, and trims with each iteration.
        """

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
    
    def generate_list_maxbatch_vec(self):
        """
        Generate a list of I until either the sum reaches 1000, or len(list) reaches 100,
        where I is an integer ranging from 1-20.\n
        Maxbatch method generates 100 integers immediately, and trims using cumulative sum.
        """

        #Generate 100 numbers immediately without checking sum <1000
        self.list_reset()
        temporary_list = (np.random.randint(1, 21, size=100).tolist())
        self.rand_sum = np.sum(temporary_list)
        if self.rand_sum <= 1000:
            self.rand_list.extend(temporary_list)
            return self.rand_list
    
        cumulative_sum = np.cumsum(temporary_list)

        #Find index where cumulative sum first exceeds 1000
        index = np.searchsorted(cumulative_sum, 999, "right") + 1
        self.rand_list.extend(temporary_list[:index])
        self.rand_sum = np.sum(self.rand_list)
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
                f"4. Cumulative Sum Maxbatch Method\n"
                f"Select: "
            )
            option = int(option)
            if 0 < option < 5:
                break
            else:
                print("Please select 1-4.")
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
        case 4:
            current_time = time.time()
            rand.generate_list_maxbatch_vec()
    
    print(
        f"-------------------------------------------------------------\n"
        f"Random numbers summed to {rand.rand_sum} with {len(rand.rand_list)} elements.\n"
        f"List contains: {rand.rand_list}\n"
        f"Generation took {(time.time()-current_time) * 1000 * 1000:.3f}us."
    )


if __name__ == "__main__":
    main()
