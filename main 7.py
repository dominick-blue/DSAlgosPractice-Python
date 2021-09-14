import math

print('Please enter two angles in degrees:')

first_input = int(input())
second_input = int(input())

first_input_radians = math.radians(first_input)
second_input_radians = math.radians(second_input)

first_input_sine = math.sin(first_input_radians)
second_input_sine = math.sin(second_input_radians)

first_input_cosine = math.cos(first_input_radians)
second_input_cosine = math.cos(second_input_radians)

total = (first_input_sine * second_input_cosine) + (first_input_cosine * second_input_sine)
limit_float = round(total, 2)

print('You entered α =',first_input)
print('You entered β =',second_input)
print('\n\nsin({0}+{1})can be found by performing the following trig identity:\nsin(α+β) = sin(α)cos(β) + cos(α)sin(β)\n\n'.format(first_input, second_input))
print('''Therefore:
sin({0}+{1}) = sin({0})cos({1}) + cos({0})sin({1})
=({2:.2f})({5:.2f}) + ({4:.2f})({3:.2f})
={6}'''.format(first_input, second_input, first_input_sine, second_input_sine, first_input_cosine, second_input_cosine, limit_float))