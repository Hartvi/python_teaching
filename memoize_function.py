
def memoize_function(f):
    cached_results = dict()  # {1: 10, 2: 20}

    def calculate(*args):
        # add(a, b) 
        #  => `args` se v tomhle pripade rovna (a, b)
        # kdyz napiseme `add(*args)`, tak to je to samy jako `add(*(a, b))` coz je to samy jako add(a, b)
        # kdybychom tam nedali `*`, tak to bude volat `add((a, b))` 
        
        inputs: tuple = args  # tuple
        
        print("cached_results length:", len(cached_results))
        if inputs in cached_results:
            # print("Memoization:", inputs, cached_results[inputs])
            return cached_results[inputs]
        else:
            # f(inputs)
            res = f(*inputs)
            cached_results[inputs] = res
            return res
    
    return calculate


F0 = 0
F1 = 1
# F(N) = F(N-1) + F(N-2) | N > 1

# define function:
def fibonacci(n):
    # print("n:", n, "  type(n):", type(n))
    assert isinstance(n, int), "Expecting an integer"
    assert n >= 0, "Integer must be larger than 1"

    # N > 1:
    if n > 1:
        # F(N-1) + F(N-2)
        return fibonacci(n - 1) + fibonacci(n - 2)
    
    # N <= 1:
    # initial conditions
    if n == 1:
        return F1
    # else if
    elif n == 0:
        return F0


new_fibonacci = memoize_function(fibonacci)

import time


# new_fibonacci(1) => 1
# new_fibonacci(2) => 2

# new_fibonacci(30) => 30

num = 30
for i in range(num):
    new_fibonacci(i)

start_time = time.time()
f_something = new_fibonacci(num)

print("Took:", time.time() - start_time)

print(f_something)