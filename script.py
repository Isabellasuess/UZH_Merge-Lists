#!/usr/bin/env python3

# This signature is required for the automated grading to work.
# Do not rename the function or change its list of parameters!

def merge(a, b):

    mergelist = []

    if len(a) == 0 or len(b) == 0:
        return []

    if len(a) > len(b):
        b.append(b[-1])

    if len(b) > len(a):
        a.append(a[-1])

    if len(a) == len(b):
        result = zip(a, b)
        mergelist = list(result)

    return mergelist



# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!
print(merge([0, 1, 2], [5, 6]))
