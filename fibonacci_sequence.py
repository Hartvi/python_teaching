

F0 = 0
F1 = 1
# F(N) = F(N-1) + F(N-2) | N > 1

# define function:
def fibonacci(n):
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

# == je to samy jako `is_equal_to`
# = je `assign right hand side to the left hand side`
import time

start_time = time.time()

f_something = fibonacci(30)

print("Took:", time.time() - start_time)

print(f_something)



"""
f(1) => F1
f(2) => (f(1) + f(0))
f(3) => f(2) + f(1) => ((f(1) + f(0)) + f(1))
f(4) => f(3) + f(2) => ((f(1) + f(0)) + f(1)) + (f(1) + f(0)))
f(5) => f(4) + f(3) => (((f(1) + f(0)) + f(1)) + (f(1) + f(0))) + ((f(1) + f(0)) + f(1)))
"""

"""
     /\
    /\/\
  /\/\/\/\
"""
    

