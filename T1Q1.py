"""
Tutorial 1, Question 1.

Calculates average speed of 100m race in mph based on time in seconds.
"""


class SpeedCalculator:
    """Speed conversion for 100m race."""

    #Defined as speed(mph) = CONVERSION_FACTOR / time(s)
    CONVERSION_FACTOR = 223.6936

    def __init__(self):
        self.time = None
        self.speed = None
    
    def get_time_speed(self):
        """Prompts user for time, calculates speed."""

        while True:
            print("Input 100m Time (s): ", end='')
            usr_input = input()
            try:
                time_val = float(usr_input)
                if time_val > 0:
                    self.time = time_val
                    self.speed = self.CONVERSION_FACTOR / time_val
                    break
                print("Time must be more than 0.\n")
            except ValueError:
                print("Wrong Input Type! Please try again.\n")
        
        return self.speed


if __name__ == "__main__":
    runner = SpeedCalculator()
    print(f"\nAverage Speed: {runner.get_time_speed()}mph")

    #Alternatively, we can also use the class variable
    #runner.get_time_speed()
    #print(f"\nAverage Speed: {runner.speed}mph")
