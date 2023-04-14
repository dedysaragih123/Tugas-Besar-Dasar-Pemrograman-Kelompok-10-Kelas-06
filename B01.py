from time import time
#GENERATE RANDOM NUMBER
random = int(time())
def randomize(lower_bound : int, upper_bound : int) -> int:
    a = 1583458089
    b = 1132489760
    m = (2**31) - 1
    global random
    random = (a*random + b) % m
    while random % (upper_bound + 1) < lower_bound:
        random = (a*random + b) % m
    return random % (upper_bound + 1)