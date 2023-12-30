# this is a comment


print("Hello world")

a = 1  # this is an integer
b = 1.2  # this is a float
# float normally has 32bit precision
# double normally has 64 bit precision = 32*2
# between 0-1 they are most precise and then get less precise as the size increases
# 1/10 in reality equals 0.1000000000001 <= some finite precision

c = "This is a string"  # a string is an array (or sometimes called list) of characters
# "as d" = ["a", "s", " ", "d"]
print(c[1])

d = ["this", "is", "a", "list", "This is a string", 1, b]  # a list is an ordered collection of elements

print(d[0])
print(d[2])

print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# the following line throws an error:
# print(a+b+c+d)


# write `d.` and then press `ctrl+space`
# d.
# uncomment the above line using `ctrl+/`

# append
d.append(c)

print("d after appending:", d)

# lets try appending a number
d.append(a)
d.append(b)
print("d after appending 'a' and 'b':", d)

# len(d) = length of list `d`
# range(number) creates an iterator like 0, 1, ..., number-1
# example: range(5) generates 0, 1, 2, 3, 4 - so in total 5 numbers, starting with `0`
# for iterates over a list or iterator

# to iterate means to go element by element

# equals 7 because len(d) == 7
length_of_array = len(d)  # len gives you the length of a list
# this means that len(d) is an integer

# then we plug the length into range(integer)
# range(7) => 0,1,2,3,4,5,6
# and as we know from above, range(3) for example gives you 0,1,2
for i in range(length_of_array):
    print("i:", i)  # 0 - 6
    print("i:", i)
    # "aasd"  + "ddd" = "aasdddd"
    # i = e.g. 5 => str(5) = "5"
    print("d[" + str(i) + "]:", d[i])

    print(f"d[{i}]:", d[i])

    print(f"type of '{d[i]}':", type(d[i]))

