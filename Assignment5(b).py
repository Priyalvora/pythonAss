
def Prime(x):
    for n in range(2,x):
        if x % n == 0:
            return False
        else:
            return True
x_one = filter(Prime, range(1, 2500))
print(list(x_one))