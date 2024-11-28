###

list = [x for x in range(0,21)]

def cuadrados(number):
    return number ** 2

new_list = [cuadrados(i) for i in list]
print(new_list)