"""
Tutorial 2, Question 3.

Generate up to MAX_LIST_SIZE random integers that sum exceeds MAX_LIST_SUM.
Each integer ranges MIN_RANDOM to MAX_RANDOM.

4 methods of generation is proposed, using:
a) Bruteforce, b) Min Batch, c) Max Batch, d) Max Batch with Cumulative Sum
All methods follow O(n) time and space complexity.
"""


import numpy as np
import time


MAX_LIST_SIZE = 100
MAX_LIST_SUM = 1000
MIN_RANDOM = 1
MAX_RANDOM = 20


class RandomNumGen:
    """Generate list of random numbers, with 3 methods available."""

    def __init__(self):
        """
        Initialise generator and decide seed.\n
        Run in debug mode for fixed seed (0), else seed is based on system time.
        """

        self.rand_list = []
        self.rand_sum = 0

        #Standardising seed for reproducability when debugging
        np.random.seed(0) if __debug__ else np.random.seed(int(time.time()))
    
    def list_reset(self):
        """Resets rand_list and rand_sum to empty."""

        self.rand_list = []
        self.rand_sum = 0

    def generate_list_bruteforce(self):
        """
        Generate a list of I until either the sum reaches MAX_LIST_SUM, or len(list) reaches MAX_LIST_SIZE,
        where I is an integer ranging from MIN_RANDOM to MAX_RANDOM.\n
        Bruteforce method appends one integer and checks sum with ever iteration.\n
        Returns list by defualt.
        """

        self.list_reset()
        count = 0
        while self.rand_sum < MAX_LIST_SUM and count < MAX_LIST_SIZE:
            generate_random = np.random.randint(MIN_RANDOM, MAX_RANDOM+1)
            self.rand_list.append(generate_random)
            self.rand_sum += generate_random
            count += 1
        return self.rand_list

    def generate_list_minbatch(self):
        """
        Generate a list of I until either the sum reaches MAX_LIST_SUM, or len(list) reaches MAX_LIST_SIZE,
        where I is an integer ranging from MIN_RANDOM to MAX_RANDOM.\n
        initial_size is the maximum size such that list is GURANTEED to be below MAX_LIST_SUM.\n
        Minbatch method generates initial_size integers immediately, and appends with each iteration.\n
        Returns list by defualt.
        """

        self.list_reset()
        initial_size = min(MAX_LIST_SUM // MAX_RANDOM, MAX_LIST_SIZE)
        self.rand_list.extend(np.random.randint(MIN_RANDOM, MAX_RANDOM+1, size=initial_size).tolist())
        self.rand_sum = np.sum(self.rand_list)
        count = initial_size

        while self.rand_sum < MAX_LIST_SUM and count < MAX_LIST_SIZE:
            generate_random = np.random.randint(MIN_RANDOM, MAX_RANDOM+1)
            self.rand_list.append(generate_random)
            self.rand_sum += generate_random
            count += 1
        return self.rand_list

    def generate_list_maxbatch(self):
        """
        Generate a list of I until either the sum reaches MAX_LIST_SUM, or len(list) reaches MAX_LIST_SIZE,
        where I is an integer ranging from MIN_RANDOM to MAX_RANDOM.\n
        Maxbatch method generates MAX_LIST_SIZE integers immediately, and trims with each iteration.\n
        Returns list by defualt.
        """

        self.list_reset()
        self.rand_list.extend(np.random.randint(MIN_RANDOM, MAX_RANDOM+1, size=MAX_LIST_SIZE).tolist())
        self.rand_sum = np.sum(self.rand_list)

        if self.rand_sum <= MAX_LIST_SUM:
            return self.rand_list

        while self.rand_sum > MAX_LIST_SUM-1:
            last_item = self.rand_list[-1]
            self.rand_list.pop()
            self.rand_sum -= last_item
        
        self.rand_list.append(last_item)
        self.rand_sum += last_item
        return self.rand_list
    
    def generate_list_maxbatch_vec(self):
        """
        Generate a list of I until either the sum reaches MAX_LIST_SUM, or len(list) reaches MAX_LIST_SIZE,
        where I is an integer ranging from MIN_RANDOM to MAX_RANDOM.\n
        Maxbatch method generates MAX_LIST_SIZE integers immediately, and trims using cumulative sum.\n
        Returns list by defualt.
        """

        self.list_reset()
        temporary_list = (np.random.randint(MIN_RANDOM, MAX_RANDOM+1, size=MAX_LIST_SIZE))
        self.rand_sum = np.sum(temporary_list)
        if self.rand_sum <= MAX_LIST_SUM:
            self.rand_list.extend(temporary_list.tolist())
            return self.rand_list
    
        cumulative_sum = np.cumsum(temporary_list)

        #Find index where cumulative sum first exceeds 1000
        index = np.searchsorted(cumulative_sum, MAX_LIST_SUM-1, "right") + 1
        self.rand_list.extend(temporary_list.tolist()[:index])
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
                print(f"\n-------------------------------------------------------------\n"
                      f"Please select 1-4.\n"
                      f"-------------------------------------------------------------\n"
                )
                continue
        except ValueError:
            print(
                f"\n-------------------------------------------------------------\n"
                f"Wrong input type.\n"
                f"-------------------------------------------------------------\n"
            )

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
        f"List contains: {rand.rand_list}\n"
        f"Random numbers summed to {rand.rand_sum} with {len(rand.rand_list)} elements.\n"
        f"Generation took {(time.time()-current_time) * 1000 * 1000:.3f}us.\n"
        f"-------------------------------------------------------------"
    )


if __name__ == "__main__":
    main()
