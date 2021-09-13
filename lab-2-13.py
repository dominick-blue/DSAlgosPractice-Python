mpg = float(input())
gas_cost = float(input())
per_mile = gas_cost / mpg
miles_20 = per_mile * 20
miles_75 = per_mile * 75
miles_500 = per_mile * 500


print('{:.2f} {:.2f} {:.2f}'.format(miles_20, miles_75, miles_500))
