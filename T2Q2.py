"""
Tutorial 2, Question 2.

Find number CAB such that AB * AB = CAB for some C.
This problem can be rewritten as AB such that:
AB**2 = 100C + AB, or C = (AB**2 - AB)/100
where A, B and C are integers
"""

class FindC:
    """Find C using 2 approaches given AB"""

    def __init__(self):
        self.num_list = []
        self.c_list = []
    
    def check_c(self, num):
        """Check the solution using mathematical identities"""

        c_value = (num**2 - num)/100
        if c_value%1 == 0 and c_value < 10:
            self.num_list.append(num)
            self.c_list.append(int(c_value))
        return 0
    
    def find_c(self):
        for i in range(0,99):
            self.check_c(i)
    

if __name__ == "__main__":
    number = FindC()
    number.find_c()
    
    if len(number.c_list) > 0:
        print("The pairs of C, AB are: ")
        for i in range(len(number.c_list)):
            print(f"{number.c_list[i]} , {number.num_list[i]:02d}")
    