F0 = 0
F1 = 1
# SAVE RESULTS IN HERE
saved_results = dict()

def fibonacci(n):
    assert isinstance(n, int), "Expecting an integer"
    assert n >= 0, "Integer must be larger than 1"

    # READ RESULT
    if n in saved_results:
        return saved_results[n]
    # N > 1:
    if n > 1:
        # F(N-1) + F(N-2)
        res = fibonacci(n - 1) + fibonacci(n - 2)
        # SAVE RESULT
        saved_results[n] = res
        return res
    
    # N <= 1:
    # initial conditions
    if n == 1:
        return F1
    # else if
    elif n == 0:
        return F0

import time

start_time = time.time()

f_something = fibonacci(100)

print("Took:", time.time() - start_time)

print(f_something)
