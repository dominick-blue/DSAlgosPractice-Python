import math


x = float(input())
y = float(input())
z = float(input())

x_powerz = x**z
x_power_of_powerz = x**(y**z)
absolute_value = abs(x-y)
square_root = math.sqrt(x**z) 

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(x_powerz, x_power_of_powerz, absolute_value, square_root))