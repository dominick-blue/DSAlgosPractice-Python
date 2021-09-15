quarters = int(input()) * 0.25
dimes = int(input()) * 0.10 
nickels = int(input()) * 0.05
pennies = int(input()) * 0.01

dollars = quarters + dimes + nickels + pennies

print(f'Amount: ${dollars:.2f}')

