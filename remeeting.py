from functools import reduce

def function(data):
    ss, s, n = reduce(lambda a, b: map(sum, zip(a,b)), [(x*x, x, 1) for x in data])
    return (ss - s*s/n) / n

"""
reduce is "reducing" function - lambda a, b: map(sum, zip(a,b))
on the list of tuples [(x * x, x, 1), (x * x, x, 1)]

Look at the function -
map(sum, zip(a,b)).
    zip(a,b): (a1, b1), (a2, b2), ...
    map(sum, zip(a,b)) =

n returns "number of elements in data"
s returns "sum of elements in data"
ss returns "sum of square of elements in data"

If input integer,
returns (x^2 - x^2/n) / n

Input (a, b, c, d...)

returns (\sum x^2 - (\sum x)^2 / n ) / n

--> ( \sum (x^2) ) / n - (\sum x / n)^2
-->
"""
def function2(data):
    """

    """
    len_data = len(data)
    sum_data = sum(data)
    sum_data_sqr = sum(map(lambda x: x * x, data))
    return sum_data_sqr / len_data - (sum_data / len_data) ** 2

"""
QUESTION 2: 144
LOOK AT IPYNB
"""
