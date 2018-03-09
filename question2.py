"""
def function(data):
    ss, s, n = reduce(lambda a, b: map(sum, zip(a,b)), [(x*x, x, 1) for x in data])
    return (ss - s*s/n) / n

returns (\sum x^2 - (\sum x)^2 / n ) / n

( \sum (x^2) ) / n - (\sum x / n)^2
"""

def function(data):
    len_data = len(data)
    sum_data = sum(data)
    sum_data_sqr = sum(map(lambda x: x * x, data))
    return sum_data_sqr / len_data - (sum_data / len_data) ** 2
