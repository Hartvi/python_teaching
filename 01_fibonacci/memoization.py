
def add(a, b):
    res = a + b
    print("result: ", res)
    return res


some_number = 5
some_number2 = 10

some_number3 = add(some_number, some_number2)  # => ((a + b) + a)

print(f"{some_number} + {some_number2}: {some_number3}")

print("END ADD SECTION\n\n")
# 1000000 + 87489149519


cached_results = dict()  # {1: 10, 2: 20}
# inputs_results[1] => 10
def memoized_add(a, b):
    inputs = (a, b)  # tuple, coz je nemenny list
    # dictionary["dfgjinrenrj"] "dfgjinrenrj" => hash, coz je dlouhy cely cislo 216594
    # a = [1, 2, 3]
    # dictionary[a] = "abc" => hash 123 => 
    # a.append(4)
    # dictionary[a] co je ve slovniku za hodnotu pro tenhle klic?
    # [1, 2, 3, 4] => "abcd" => hash 1234 => neexistuje => error

    if inputs in cached_results:
        return cached_results[inputs]
    else:
        # f(inputs)
        res = a + b
        cached_results[inputs] = res
        return res

import random

n = 5000

test_inputs = [[                   ],  # a's 
               [                   ]]  # b's

for _ in range(n):
    rand_a = random.randint(0, 1000)
    test_inputs[0].append(rand_a)

    rand_b = random.randint(0, 1000)
    test_inputs[1].append(rand_b)

print("Length of test:", len(test_inputs[0]))

for i in range(n):
    a_i = test_inputs[0][i]
    b_i = test_inputs[1][i]

    print("Results match: ", add(a_i, b_i) == memoized_add(a_i, b_i))


add(2, 1)  # a=2, b=1
add(b=1, a=2)  # **{b: 1, a: 2}