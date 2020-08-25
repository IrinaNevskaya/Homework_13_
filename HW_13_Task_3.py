# Task 3
# Write a function called `choose_func` which takes a list of nums and 2 callback functions.
# If all nums inside the list are positive, execute the first function on that list and return the result of it.
# Otherwise, return the result of the second one

def square(elem):
    return elem ** 2

def sum(elem):
    return elem + 5

def mul(elem):
    return elem * 10

def our_functions(func_tupl):
    def func(elem):
        for sam_func in func_tupl:
            elem = sam_func(elem)
        return elem
    return func

def choose_func(nums_list,*args):
    new_list = []
    for i in nums_list:
        if i > 0:
            new_list.append(i)
    return list(map(our_functions(args), new_list))

nums_list = [-1,-9,10,-10]
print(choose_func(nums_list, square, sum, mul))

