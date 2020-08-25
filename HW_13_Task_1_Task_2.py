# Task 1
# Write a Python program to detect the number of local variables declared in a function.

def sum_sam_num (a,b,c,d):
    sum = a + b + c + d
    return sum

(print(sum_sam_num.__code__.co_nlocals))

# Task 2
# Write a Python program to access a function inside a function
# (Tips: use function, which returns another function)

def sam_func(*args):
    my_list = list(args)
    list_7 = []
    def filt():
        for i in my_list:
            if i % 7 == 0 and i > 0:
                list_7.append(i)
        return list_7
    return filt

a = sam_func(1,7,3,49,14,50,70)
print(a())

