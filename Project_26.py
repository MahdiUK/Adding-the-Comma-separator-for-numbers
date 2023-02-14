def add_comma_separator(num):
    return 'Your sorted number by comma is: {:,}'.format(num)
num = int(input("please enter your amount of money: "))
result = add_comma_separator(num)
print(result)
        